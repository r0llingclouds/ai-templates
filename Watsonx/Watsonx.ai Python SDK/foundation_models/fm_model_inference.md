ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#furo-main-content)

[Back to top](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#)

[View this page](https://ibm.github.io/watsonx-ai-python-sdk/_sources/fm_model_inference.rst.txt "View this page")

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ModelInference [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html\#modelinference "Link to this heading")

_class_ ibm\_watsonx\_ai.foundation\_models.inference.ModelInference( _\*_, _model\_id=None_, _deployment\_id=None_, _params=None_, _credentials=None_, _project\_id=None_, _space\_id=None_, _verify=None_, _api\_client=None_, _validate=True_, _persistent\_connection=True_, _max\_retries=None_, _delay\_time=None_, _retry\_status\_codes=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/inference/model_inference.html#ModelInference) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#ibm_watsonx_ai.foundation_models.inference.ModelInference "Link to this definition")

Bases: `BaseModelInference`

Instantiate the model interface.

Hint

To use the ModelInference class with LangChain, use the `WatsonxLLM` wrapper.

Parameters:

- **model\_id** ( _str_ _,_ _optional_) – type of model to use

- **deployment\_id** ( _str_ _,_ _optional_) – ID of tuned model’s deployment

- **credentials** ( [_Credentials_](https://ibm.github.io/watsonx-ai-python-sdk/base.html#credentials.Credentials "credentials.Credentials") _or_ _dict_ _,_ _optional_) – credentials for the Watson Machine Learning instance

- **params** ( _dict_ _,_ [_TextGenParameters_](https://ibm.github.io/watsonx-ai-python-sdk/fm_schema.html#ibm_watsonx_ai.foundation_models.schema.TextGenParameters "ibm_watsonx_ai.foundation_models.schema.TextGenParameters") _,_ [_TextChatParameters_](https://ibm.github.io/watsonx-ai-python-sdk/fm_schema.html#ibm_watsonx_ai.foundation_models.schema.TextChatParameters "ibm_watsonx_ai.foundation_models.schema.TextChatParameters") _,_ _optional_) – parameters to use during request generation

- **project\_id** ( _str_ _,_ _optional_) – ID of the Watson Studio project

- **space\_id** ( _str_ _,_ _optional_) – ID of the Watson Studio space

- **verify** ( _bool_ _or_ _str_ _,_ _optional_) –

You can pass one of the following as verify:


  - the path to a CA\_BUNDLE file

  - the path of directory with certificates of trusted CAs

  - True \- default path to truststore will be taken

  - False \- no verification will be made


- **api\_client** ( [_APIClient_](https://ibm.github.io/watsonx-ai-python-sdk/base.html#client.APIClient "client.APIClient") _,_ _optional_) – initialized APIClient object with a set project ID or space ID. If passed, `credentials` and `project_id`/ `space_id` are not required.

- **validate** ( _bool_ _,_ _optional_) – Model ID validation, defaults to True

- **persistent\_connection** ( _bool_ _,_ _optional_) – Whether to keep persistent connection when evaluating generate, generate\_text or tokenize methods.
This parameter is only applicable for the mentioned methods when the prompt is a str type.
To close the connection, run model.close\_persistent\_connection(), defaults to True. Added in 1.1.2.

- **max\_retries** ( _int_ _,_ _optional_) – number of retries performed when request was not successful and status code is in retry\_status\_codes, defaults to 10

- **delay\_time** ( _float_ _,_ _optional_) – delay time to retry request, factor in exponential backoff formula: wx\_delay\_time \* pow(2.0, attempt), defaults to 0.5s

- **retry\_status\_codes** ( _list_ _\[_ _int_ _\]_ _,_ _optional_) – list of status codes which will be considered for retry mechanism, defaults to \[429, 503, 504, 520\]


Note

- You must provide one of these parameters: \[ `model_id`, `deployment_id`\]

- When the `credentials` parameter is passed, you must provide one of these parameters: \[ `project_id`, `space_id`\].


Hint

You can copy the project\_id from the Project’s Manage tab (Project -> Manage -> General -> Details).

**Example:**

```
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes, DecodingMethods

# To display example params enter
GenParams().get_example_values()

generate_params = {
    GenParams.MAX_NEW_TOKENS: 25
}

model_inference = ModelInference(
    model_id=ModelTypes.FLAN_UL2,
    params=generate_params,
    credentials=Credentials(
        api_key = IAM_API_KEY,
        url = "https://us-south.ml.cloud.ibm.com"),
    project_id="*****"
    )

```

```
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import Credentials

deployment_inference = ModelInference(
    deployment_id="<ID of deployed model>",
    credentials=Credentials(
        api_key = IAM_API_KEY,
        url = "https://us-south.ml.cloud.ibm.com"),
    project_id="*****"
    )

```

_async_ achat( _messages_, _params=None_, _tools=None_, _tool\_choice=None_, _tool\_choice\_option=None_, _context=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/inference/model_inference.html#ModelInference.achat) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#ibm_watsonx_ai.foundation_models.inference.ModelInference.achat "Link to this definition")

Given a list of messages comprising a conversation with a chat model in an asynchronous manner.

Parameters:

- **messages** ( _list_ _\[_ _dict_ _\]_) – The messages for this chat session.

- **params** ( _dict_ _,_ [_TextChatParameters_](https://ibm.github.io/watsonx-ai-python-sdk/fm_schema.html#ibm_watsonx_ai.foundation_models.schema.TextChatParameters "ibm_watsonx_ai.foundation_models.schema.TextChatParameters") _,_ _optional_) – meta props for chat generation, use `ibm_watsonx_ai.foundation_models.schema.TextChatParameters.show()`

- **tools** ( _list_) – Tool functions that can be called with the response.

- **tool\_choice** ( _dict_ _,_ _optional_) – Specifying a particular tool via {“type”: “function”, “function”: {“name”: “my\_function”}} forces the model to call that tool.

- **tool\_choice\_option** ( _Literal_ _\[_ _"none"_ _,_ _"auto"_ _\]_ _,_ _optional_) – Tool choice option

- **context** ( _str_ _,_ _optional_) – context variable can be present in chat system\_prompt or chat messages content fields and are
identified by sentence ‘{{ context }}’. Supported only with deployment\_id, defaults to None.


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
generated_response = await model.achat(messages=messages)

# Print all response
print(generated_response)

# Print only content
print(generated_response['choices'][0]['message']['content'])

```

_async_ achat\_stream( _messages_, _params=None_, _tools=None_, _tool\_choice=None_, _tool\_choice\_option=None_, _context=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/inference/model_inference.html#ModelInference.achat_stream) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#ibm_watsonx_ai.foundation_models.inference.ModelInference.achat_stream "Link to this definition")

Given a list of messages comprising a conversation, the model will return a response in stream in an asynchronous manner.

Parameters:

- **messages** ( _list_ _\[_ _dict_ _\]_) – The messages for this chat session.

- **params** ( _dict_ _,_ [_TextChatParameters_](https://ibm.github.io/watsonx-ai-python-sdk/fm_schema.html#ibm_watsonx_ai.foundation_models.schema.TextChatParameters "ibm_watsonx_ai.foundation_models.schema.TextChatParameters") _,_ _optional_) – meta props for chat generation, use `ibm_watsonx_ai.foundation_models.schema.TextChatParameters.show()`

- **tools** ( _list_) – Tool functions that can be called with the response.

- **tool\_choice** ( _dict_ _,_ _optional_) – Specifying a particular tool via {“type”: “function”, “function”: {“name”: “my\_function”}} forces the model to call that tool.

- **tool\_choice\_option** ( _Literal_ _\[_ _"none"_ _,_ _"auto"_ _\]_ _,_ _optional_) – Tool choice option

- **context** ( _str_ _,_ _optional_) – context variable can be present in chat system\_prompt or chat messages content fields and are
identified by sentence ‘{{ context }}’. Supported only with deployment\_id, defaults to None.


Returns:

scoring result containing generated chat content.

Return type:

AsyncGenerator

**Example:**

```
messages = [\
    {"role": "system", "content": "You are a helpful assistant."},\
    {"role": "user", "content": "Who won the world series in 2020?"}\
]
generated_response = await model.achat_stream(messages=messages)

async for chunk in generated_response:
    if chunk['choices']:
        print(chunk['choices'][0]['delta'].get('content', ''), end='', flush=True)

```

_async_ aclose\_persistent\_connection() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/inference/model_inference.html#ModelInference.aclose_persistent_connection) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#ibm_watsonx_ai.foundation_models.inference.ModelInference.aclose_persistent_connection "Link to this definition")

Only applicable if persistent\_connection was set to True in the ModelInference initialization.

_async_ agenerate( _prompt=None_, _params=None_, _guardrails=False_, _guardrails\_hap\_params=None_, _guardrails\_pii\_params=None_, _validate\_prompt\_variables=True_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/inference/model_inference.html#ModelInference.agenerate) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#ibm_watsonx_ai.foundation_models.inference.ModelInference.agenerate "Link to this definition")

Generate a response in an asynchronous manner.

Parameters:

- **prompt** ( _str_ _\|_ _None_ _,_ _optional_) – prompt string, defaults to None

- **params** ( _dict_ _\|_ _None_ _,_ _optional_) – MetaProps for text generation, use `ibm_watsonx_ai.metanames.GenTextParamsMetaNames().show()` to view the list of MetaNames, defaults to None

- **guardrails** ( _bool_ _,_ _optional_) – If True, the detection filter for potentially hateful, abusive, and/or profane language (HAP) is toggle on for both prompt and generated text, defaults to False
If HAP is detected, then the HAPDetectionWarning is issued

- **guardrails\_hap\_params** ( _dict_ _\|_ _None_ _,_ _optional_) – MetaProps for HAP moderations, use `ibm_watsonx_ai.metanames.GenTextModerationsMetaNames().show()`
to view the list of MetaNames

- **validate\_prompt\_variables** ( _bool_ _,_ _optional_) – If True, the prompt variables provided in params are validated with the ones in the Prompt Template Asset.
This parameter is only applicable in a Prompt Template Asset deployment scenario and should not be changed for different cases, defaults to True


Returns:

raw response that contains the generated content

Return type:

dict

_async_ agenerate\_stream( _prompt=None_, _params=None_, _guardrails=False_, _guardrails\_hap\_params=None_, _guardrails\_pii\_params=None_, _validate\_prompt\_variables=True_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/inference/model_inference.html#ModelInference.agenerate_stream) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#ibm_watsonx_ai.foundation_models.inference.ModelInference.agenerate_stream "Link to this definition")

Generates a stream as agenerate\_stream after getting a text prompt as input and
parameters for the selected model (model\_id). For prompt template deployment, prompt should be None.

Parameters:

- **params** ( _dict_ _,_ [_TextGenParameters_](https://ibm.github.io/watsonx-ai-python-sdk/fm_schema.html#ibm_watsonx_ai.foundation_models.schema.TextGenParameters "ibm_watsonx_ai.foundation_models.schema.TextGenParameters") _,_ _optional_) – MetaProps for text generation, use `ibm_watsonx_ai.metanames.GenTextParamsMetaNames().show()` to view the list of MetaNames

- **prompt** ( _str_ _,_ _optional_) – prompt string, defaults to None

- **guardrails** ( _bool_) – If True, the detection filter for potentially hateful, abusive, and/or profane language (HAP) is toggle on for both prompt and generated text, defaults to False
If HAP is detected, then the HAPDetectionWarning is issued

- **guardrails\_hap\_params** ( _dict_) – MetaProps for HAP moderations, use `ibm_watsonx_ai.metanames.GenTextModerationsMetaNames().show()`
to view the list of MetaNames

- **validate\_prompt\_variables** ( _bool_) – If True, the prompt variables provided in params are validated with the ones in the Prompt Template Asset.
This parameter is only applicable in a Prompt Template Asset deployment scenario and should not be changed for different cases, defaults to True


Returns:

scoring result that contains the generated content

Return type:

AsyncGenerator

Note

By default, only the first occurrence of HAPDetectionWarning is displayed. To enable printing all warnings of this category, use:

```
import warnings
from ibm_watsonx_ai.foundation_models.utils import HAPDetectionWarning

warnings.filterwarnings("always", category=HAPDetectionWarning)

```

**Example:**

```
q = "Write an epigram about the sun"
generated_response = await model_inference.agenerate_stream(prompt=q)

async for chunk in generated_response:
    print(chunk, end='', flush=True)

```

chat( _messages_, _params=None_, _tools=None_, _tool\_choice=None_, _tool\_choice\_option=None_, _context=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/inference/model_inference.html#ModelInference.chat) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#ibm_watsonx_ai.foundation_models.inference.ModelInference.chat "Link to this definition")

Given a list of messages comprising a conversation, the model will return a response.

Parameters:

- **messages** ( _list_ _\[_ _dict_ _\]_) – The messages for this chat session.

- **params** ( _dict_ _,_ [_TextChatParameters_](https://ibm.github.io/watsonx-ai-python-sdk/fm_schema.html#ibm_watsonx_ai.foundation_models.schema.TextChatParameters "ibm_watsonx_ai.foundation_models.schema.TextChatParameters") _,_ _optional_) – meta props for chat generation, use `ibm_watsonx_ai.foundation_models.schema.TextChatParameters.show()`

- **tools** ( _list_) – Tool functions that can be called with the response.

- **tool\_choice** ( _dict_ _,_ _optional_) – Specifying a particular tool via {“type”: “function”, “function”: {“name”: “my\_function”}} forces the model to call that tool.

- **tool\_choice\_option** ( _Literal_ _\[_ _"none"_ _,_ _"auto"_ _\]_ _,_ _optional_) – Tool choice option

- **context** ( _str_ _,_ _optional_) – context variable can be present in chat system\_prompt or chat messages content fields and are
identified by sentence ‘{{ context }}’. Supported only with deployment\_id, defaults to None.


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
print(generated_response['choices'][0]['message']['content'])

```

chat\_stream( _messages_, _params=None_, _tools=None_, _tool\_choice=None_, _tool\_choice\_option=None_, _context=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/inference/model_inference.html#ModelInference.chat_stream) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#ibm_watsonx_ai.foundation_models.inference.ModelInference.chat_stream "Link to this definition")

Given a list of messages comprising a conversation, the model will return a response in stream.

Parameters:

- **messages** ( _list_ _\[_ _dict_ _\]_) – The messages for this chat session.

- **params** ( _dict_ _,_ [_TextChatParameters_](https://ibm.github.io/watsonx-ai-python-sdk/fm_schema.html#ibm_watsonx_ai.foundation_models.schema.TextChatParameters "ibm_watsonx_ai.foundation_models.schema.TextChatParameters") _,_ _optional_) – meta props for chat generation, use `ibm_watsonx_ai.foundation_models.schema.TextChatParameters.show()`

- **tools** ( _list_) – Tool functions that can be called with the response.

- **tool\_choice** ( _dict_ _,_ _optional_) – Specifying a particular tool via {“type”: “function”, “function”: {“name”: “my\_function”}} forces the model to call that tool.

- **tool\_choice\_option** ( _Literal_ _\[_ _"none"_ _,_ _"auto"_ _\]_ _,_ _optional_) – Tool choice option

- **context** ( _str_ _,_ _optional_) – context variable can be present in chat system\_prompt or chat messages content fields and are
identified by sentence ‘{{ context }}’. Supported only with deployment\_id, defaults to None.


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
    if chunk['choices']:
        print(chunk['choices'][0]['delta'].get('content', ''), end='', flush=True)

```

close\_persistent\_connection() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/inference/model_inference.html#ModelInference.close_persistent_connection) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#ibm_watsonx_ai.foundation_models.inference.ModelInference.close_persistent_connection "Link to this definition")

Only applicable if persistent\_connection was set to True in ModelInference initialization.
Calling this method closes the current httpx.Client and recreates a new httpx.Client with default values:
timeout: httpx.Timeout(timeout=30 \* 60, connect=10)
limit: httpx.Limits(max\_connections=10, max\_keepalive\_connections=10, keepalive\_expiry=HTTPX\_KEEPALIVE\_EXPIRY)

generate( _prompt=None_, _params=None_, _guardrails=False_, _guardrails\_hap\_params=None_, _guardrails\_pii\_params=None_, _concurrency\_limit=8_, _async\_mode=False_, _validate\_prompt\_variables=True_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/inference/model_inference.html#ModelInference.generate) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#ibm_watsonx_ai.foundation_models.inference.ModelInference.generate "Link to this definition")

Generates a completion text as generated\_text after getting a text prompt as input and parameters for the
selected model (model\_id) or deployment (deployment\_id). For prompt template deployment, prompt should be None.

Parameters:

- **params** ( _dict_ _,_ [_TextGenParameters_](https://ibm.github.io/watsonx-ai-python-sdk/fm_schema.html#ibm_watsonx_ai.foundation_models.schema.TextGenParameters "ibm_watsonx_ai.foundation_models.schema.TextGenParameters") _,_ _optional_) – MetaProps for text generation, use `ibm_watsonx_ai.metanames.GenTextParamsMetaNames().show()` to view the list of MetaNames

- **concurrency\_limit** ( _int_) – number of requests to be sent in parallel, max is 10

- **prompt** ( _(_ _str_ _\|_ _list_ _\|_ _None_ _)_ _,_ _optional_) – prompt string or list of strings. If list of strings is passed, requests will be managed in parallel with the rate of concurency\_limit, defaults to None

- **guardrails** ( _bool_) – If True, the detection filter for potentially hateful, abusive, and/or profane language (HAP)
is toggle on for both prompt and generated text, defaults to False

- **guardrails\_hap\_params** ( _dict_) – MetaProps for HAP moderations, use `ibm_watsonx_ai.metanames.GenTextModerationsMetaNames().show()`
to view the list of MetaNames

- **async\_mode** ( _bool_) – If True, yields results asynchronously (using a generator). In this case, both prompt and
generated text will be concatenated in the final response - under generated\_text, defaults
to False

- **validate\_prompt\_variables** ( _bool_ _,_ _optional_) – If True and ModelInference instance has been initialized with validate=True, prompt variables provided in params are validated with the ones in the Prompt Template Asset.
This parameter is only applicable in a Prompt Template Asset deployment scenario and should not be changed for different cases, defaults to True


Returns:

scoring result the contains the generated content

Return type:

dict

**Example:**

```
q = "What is 1 + 1?"
generated_response = model_inference.generate(prompt=q)
print(generated_response['results'][0]['generated_text'])

```

generate\_text( _prompt=None_, _params=None_, _raw\_response=False_, _guardrails=False_, _guardrails\_hap\_params=None_, _guardrails\_pii\_params=None_, _concurrency\_limit=8_, _validate\_prompt\_variables=True_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/inference/model_inference.html#ModelInference.generate_text) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#ibm_watsonx_ai.foundation_models.inference.ModelInference.generate_text "Link to this definition")

Generates a completion text as generated\_text after getting a text prompt as input and
parameters for the selected model (model\_id). For prompt template deployment, prompt should be None.

Parameters:

- **params** ( _dict_ _,_ [_TextGenParameters_](https://ibm.github.io/watsonx-ai-python-sdk/fm_schema.html#ibm_watsonx_ai.foundation_models.schema.TextGenParameters "ibm_watsonx_ai.foundation_models.schema.TextGenParameters") _,_ _optional_) – MetaProps for text generation, use `ibm_watsonx_ai.metanames.GenTextParamsMetaNames().show()` to view the list of MetaNames

- **concurrency\_limit** ( _int_) – number of requests to be sent in parallel, max is 10

- **prompt** ( _(_ _str_ _\|_ _list_ _\|_ _None_ _)_ _,_ _optional_) – prompt string or list of strings. If list of strings is passed, requests will be managed in parallel with the rate of concurency\_limit, defaults to None

- **guardrails** ( _bool_) – If True, the detection filter for potentially hateful, abusive, and/or profane language (HAP) is toggle on for both prompt and generated text, defaults to False
If HAP is detected, then the HAPDetectionWarning is issued

- **guardrails\_hap\_params** ( _dict_) – MetaProps for HAP moderations, use `ibm_watsonx_ai.metanames.GenTextModerationsMetaNames().show()`
to view the list of MetaNames

- **raw\_response** ( _bool_ _,_ _optional_) – returns the whole response object

- **validate\_prompt\_variables** ( _bool_) – If True, the prompt variables provided in params are validated with the ones in the Prompt Template Asset.
This parameter is only applicable in a Prompt Template Asset deployment scenario and should not be changed for different cases, defaults to True


Returns:

generated content

Return type:

str \| list \| dict

Note

By default, only the first occurrence of HAPDetectionWarning is displayed. To enable printing all warnings of this category, use:

```
import warnings
from ibm_watsonx_ai.foundation_models.utils import HAPDetectionWarning

warnings.filterwarnings("always", category=HAPDetectionWarning)

```

**Example:**

```
q = "What is 1 + 1?"
generated_text = model_inference.generate_text(prompt=q)
print(generated_text)

```

generate\_text\_stream( _prompt=None_, _params=None_, _raw\_response=False_, _guardrails=False_, _guardrails\_hap\_params=None_, _guardrails\_pii\_params=None_, _validate\_prompt\_variables=True_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/inference/model_inference.html#ModelInference.generate_text_stream) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#ibm_watsonx_ai.foundation_models.inference.ModelInference.generate_text_stream "Link to this definition")

Generates a streamed text as generate\_text\_stream after getting a text prompt as input and
parameters for the selected model (model\_id). For prompt template deployment, prompt should be None.

Parameters:

- **params** ( _dict_ _,_ [_TextGenParameters_](https://ibm.github.io/watsonx-ai-python-sdk/fm_schema.html#ibm_watsonx_ai.foundation_models.schema.TextGenParameters "ibm_watsonx_ai.foundation_models.schema.TextGenParameters") _,_ _optional_) – MetaProps for text generation, use `ibm_watsonx_ai.metanames.GenTextParamsMetaNames().show()` to view the list of MetaNames

- **prompt** ( _str_ _,_ _optional_) – prompt string, defaults to None

- **raw\_response** ( _bool_ _,_ _optional_) – yields the whole response object

- **guardrails** ( _bool_) – If True, the detection filter for potentially hateful, abusive, and/or profane language (HAP) is toggle on for both prompt and generated text, defaults to False
If HAP is detected, then the HAPDetectionWarning is issued

- **guardrails\_hap\_params** ( _dict_) – MetaProps for HAP moderations, use `ibm_watsonx_ai.metanames.GenTextModerationsMetaNames().show()`
to view the list of MetaNames

- **validate\_prompt\_variables** ( _bool_) – If True, the prompt variables provided in params are validated with the ones in the Prompt Template Asset.
This parameter is only applicable in a Prompt Template Asset deployment scenario and should not be changed for different cases, defaults to True


Returns:

scoring result that contains the generated content

Return type:

generator

Note

By default, only the first occurrence of HAPDetectionWarning is displayed. To enable printing all warnings of this category, use:

```
import warnings
from ibm_watsonx_ai.foundation_models.utils import HAPDetectionWarning

warnings.filterwarnings("always", category=HAPDetectionWarning)

```

**Example:**

```
q = "Write an epigram about the sun"
generated_response = model_inference.generate_text_stream(prompt=q)

for chunk in generated_response:
    print(chunk, end='', flush=True)

```

get\_details() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/inference/model_inference.html#ModelInference.get_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#ibm_watsonx_ai.foundation_models.inference.ModelInference.get_details "Link to this definition")

Get the details of a model interface

Returns:

details of the model or deployment

Return type:

dict

**Example:**

```
model_inference.get_details()

```

get\_identifying\_params() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/inference/model_inference.html#ModelInference.get_identifying_params) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#ibm_watsonx_ai.foundation_models.inference.ModelInference.get_identifying_params "Link to this definition")

Represent Model Inference’s setup in dictionary

set\_api\_client( _api\_client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/inference/model_inference.html#ModelInference.set_api_client) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#ibm_watsonx_ai.foundation_models.inference.ModelInference.set_api_client "Link to this definition")

Set or refresh the APIClient object associated with ModelInference object.

Parameters:

**api\_client** ( [_APIClient_](https://ibm.github.io/watsonx-ai-python-sdk/base.html#client.APIClient "client.APIClient") _,_ _optional_) – initialized APIClient object with a set project ID or space ID.

**Example:**

```
api_client = APIClient(credentials=..., space_id=...)
model_inference.set_api_client(api_client=api_client)

```

to\_langchain() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/inference/model_inference.html#ModelInference.to_langchain) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#ibm_watsonx_ai.foundation_models.inference.ModelInference.to_langchain "Link to this definition")Returns:

WatsonxLLM wrapper for watsonx foundation models

Return type:

WatsonxLLM

**Example:**

```
from langchain import PromptTemplate
from langchain.chains import LLMChain
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes

flan_ul2_model = ModelInference(
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

```
from langchain import PromptTemplate
from langchain.chains import LLMChain
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes

deployed_model = ModelInference(
    deployment_id="<ID of deployed model>",
    credentials=Credentials(
                        api_key = IAM_API_KEY,
                        url = "https://us-south.ml.cloud.ibm.com"),
    space_id="*****"
    )

prompt_template = "What color is the {car}?"

llm_chain = LLMChain(llm=deployed_model.to_langchain(), prompt=PromptTemplate.from_template(prompt_template))
llm_chain.invoke('sunflower')

```

tokenize( _prompt_, _return\_tokens=False_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/inference/model_inference.html#ModelInference.tokenize) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#ibm_watsonx_ai.foundation_models.inference.ModelInference.tokenize "Link to this definition")

The text tokenize operation allows you to check the conversion of provided input to tokens for a given model.
It splits text into words or sub-words, which then are converted to IDs through a look-up table (vocabulary).
Tokenization allows the model to have a reasonable vocabulary size.

Note

The tokenization method is available only for base models and is not supported for deployments.

Parameters:

- **prompt** ( _str_ _,_ _optional_) – prompt string, defaults to None

- **return\_tokens** ( _bool_) – parameter for text tokenization, defaults to False


Returns:

result of tokenizing the input string

Return type:

dict

**Example:**

```
q = "Write an epigram about the moon"
tokenized_response = model_inference.tokenize(prompt=q, return_tokens=True)
print(tokenized_response["result"])

```

## Enums [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html\#enums "Link to this heading")

_class_ TextModels [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#TextModels "Link to this definition")

Bases: `StrEnum`

This represents a dynamically generated Enum for Foundation Models.

**Example of getting TextModels:**

```
# GET TextModels ENUM
client.foundation_models.TextModels

# PRINT dict of Enums
client.foundation_models.TextModels.show()

```

**Example Output:**

```
{'GRANITE_13B_CHAT_V2': 'ibm/granite-13b-chat-v2',
'GRANITE_13B_INSTRUCT_V2': 'ibm/granite-13b-instruct-v2',
...
'LLAMA_2_13B_CHAT': 'meta-llama/llama-2-13b-chat',
'LLAMA_2_70B_CHAT': 'meta-llama/llama-2-70b-chat',
'LLAMA_3_70B_INSTRUCT': 'meta-llama/llama-3-70b-instruct',
'MIXTRAL_8X7B_INSTRUCT_V01': 'mistralai/mixtral-8x7b-instruct-v01'}

```

**Example of initialising ModelInference with TextModels Enum:**

```
from ibm_watsonx_ai.foundation_models import ModelInference

model = ModelInference(
    model_id=client.foundation_models.TextModels.GRANITE_13B_INSTRUCT_V2,
    credentials=Credentials(...),
    project_id=project_id,
)

```

_class_ ChatModels [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#ChatModels "Link to this definition")

Bases: `StrEnum`

This represents a dynamically generated Enum for Chat Models.

**Example of getting ChatModels:**

```
# GET ChatModels ENUM
client.foundation_models.ChatModels

# PRINT dict of Enums
client.foundation_models.ChatModels.show()

```

**Example Output:**

```
{'GRANITE_20B_CODE_INSTRUCT': 'ibm/granite-20b-code-instruct',
'GRANITE_3_8B_INSTRUCT': 'ibm/granite-3-8b-instruct',
...
'LLAMA_3_3_70B_INSTRUCT': 'meta-llama/llama-3-3-70b-instruct',
'LLAMA_3_405B_INSTRUCT': 'meta-llama/llama-3-405b-instruct',
'MISTRAL_LARGE': 'mistralai/mistral-large',
'MIXTRAL_8X7B_INSTRUCT_V01': 'mistralai/mixtral-8x7b-instruct-v01'}

```

**Example of initialising ModelInference with ChatModels Enum:**

```
from ibm_watsonx_ai.foundation_models import ModelInference

model = ModelInference(
    model_id=client.foundation_models.ChatModels.GRANITE_3_8B_INSTRUCT,
    credentials=Credentials(...),
    project_id=project_id,
)

```