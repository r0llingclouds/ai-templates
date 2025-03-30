# %% [markdown]
# # BeeAI ReAct agents
# 
# The BeeAI ReAct agent is a pre-configured implementation of the ReAct (Reasoning and Acting) pattern. It can be customized with tools and instructions to suit different tasks.
# 
# The ReAct pattern is a framework used in AI models, particularly language models, to separate the reasoning process from the action-taking process. This pattern enhances the model's ability to handle complex queries by enabling it to:
# 
# - Reason about the problem.
# - Decide on an action to take.
# - Observe the result of that action to inform further reasoning and actions.
# 
# The ReAct agent provides a convenient out-of-the-box agent implementation that makes it easier to build agents using this pattern.

# %% [markdown]
# ## Basic ReAct Agent
# 
# To configure a ReAct agent, you need to define a ChatModel and construct a Agent.
# 
# In this example, we won't provide any external tools to the agent. It will rely solely on its own memory to provide answers. This is a basic setup where the agent tries to reason and act based on the context it has built internally.
# 
# Try modifying the input text in the call to agent.run() to experiment with obtaining different answers. This will help you see how the agent's reasoning and response vary with different prompts.

# %%
from typing import Any

from beeai_framework.agents.react.agent import ReActAgent
from beeai_framework.agents.react.types import ReActAgentRunOutput
from beeai_framework.backend.chat import ChatModel
from beeai_framework.emitter.emitter import Emitter, EventMeta
from beeai_framework.emitter.types import EmitterOptions
from beeai_framework.memory.unconstrained_memory import UnconstrainedMemory

# Construct ChatModel
# chat_model: ChatModel = ChatModel.from_name("ollama:granite3.1-dense:8b")

import os
from dotenv import load_dotenv

load_dotenv()

# Create a ChatModel to interface with granite3.1-dense:8b on a local ollama
model = ChatModel.from_name(
    "watsonx:ibm/granite-3-8b-instruct",
    options={
        "project_id": os.getenv("WATSONX_PROJECT_ID"),
        "api_key": os.getenv("WATSONX_API_KEY"),
        "api_base": os.getenv("WATSONX_API_URL"),
    },
)

# Construct Agent instance with the chat model
agent = ReActAgent(llm=model, tools=[], memory=UnconstrainedMemory())


async def process_agent_events(event_data: Any, event_meta: EventMeta) -> None:
    """Process agent events and log appropriately"""

    if event_meta.name == "error":
        print("Agent 🤖 : ", event_data.error)
    elif event_meta.name == "retry":
        print("Agent 🤖 : ", "retrying the action...")
    elif event_meta.name == "update":
        print(f"Agent({event_data.update.key}) 🤖 : ", event_data.update.parsed_value)


# Observe the agent
async def observer(emitter: Emitter) -> None:
    emitter.on("*.*", process_agent_events, EmitterOptions(match_nested=True))


# Run the agent
result: ReActAgentRunOutput = await agent.run("What chemical elements make up a water molecule?").observe(observer)

# %% [markdown]
# ## Using Tools
# 
# To go beyond just chatting with an LLM, you can provide tools to the agent. This enables the agent to perform specific tasks and interact with external systems, enhancing its functionality. There are different ways to add tools to the agent:
# 
# - Built-in tools from the framework: BeeAI provides several built-in tools that you can easily integrate with your agent.
# - Importing tools from other libraries: You can bring in external tools or APIs to extend your agent's capabilities.
# - Custom tooling: You can also write your own custom tools tailored to your specific use case.
# 
# By equipping the agent with these tools, you allow it to perform more complex actions, such as querying databases, interacting with APIs, or manipulating data.
# 
# ## Built-in tools
# 
# BeeAI comes with several built-in tools that are part of the library, which can be easily imported and added to your agent.
# 
# In this example, we provide the agent with a weather forecast lookup tool called OpenMeteoTool. With this tool, the agent can retrieve real-time weather data, enabling it to answer weather-related queries with more accuracy.
# 
# Follow the agent's thoughts and actions to understand how it approaches and solves the problem.

# %%
from beeai_framework.backend.chat import ChatModel
from beeai_framework.tools.weather.openmeteo import OpenMeteoTool

import os
from dotenv import load_dotenv

load_dotenv()

# Create a ChatModel to interface with granite3.1-dense:8b on a local ollama
model = ChatModel.from_name(
    "watsonx:ibm/granite-3-8b-instruct",
    options={
        "project_id": os.getenv("WATSONX_PROJECT_ID"),
        "api_key": os.getenv("WATSONX_API_KEY"),
        "api_base": os.getenv("WATSONX_API_URL"),
    },
)

# create an agent using the default LLM and add the OpenMeteoTool that is capable of fetching weather-based information
agent = ReActAgent(llm=model, tools=[OpenMeteoTool()], memory=UnconstrainedMemory())


# Run the agent
result: ReActAgentRunOutput = await agent.run("What's the current weather in London?").observe(observer)

# %% [markdown]
# ### Imported Tools
# 
# Tools can also be imported from other libraries to extend the functionality of your agent. For example, you can integrate tools from libraries like LangChain to give your agent access to even more capabilities.
# 
# Here’s an example showing how to integrate the Wikipedia tool from LangChain, written in long form (without using the @tool decorator):

# %%
from typing import Any

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from pydantic import BaseModel, Field

from beeai_framework.agents.react.agent import ReActAgent
from beeai_framework.context import RunContext
from beeai_framework.tools import StringToolOutput, Tool
from beeai_framework.tools.types import ToolRunOptions


class LangChainWikipediaToolInput(BaseModel):
    query: str = Field(description="The topic or question to search for on Wikipedia.")


class LangChainWikipediaTool(Tool[LangChainWikipediaToolInput, ToolRunOptions, StringToolOutput]):
    """Adapter class to integrate LangChain's Wikipedia tool with our framework"""

    name = "Wikipedia"
    description = "Search factual and historical information from Wikipedia about given topics."
    input_schema = LangChainWikipediaToolInput

    def __init__(self) -> None:
        super().__init__()
        self._wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

    def _create_emitter(self) -> Emitter:
        return Emitter.root().child(
            namespace=["tool", "search", "langchain_wikipedia"],
            creator=self,
        )

    async def _run(
        self, input: LangChainWikipediaToolInput, options: ToolRunOptions | None, context: RunContext
    ) -> StringToolOutput:
        query = input.query
        try:
            result = self._wikipedia.run(query)
            return StringToolOutput(result=result)
        except Exception as e:
            print(f"Wikipedia search error: {e!s}")
            return f"Error searching Wikipedia: {e!s}"


import os
from dotenv import load_dotenv

load_dotenv()

# Create a ChatModel to interface with granite3.1-dense:8b on a local ollama
model = ChatModel.from_name(
    "watsonx:ibm/granite-3-8b-instruct",
    options={
        "project_id": os.getenv("WATSONX_PROJECT_ID"),
        "api_key": os.getenv("WATSONX_API_KEY"),
        "api_base": os.getenv("WATSONX_API_URL"),
    },
)

agent = ReActAgent(llm=model, tools=[LangChainWikipediaTool()], memory=UnconstrainedMemory())

result: ReActAgentRunOutput = await agent.run("Who is the current president of the European Commission?").observe(
    observer
)

# %% [markdown]
# The previous example can be re-written in a shorter form by adding the @tool decorator, which simplifies the tool definition. Here's how you can do it:

# %%
from langchain_community.tools import WikipediaQueryRun  # noqa: F811
from langchain_community.utilities import WikipediaAPIWrapper  # noqa: F811

from beeai_framework.agents.react.agent import ReActAgent
from beeai_framework.tools import Tool, tool


# defining a tool using the `tool` decorator
# Note: the pydoc is important as it serves as the tool description to the agent
@tool
def langchain_wikipedia_tool(query: str) -> str:
    """
    Search factual and historical information, including biography, history, politics, geography, society, culture,
    science, technology, people, animal species, mathematics, and other subjects.

    Args:
        query: The topic or question to search for on Wikipedia.

    Returns:
        The information found via searching Wikipedia.
    """
    wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
    return wikipedia.run(query)


# using the tool in an agent
# Set up credentials for WatsonX
import os
from dotenv import load_dotenv

load_dotenv()

# Create a ChatModel to interface with granite3.1-dense:8b on a local ollama
model = ChatModel.from_name(
    "watsonx:ibm/granite-3-8b-instruct",
    options={
        "project_id": os.getenv("WATSONX_PROJECT_ID"),
        "api_key": os.getenv("WATSONX_API_KEY"),
        "api_base": os.getenv("WATSONX_API_URL"),
    },
)

agent = ReActAgent(llm=model, tools=[langchain_wikipedia_tool], memory=UnconstrainedMemory())

result: ReActAgentRunOutput = await agent.run("What is the longest living vertebrate?").observe(observer)


