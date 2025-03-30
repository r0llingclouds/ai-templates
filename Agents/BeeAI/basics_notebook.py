# %% [markdown]
# ## BeeAI Framework Basics
# 
# These examples demonstrate fundamental usage patterns of BeeAI in Python. They progressively increase in complexity, providing a well-rounded overview of the framework.

# %% [markdown]
# ## Prompt Templates
# 
# One of the core constructs in the BeeAI framework is the PromptTemplate. It allows you to dynamically insert data into a prompt before sending it to a language model. BeeAI uses the Mustache templating language for prompt formatting.
# 
# The following example demonstrates how to create a Retrieval-Augmented Generation (RAG) template and apply it to your data to generate a structured prompt.

# %%


# %%
from pydantic import BaseModel

from beeai_framework.template import PromptTemplate, PromptTemplateInput


# Defines the structure of the input data that can passed to the template i.e. the input schema
class RAGTemplateInput(BaseModel):
    question: str
    context: str


# Define the prompt template
rag_template: PromptTemplate = PromptTemplate(
    PromptTemplateInput(
        schema=RAGTemplateInput,
        template="""
Context: {{context}}
Question: {{question}}

Provide a concise answer based on the context. Avoid statements such as 'Based on the context' or 'According to the context' etc. """,
    )
)

# Render the template using an instance of the input model
prompt = rag_template.render(
    RAGTemplateInput(
        question="What is the capital of France?",
        context="France is a country in Europe. Its capital city is Paris, known for its culture and history.",
    )
)

# Print the rendered prompt
print(prompt)

# %% [markdown]
# ## More complex templates
# 
# The previous example demonstrated a simple template, but the PromptTemplate class can also handle more complex structures and incorporate conditional logic.
# 
# The following example showcases a template that includes a question along with a set of detailed search results represented as a list.

# %%
from pydantic import BaseModel

from beeai_framework.template import PromptTemplate, PromptTemplateInput


# Individual search result
class SearchResult(BaseModel):
    title: str
    url: str
    content: str


# Input specification
class SearchTemplateInput(BaseModel):
    question: str
    results: list[SearchResult]


# Define the template, in this instance the template will iterate over the results
search_template: PromptTemplate = PromptTemplate(
    PromptTemplateInput(
        schema=SearchTemplateInput,
        template="""
Search results:
{{#results.0}}
{{#results}}
Title: {{title}}
Url: {{url}}
Content: {{content}}
{{/results}}
{{/results.0}}

Question: {{question}}
Provide a concise answer based on the search results provided.""",
    )
)

# Render the template using an instance of the input model
prompt = search_template.render(
    SearchTemplateInput(
        question="What is the capital of France?",
        results=[
            SearchResult(
                title="France",
                url="https://en.wikipedia.org/wiki/France",
                content="France is a country in Europe. Its capital city is Paris, known for its culture and history.",
            ),
            SearchResult(
                title="England",
                url="https://en.wikipedia.org/wiki/England",
                content="England is a country in Europe. Its capital city is London, known for its culture and history.",
            )
        ],
    )
)

# Print the rendered prompt
print(prompt)

# %% [markdown]
# ## The ChatModel
# 
# Once you have a PromptTemplate and can easily render prompts, you’re ready to start interacting with a model. BeeAI supports a variety of LLMs through the ChatModel interface.
# 
# In this section, we will use the IBM `Granite 3.1 8B` language model via the Ollama provider.
# 
# If you haven't set up Ollama yet, follow the [guide on running Granite 3.1 using Ollama](https://www.ibm.com/granite/docs/run/granite-on-mac/granite/) for mac, or for other platforms use the [Ollama documentation](https://ollama.com) and [IBM Granite model page](https://ollama.com/library/granite3.1-dense:8b).
# 
# ⚡ If you would prefer to use watsonx then you should check out [watsonx.ipynb](watsonx.ipynb) and edit the following examples to use a watsonx ChatModel provider. ⚡
# 
# Before creating a ChatModel, we need to briefly discuss Messages. The ChatModel operates using message-based interactions, allowing you to structure conversations between the user and the assistant (LLM) naturally.
# 
# Let’s start by creating a UserMessage to greet the assistant and ask a simple question.

# %%
from beeai_framework.backend.message import UserMessage

# Create a user message to start a chat with the model
user_message = UserMessage(content="Hello! Can you tell me what is the capital of France?")

# %% [markdown]
# We can now create a ChatModel and send this message to Granite for processing.

# %%
from beeai_framework.backend.chat import ChatModel
from beeai_framework.backend.types import ChatModelOutput
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

output: ChatModelOutput = await model.create(messages=[user_message])

print(output.get_text_content())

# %% [markdown]
# ## Memory 
# The model has provided a response! We can now start to build up a `Memory`. Memory is just a convenient way of storing a set of messages that can be considered as the history of the dialog between the user and the llm.
# 
# In this next example we will construct a memory from our existing messages and add a new user message. Notice that the new message can implicitly refer to content from prior messages. Internally the `ChatModel` formats all the messages and sends them to the LLM.

# %%
from beeai_framework.backend.message import AssistantMessage
from beeai_framework.memory.unconstrained_memory import UnconstrainedMemory

memory = UnconstrainedMemory()

await memory.add_many(
    [
        user_message,
        AssistantMessage(content=output.get_text_content()),
        UserMessage(content="If you had to recommend one thing to do there, what would it be?"),
    ]
)

output: ChatModelOutput = await model.create(messages=memory.messages)

print(output.get_text_content())

# %%
memory.messages[0].text

# %% [markdown]
# ## Combining Templates and Messages
# 
# To use a PromptTemplate with the Granite ChatModel, you can render the template and then place the resulting content into a Message. This allows you to dynamically generate prompts and pass them along as part of the conversation flow.

# %%
# Some context that the model will use to provide an answer. Source wikipedia: https://en.wikipedia.org/wiki/Ireland
context = """The geography of Ireland comprises relatively low-lying mountains surrounding a central plain, with several navigable rivers extending inland.
Its lush vegetation is a product of its mild but changeable climate which is free of extremes in temperature.
Much of Ireland was woodland until the end of the Middle Ages. Today, woodland makes up about 10% of the island,
compared with a European average of over 33%, with most of it being non-native conifer plantations.
The Irish climate is influenced by the Atlantic Ocean and thus very moderate, and winters are milder than expected for such a northerly area,
although summers are cooler than those in continental Europe. Rainfall and cloud cover are abundant.
"""

# Lets reuse our RAG template from earlier!
prompt = rag_template.render(RAGTemplateInput(question="How much of Ireland is forested?", context=context))

output: ChatModelOutput = await model.create(messages=[UserMessage(content=prompt)])

print(output.get_text_content())

# %% [markdown]
# ## Structured Outputs
# 
# Often, you'll want the LLM to produce output in a specific format. This ensures reliable interaction between the LLM and your code—such as when you need the LLM to generate input for a function or tool. To achieve this, you can use structured output.
# 
# In the example below, we will prompt Granite to generate a character using a very specific format.

# %%
from typing import Literal

from pydantic import Field


# The output structure definition, note the field descriptions that can help the LLM to understand the intention of the field.
class CharacterSchema(BaseModel):
    name: str = Field(description="The name of the character.")
    occupation: str = Field(description="The occupation of the character.")
    species: Literal["Human", "Insectoid", "Void-Serpent", "Synth", "Ethereal", "Liquid-Metal"] = Field(
        description="The race of the character."
    )
    back_story: str = Field(description="Brief backstory of this character.")


user_message = UserMessage(
    "Create a fantasy sci-fi character for my new game. This character will be the main protagonist, be creative."
)

response = await model.create_structure(schema=CharacterSchema, messages=[user_message])

print(response.object)

# %% [markdown]
# ## System Prompts
# 
# The SystemMessage is a special message type that can influence the general behavior of an LLM. By including a SystemMessage, you can provide high-level instructions that shape the LLM’s overall response style. The system message typically appears as the first message in the model’s memory.
# 
# In the example below, we add a system message that instructs the LLM to speak like a pirate!

# %%
from beeai_framework.backend.message import SystemMessage

system_message = SystemMessage(content="You are pirate. You always respond using pirate slang.")
user_message = UserMessage(content="What is a baby hedgehog called?")
output: ChatModelOutput = await model.create(messages=[system_message, user_message])

print(output.get_text_content())

# %% [markdown]
# ## Building an Agent
# 
# You’re now ready to build your first agent! Proceed to the [workflows.ipynb](workflows.ipynb) notebook to continue.


