ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#furo-main-content)

[Back to top](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#)

[View this page](https://ibm.github.io/watsonx-ai-python-sdk/_sources/fm_model.rst.txt "View this page")

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Model [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html\#model "Link to this heading")

_class_ ibm\_watsonx\_ai.foundation\_models.Model( _model\_id_, _credentials_, _params=None_, _project\_id=None_, _space\_id=None_, _verify=None_, _validate=True_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/model.html#Model) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.Model "Link to this definition")

Bases: [`ModelInference`](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#ibm_watsonx_ai.foundation_models.inference.ModelInference "ibm_watsonx_ai.foundation_models.inference.model_inference.ModelInference")

Instantiate the model interface.

Deprecated since version 1.1.21: Use [`ModelInference()`](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#ibm_watsonx_ai.foundation_models.inference.ModelInference "ibm_watsonx_ai.foundation_models.inference.ModelInference") instead.

Hint

To use the Model class with LangChain, use the [`to_langchain()`](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.Model.to_langchain "ibm_watsonx_ai.foundation_models.Model.to_langchain") function.

Parameters:

- **model\_id** ( _str_) – type of model to use

- **credentials** ( [_Credentials_](https://ibm.github.io/watsonx-ai-python-sdk/base.html#credentials.Credentials "credentials.Credentials") _or_ _dict_) – credentials for the Watson Machine Learning instance

- **params** ( _dict_ _,_ [_TextGenParameters_](https://ibm.github.io/watsonx-ai-python-sdk/fm_schema.html#ibm_watsonx_ai.foundation_models.schema.TextGenParameters "ibm_watsonx_ai.foundation_models.schema.TextGenParameters") _,_ [_TextChatParameters_](https://ibm.github.io/watsonx-ai-python-sdk/fm_schema.html#ibm_watsonx_ai.foundation_models.schema.TextChatParameters "ibm_watsonx_ai.foundation_models.schema.TextChatParameters") _,_ _optional_) – parameters to use during generate requests

- **project\_id** ( _str_ _,_ _optional_) – ID of the Watson Studio project

- **space\_id** ( _str_ _,_ _optional_) – ID of the Watson Studio space

- **verify** ( _bool_ _or_ _str_ _,_ _optional_) –

You can pass one of following as verify:


  - the path to a CA\_BUNDLE file

  - the path of a directory with certificates of trusted CAs

  - True \- default path to truststore will be taken

  - False \- no verification will be made


- **validate** ( _bool_ _,_ _optional_) – model ID validation, defaults to True


Note

One of these parameters is required: \[‘project\_id ‘, ‘space\_id’\].

Hint

You can copy the project\_id from the Project’s Manage tab (Project -> Manage -> General -> Details).

**Example:**

```
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes, DecodingMethods

# To display example params enter
GenParams().get_example_values()

generate_params = {
    GenParams.MAX_NEW_TOKENS: 25
}

model = Model(
    model_id=ModelTypes.FLAN_UL2,
    params=generate_params,
    credentials=Credentials(
        api_key = IAM_API_KEY,
        url = "https://us-south.ml.cloud.ibm.com"),
    project_id="*****"
    )

```

chat( _messages_, _params=None_, _tools=None_, _tool\_choice=None_, _tool\_choice\_option=None_, _context=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/model.html#Model.chat) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.Model.chat "Link to this definition")

Given a list of messages comprising a conversation, the model will return a response.

Parameters:

- **messages** ( _list_ _\[_ _dict_ _\]_) – The messages for this chat session.

- **params** ( _dict_ _,_ [_TextChatParameters_](https://ibm.github.io/watsonx-ai-python-sdk/fm_schema.html#ibm_watsonx_ai.foundation_models.schema.TextChatParameters "ibm_watsonx_ai.foundation_models.schema.TextChatParameters") _,_ _optional_) – meta props for chat generation, use `ibm_watsonx_ai.foundation_models.schema.TextChatParameters.show()`

- **tools** ( _list_) – Tool functions that can be called with the response.

- **tool\_choice** ( _dict_ _,_ _optional_) – Specifying a particular tool via {“type”: “function”, “function”: {“name”: “my\_function”}} forces the model to call that tool.

- **tool\_choice\_option** ( _Literal_ _\[_ _"none"_ _,_ _"auto"_ _\]_ _,_ _optional_) – Tool choice option


Returns:

scoring result containing generated chat content.

Return type:

dict

**Example:**

```
messages = [\
    {"role": "system", "content": "You are a helpful assistant."},\
    {"role": "user", "content": "Who won the world series in 2020?"}\
]
generated_response = model.chat(messages=messages)

# Print all response
print(generated_response)

# Print only content
print(response['choices'][0]['message']['content'])

```

chat\_stream( _messages_, _params=None_, _tools=None_, _tool\_choice=None_, _tool\_choice\_option=None_, _context=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/model.html#Model.chat_stream) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.Model.chat_stream "Link to this definition")

Given a list of messages comprising a conversation, the model will return a response in stream.

Parameters:

- **messages** ( _list_ _\[_ _dict_ _\]_) – The messages for this chat session.

- **params** ( _dict_ _,_ [_TextChatParameters_](https://ibm.github.io/watsonx-ai-python-sdk/fm_schema.html#ibm_watsonx_ai.foundation_models.schema.TextChatParameters "ibm_watsonx_ai.foundation_models.schema.TextChatParameters") _,_ _optional_) – meta props for chat generation, use `ibm_watsonx_ai.foundation_models.schema.TextChatParameters.show()`

- **tools** ( _list_) – Tool functions that can be called with the response.

- **tool\_choice** ( _dict_ _,_ _optional_) – Specifying a particular tool via {“type”: “function”, “function”: {“name”: “my\_function”}} forces the model to call that tool.

- **tool\_choice\_option** ( _Literal_ _\[_ _"none"_ _,_ _"auto"_ _\]_ _,_ _optional_) – Tool choice option


Returns:

scoring result containing generated chat content.

Return type:

generator

**Example:**

```
messages = [\
    {"role": "system", "content": "You are a helpful assistant."},\
    {"role": "user", "content": "Who won the world series in 2020?"}\
]
generated_response = model.chat_stream(messages=messages)

for chunk in generated_response:
    print(chunk['choices'][0]['delta'].get('content', ''), end='', flush=True)

```

generate( _prompt=None_, _params=None_, _guardrails=False_, _guardrails\_hap\_params=None_, _guardrails\_pii\_params=None_, _concurrency\_limit=8_, _async\_mode=False_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/model.html#Model.generate) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.Model.generate "Link to this definition")

Generates a completion text as generated\_text after getting
a text prompt as input and parameters for the selected model (model\_id).

Parameters:

- **params** ( _dict_) – MetaProps for text generation, use `ibm_watsonx_ai.metanames.GenTextParamsMetaNames().show()` to view the list of MetaNames

- **concurrency\_limit** ( _int_) – number of requests that will be sent in parallel, max is 10

- **prompt** ( _str_ _,_ _list_) – the prompt string or list of strings. If a list of strings is passed, requests will be managed in parallel with the rate of concurency\_limit

- **guardrails** ( _bool_) – if True, the detection filter for potentially hateful, abusive, and/or profane language (HAP)
is toggle on for both prompt and generated text, defaults to False

- **guardrails\_hap\_params** – MetaProps for HAP moderations, use `ibm_watsonx_ai.metanames.GenTextModerationsMetaNames().show()`
to view the list of MetaNames

- **async\_mode** ( _bool_) – if True, then yields results asynchronously using a generator. In this case, both prompt and
generated text will be concatenated in the final response - under generated\_text, defaults
to False


Returns:

scoring result that contains the generated content

Return type:

dict

**Example:**

```
q = "What is 1 + 1?"
generated_response = model.generate(prompt=q)
print(generated_response['results'][0]['generated_text'])

```

generate\_text( _prompt=None_, _params=None_, _raw\_response=False_, _guardrails=False_, _guardrails\_hap\_params=None_, _guardrails\_pii\_params=None_, _concurrency\_limit=8_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/model.html#Model.generate_text) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.Model.generate_text "Link to this definition")

Generates a completion text as generated\_text after getting
a text prompt as input and parameters for the selected model (model\_id).

Parameters:

- **params** ( _dict_) – MetaProps for text generation, use `ibm_watsonx_ai.metanames.GenTextParamsMetaNames().show()` to view the list of MetaNames

- **concurrency\_limit** ( _int_) – number of requests to be sent in parallel, max is 10

- **prompt** ( _str_ _,_ _list_) – the prompt string or list of strings. If a list of strings is passed, requests will be managed in parallel with the rate of concurency\_limit

- **raw\_response** ( _bool_ _,_ _optional_) – return the whole response object

- **guardrails** ( _bool_) – if True, the detection filter for potentially hateful, abusive, and/or profane language (HAP)
is toggle on for both prompt and generated text, defaults to False

- **guardrails\_hap\_params** – MetaProps for HAP moderations, use `ibm_watsonx_ai.metanames.GenTextModerationsMetaNames().show()`
to view the list of MetaNames


Returns:

generated content

Return type:

str or dict

**Example:**

```
q = "What is 1 + 1?"
generated_text = model.generate_text(prompt=q)
print(generated_text)

```

generate\_text\_stream( _prompt=None_, _params=None_, _raw\_response=False_, _guardrails=False_, _guardrails\_hap\_params=None_, _guardrails\_pii\_params=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/model.html#Model.generate_text_stream) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.Model.generate_text_stream "Link to this definition")

Generates a streamed text as generate\_text\_stream after getting
a text prompt as input and parameters for the selected model (model\_id).

Parameters:

- **params** ( _dict_) – MetaProps for text generation, use `ibm_watsonx_ai.metanames.GenTextParamsMetaNames().show()` to view the list of MetaNames

- **prompt** ( _str_ _,_) – the prompt string

- **raw\_response** ( _bool_ _,_ _optional_) – yields the whole response object

- **guardrails** ( _bool_) – If True, the detection filter for potentially hateful, abusive, and/or profane language (HAP)
is toggle on for both prompt and generated text, defaults to False

- **guardrails\_hap\_params** – MetaProps for HAP moderations, use `ibm_watsonx_ai.metanames.GenTextModerationsMetaNames().show()`
to view the list of MetaNames


Returns:

scoring result that contains the generated content

Return type:

generator

**Example:**

```
q = "Write an epigram about the sun"
generated_response = model.generate_text_stream(prompt=q)

for chunk in generated_response:
    print(chunk, end='', flush=True)

```

get\_details() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/model.html#Model.get_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.Model.get_details "Link to this definition")

Get the model’s details.

Returns:

model’s details

Return type:

dict

**Example:**

```
model.get_details()

```

to\_langchain() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/model.html#Model.to_langchain) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.Model.to_langchain "Link to this definition")Returns:

WatsonxLLM wrapper for watsonx foundation models

Return type:

WatsonxLLM

**Example:**

```
from langchain import PromptTemplate
from langchain.chains import LLMChain
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes

flan_ul2_model = Model(
    model_id=ModelTypes.FLAN_UL2,
    credentials=Credentials(
                api_key = IAM_API_KEY,
                url = "https://us-south.ml.cloud.ibm.com"),
    project_id="*****"
    )

prompt_template = "What color is the {flower}?"

llm_chain = LLMChain(llm=flan_ul2_model.to_langchain(), prompt=PromptTemplate.from_template(prompt_template))
llm_chain.invoke('sunflower')

```

tokenize( _prompt_, _return\_tokens=False_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/model.html#Model.tokenize) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.Model.tokenize "Link to this definition")

The text tokenize operation allows you to check the conversion of provided input to tokens for a given model.
It splits text into words or sub-words, which are are converted to IDs through a look-up table (vocabulary).
Tokenization allows the model to have a reasonable vocabulary size.

Parameters:

- **prompt** ( _str_) – prompt string

- **return\_tokens** ( _bool_) – parameter for text tokenization, defaults to False


Returns:

result of tokenizing the input string

Return type:

dict

**Example:**

```
q = "Write an epigram about the moon"
tokenized_response = model.tokenize(prompt=q, return_tokens=True)
print(tokenized_response["result"])

```

## Enums [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html\#enums "Link to this heading")

_class_ metanames.GenTextParamsMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#GenTextParamsMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#metanames.GenTextParamsMetaNames "Link to this definition")

Set of MetaNames for Foundation Model Parameters.

Available MetaNames:

|     |     |     |     |
| --- | --- | --- | --- |
| MetaName | Type | Required | Example value |
| DECODING\_METHOD | str | N | `sample` |
| LENGTH\_PENALTY | dict | N | `{'decay_factor': 2.5, 'start_index': 5}` |
| TEMPERATURE | float | N | `0.5` |
| TOP\_P | float | N | `0.2` |
| TOP\_K | int | N | `1` |
| RANDOM\_SEED | int | N | `33` |
| REPETITION\_PENALTY | float | N | `2` |
| MIN\_NEW\_TOKENS | int | N | `50` |
| MAX\_NEW\_TOKENS | int | N | `200` |
| STOP\_SEQUENCES | list | N | `['fail']` |
| TIME\_LIMIT | int | N | `600000` |
| TRUNCATE\_INPUT\_TOKENS | int | N | `200` |
| PROMPT\_VARIABLES | dict | N | `{'object': 'brain'}` |
| RETURN\_OPTIONS | dict | N | `{'input_text': True, 'generated_tokens': True, 'input_tokens': True, 'token_logprobs': True, 'token_ranks': False, 'top_n_tokens': False}` |

_class_ metanames.GenTextReturnOptMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#GenTextReturnOptMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#metanames.GenTextReturnOptMetaNames "Link to this definition")

Set of MetaNames for Foundation Model Parameters.

Available MetaNames:

|     |     |     |     |
| --- | --- | --- | --- |
| MetaName | Type | Required | Example value |
| INPUT\_TEXT | bool | Y | `True` |
| GENERATED\_TOKENS | bool | N | `True` |
| INPUT\_TOKENS | bool | Y | `True` |
| TOKEN\_LOGPROBS | bool | N | `True` |
| TOKEN\_RANKS | bool | N | `True` |
| TOP\_N\_TOKENS | int | N | `True` |

Note

One of these parameters is required: \[‘INPUT\_TEXT’, ‘INPUT\_TOKENS’\]

_class_ ibm\_watsonx\_ai.foundation\_models.utils.enums.DecodingMethods( _value_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/utils/enums.html#DecodingMethods) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.utils.enums.DecodingMethods "Link to this definition")

Bases: `Enum`

Supported decoding methods for text generation.

GREEDY _='greedy'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.utils.enums.DecodingMethods.GREEDY "Link to this definition")SAMPLE _='sample'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.utils.enums.DecodingMethods.SAMPLE "Link to this definition")_class_ ibm\_watsonx\_ai.foundation\_models.utils.enums.ModelTypes( _value_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/utils/enums.html#ModelTypes) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.utils.enums.ModelTypes "Link to this definition")

Bases: `StrEnum`

Deprecated since version 1.0.5: Use [`TextModels()`](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#TextModels "TextModels") instead.

Supported foundation models.

Note

You can check the current list of supported models types of various environments with
[`get_model_specs()`](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html#ibm_watsonx_ai.foundation_models_manager.FoundationModelsManager.get_model_specs "ibm_watsonx_ai.foundation_models_manager.FoundationModelsManager.get_model_specs") or
by referring to the [watsonx.ai](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-models.html?context=wx)
documentation.