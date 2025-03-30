# %% [markdown]
# # watsonx X BeeAI 
# 
# This notebook showcases a series of examples that demonstrate how to integrate BeeAI with watsonx.
# 
# To run these examples, you'll need a set of watsonx credentials:
# 
# - WATSONX_API_KEY
# - WATSONX_PROJECT_ID
# - WATSONX_API_URL
# 
# Please enter your credentials in the next cell before proceeding.

# %%
WATSONX_API_KEY = ""
WATSONX_PROJECT_ID = ""
WATSONX_API_URL = ""

# %% [markdown]
# ## WatsonX ChatModel
# 
# This example demonstrates how to create a ChatModel to interface with the ibm/granite-3-8b-instruct model from watsonx.

# %%
from beeai_framework.backend.chat import ChatModel
from beeai_framework.backend.message import UserMessage
from beeai_framework.backend.types import ChatModelOutput

# Create a ChatModel to interface with ibm/granite-3-8b-instruct from watsonx
model = ChatModel.from_name(
    "watsonx:ibm/granite-3-8b-instruct",
    options={
        "project_id": WATSONX_PROJECT_ID,
        "api_key": WATSONX_API_KEY,
        "api_base": WATSONX_API_URL,
    },
)

message = UserMessage(content="Briefly explain quantum computing in simple terms with an example.")
output: ChatModelOutput = await model.create(messages=[message])

print(output.get_text_content())

# %% [markdown]
# ## Structured Outputs With watsonx
# 
# This example demonstrates how to generate structured output using the ibm/granite-3-8b-instruct model from watsonx.

# %%
import json

from pydantic import BaseModel, Field


# The output structure definition, note the field descriptions that can help the LLM to understand the intention of the field.
class BookDetailsSchema(BaseModel):
    title: str = Field(description="The title of the book.")
    author: str = Field(description="The author of the book.")
    plot_summary: str = Field(description="A brief summary of the plot.")


user_message = UserMessage("Provide a summary of the following book: 'Dune' by Frank Herbert.")

response = await model.create_structure(schema=BookDetailsSchema, messages=[user_message])

print(json.dumps(response.object, indent=4))


