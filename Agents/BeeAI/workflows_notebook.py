# %% [markdown]
# # BeeAI Workflows
# 
# In the previous notebook, you learned the basics of the BeeAI framework, including PromptTemplates, Messages, Memory, Model Backends, and various forms of output generation (freeform and structured). In this notebook, we will focus on Workflows.
# 
# Workflows enable you to combine what you've already learned to develop an AI agent. The agent's behavior is defined through workflow steps and the transitions between them. You can think of a Workflow as a graph that outlines the agent's behavior.

# %% [markdown]
# ## Basics of Workflows
# 
# The main components of a BeeAI workflow are state, defined as a Pydantic model, and steps, which are Python functions.
# 
# - State: Think of state as structured memory that the workflow can read from and write to during execution. It holds the data that flows through the workflow.
# - Steps: These are the functional components of the workflow, connecting together to perform the agent’s actions.
# 
# The following simple workflow example highlights these key features:
# 
# - The state definition includes a required message field.
# - The step (my_first_step) is defined as a function that takes the state instance as a parameter.
# - The state can be modified within a step, and changes to the state are preserved across steps and workflow executions.
# - The step function returns a string (Workflow.END), indicating the name of the next step (this is how step transitions are handled).
# - Workflow.END signifies the end of the workflow.

# %%
import traceback

from pydantic import BaseModel, ValidationError

from beeai_framework.workflows.workflow import Workflow, WorkflowError


# Define global state that is accessible to each step in the workflow graph
# The message field is required when instantiating the state object
class MessageState(BaseModel):
    message: str


# Each step in the workflow is defined as a python function
async def my_first_step(state: MessageState) -> None:
    state.message += " World"  # Modify the state
    print("Running first step!")
    return Workflow.END


try:
    # Define the structure of the workflow graph
    basic_workflow = Workflow(schema=MessageState, name="MyWorkflow")

    # Add a step, each step has a name and a function that implements the step
    basic_workflow.add_step("my_first_step", my_first_step)

    # Execute the workflow
    basic_response = await basic_workflow.run(MessageState(message="Hello"))

    print("State after workflow run:", basic_response.state)

except WorkflowError:
    traceback.print_exc()
except ValidationError:
    traceback.print_exc()

# %% [markdown]
# ## A Multi-Step Workflow with Tools
# 
# Now that you understand the basic components of a Workflow, let’s explore the power of BeeAI Workflows by building a simple web search agent.
# 
# This agent creates a search query based on an input question, runs the query to retrieve search results, and then generates an answer to the question based on the results.
# 
# Let’s begin by importing the necessary modules.

# %%
from langchain_community.utilities import SearxSearchWrapper
from pydantic import Field

from beeai_framework.backend.chat import ChatModel
from beeai_framework.backend.message import UserMessage
from beeai_framework.backend.types import ChatModelOutput, ChatModelStructureOutput
from beeai_framework.template import PromptTemplate, PromptTemplateInput

# %% [markdown]
# Next, we can define our workflow State.
# 
# In this case, the question field is required when instantiating the State. The other fields, search_results and answer, are optional during construction (defaulting to None), but they will be populated by the workflow steps as the execution progresses.

# %%
# Workflow State
class SearchAgentState(BaseModel):
    question: str
    search_results: str | None = None
    answer: str | None = None

# %% [markdown]
# Next, we define the ChatModel instance that will handle interaction with our LLM. For this example, we'll use IBM Granite 3.1 8B. This model will be used to process the search query and generate answers based on the retrieved results.

# %%
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

# %% [markdown]
# Since this is a web search agent, we need a way to run web searches. For that, we'll use the SearxSearchWrapper from the Langchain community tools project.
# 
# To use the SearxSearchWrapper, you'll need to set up a local SearXNG service.
# 
# Follow the instructions in [searXNG.md](searXNG.md) to configure your local SearXNG instance before proceeding.

# %%
# Web search tool
search_tool = SearxSearchWrapper(searx_host="http://127.0.0.1:8888")

# %%


# %% [markdown]
# In this workflow, we make extensive use of PromptTemplates and structured outputs.
# 
# Here, we define the various templates, input schemas, and structured output schemas that are essential for implementing the agent. These templates will allow us to generate the search query and structure the results in a way that the agent can process effectively.

# %%
# PromptTemplate Input Schemas
class QuestionInput(BaseModel):
    question: str


class SearchRAGInput(BaseModel):
    question: str
    search_results: str


# Prompt Templates
search_query_template = PromptTemplate(
    PromptTemplateInput(
        schema=QuestionInput,
        template="""Convert the following question into a concise, effective web search query using keywords and operators for accuracy.
Question: {{question}}""",
    )
)

search_rag_template = PromptTemplate(
    PromptTemplateInput(
        schema=SearchRAGInput,
        template="""Search results:
{{search_results}}

Question: {{question}}
Provide a concise answer based on the search results provided. If the results are irrelevant or insufficient, say 'I don't know.' Avoid phrases such as 'According to the results...'.""",
    )
)


# Structured output Schemas
class WebSearchQuery(BaseModel):
    query: str = Field(description="The web search query.")

# %% [markdown]
# Now, we can define the first step of the workflow, named web_search.
# 
# In this step:
# 
# - The LLM is prompted to generate an effective search query using the search_query_template.
# - The generated search query is then used to run a web search via the search tool (SearxSearchWrapper).
# - The search results are stored in the search_results field of the workflow state.
# - Finally, the step returns generate_answer, passing control to the next step, named generate_answer.

# %%
async def web_search(state: SearchAgentState) -> str:
    print("Step: ", "web_search")
    # Generate a search query
    prompt = search_query_template.render(QuestionInput(question=state.question))
    response: ChatModelStructureOutput = await model.create_structure(
        schema=WebSearchQuery, messages=[UserMessage(prompt)]
    )

    # Run search and store results in state
    try:
        state.search_results = str(search_tool.run(response.object["query"]))
    except Exception as e:
        print(e)
        print("Search tool failed! Agent will answer from memory.")
        state.search_results = "No search results available."

    return "generate_answer"

# %% [markdown]
# The next step in the workflow is generate_answer.
# 
# This step:
# 
# - Takes the question and search_results from the workflow state.
# - Uses the search_rag_template to generate an answer based on the provided data.
# - The generated answer is stored in the workflow state.
# - Finally, the workflow ends by returning Workflow.END, signaling the completion of the agent’s task.

# %%
async def generate_answer(state: SearchAgentState) -> str:
    print("Step: ", "generate_answer")
    # Generate answer based on question and search results from previous step.
    prompt = search_rag_template.render(
        SearchRAGInput(question=state.question, search_results=state.search_results or "No results available.")
    )
    output: ChatModelOutput = await model.create(messages=[UserMessage(prompt)])

    # Store answer in state
    state.answer = output.get_text_content()
    return Workflow.END

# %% [markdown]
# Finally, we define the overall workflow and add the steps we developed earlier. This combines everything into a cohesive agent that can perform web searches and generate answers.

# %%
try:
    # Define the structure of the workflow graph
    search_agent_workflow = Workflow(schema=SearchAgentState, name="WebSearchAgent")
    search_agent_workflow.add_step("web_search", web_search)
    search_agent_workflow.add_step("generate_answer", generate_answer)

    # Execute the workflow
    search_response = await search_agent_workflow.run(
        SearchAgentState(question="What is the term for a baby hedgehog?")
    )

    print("*****")
    print("Question: ", search_response.state.question)
    print("Answer: ", search_response.state.answer)

except WorkflowError:
    traceback.print_exc()
except ValidationError:
    traceback.print_exc()

# %% [markdown]
# # Adding Memory to a Workflow Agent
# 
# The web search agent from the previous example can answer questions, but it cannot engage in a conversation because it doesn't maintain message history.
# 
# In the next example, we'll show you how to add memory to your agent, allowing it to interactively chat while keeping track of the conversation history. This will enable the agent to remember previous interactions and provide more context-aware responses.

# %%
# Workflow State
from pydantic import InstanceOf

from beeai_framework.backend.message import AssistantMessage, SystemMessage
from beeai_framework.memory.unconstrained_memory import UnconstrainedMemory


class ChatState(BaseModel):
    memory: InstanceOf[UnconstrainedMemory]
    output: str | None = None


async def chat(state: ChatState) -> str:
    output: ChatModelOutput = await model.create(messages=state.memory.messages)
    state.output = output.get_text_content()
    return Workflow.END


memory = UnconstrainedMemory()
await memory.add(SystemMessage(content="You are a helpful and friendly AI assistant."))

try:
    # Define the structure of the workflow graph
    chat_workflow = Workflow(ChatState)
    chat_workflow.add_step("chat", chat)
    chat_workflow.add_step("generate_answer", generate_answer)

    while True:
        user_input = input("User (type 'exit' to stop): ")
        if user_input == "exit":
            break
        # Add user message to memory
        await memory.add(UserMessage(content=user_input))
        # Run workflow with memory
        response = await chat_workflow.run(ChatState(memory=memory))
        # Add assistant response to memory
        await memory.add(AssistantMessage(content=response.state.output))
        print("Assistant: ", response.state.output)

except WorkflowError:
    traceback.print_exc()
except ValidationError:
    traceback.print_exc()

# %% [markdown]
# ## ReAct Agents
# 
# You are now familiar with Workflow based agents, next you can explore pre-canned ReAct agents. Move on to [agents.ipynb](agents.ipynb).


