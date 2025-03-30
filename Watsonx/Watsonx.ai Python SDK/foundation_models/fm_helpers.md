ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html#furo-main-content)

[Back to top](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html#)

[View this page](https://ibm.github.io/watsonx-ai-python-sdk/_sources/fm_helpers.rst.txt "View this page")

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Helpers [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html\#helpers "Link to this heading")

_class_ ibm\_watsonx\_ai.foundation\_models\_manager.FoundationModelsManager( _client_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models_manager.html#FoundationModelsManager) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html#ibm_watsonx_ai.foundation_models_manager.FoundationModelsManager "Link to this definition")get\_base\_foundation\_model\_deployable\_specs( _model\_id=None_, _limit=None_, _asynchronous=False_, _get\_all=False_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models_manager.html#FoundationModelsManager.get_base_foundation_model_deployable_specs) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html#ibm_watsonx_ai.foundation_models_manager.FoundationModelsManager.get_base_foundation_model_deployable_specs "Link to this definition")

Retrieve the specifications of a base deployable foundation models

Parameters:

- **model\_id** ( _str_ _,_ _optional_) – ID of the model, defaults to None (all models specifications are returned)

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, will get all entries in ‘limited’ chunks


Returns:

specifications of the base foundation model deployable

Return type:

dict or generator

**Example:**

```
client.foundation_models.get_base_foundation_model_deployable_specs()
client.foundation_models.get_base_foundation_model_deployable_specs('meta-llama/llama-3-1-8b')

```

get\_chat\_function\_calling\_model\_specs( _model\_id=None_, _limit=None_, _asynchronous=False_, _get\_all=False_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models_manager.html#FoundationModelsManager.get_chat_function_calling_model_specs) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html#ibm_watsonx_ai.foundation_models_manager.FoundationModelsManager.get_chat_function_calling_model_specs "Link to this definition")

Operations to retrieve the list of chat foundation models specifications with function calling support .

Parameters:

- **model\_id** ( _str_ _or_ [_ModelTypes_](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.utils.enums.ModelTypes "ibm_watsonx_ai.foundation_models.utils.enums.ModelTypes") _,_ _optional_) – Id of the model, defaults to None (all models specs are returned).

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, it will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, it will get all entries in ‘limited’ chunks


Returns:

list of deployed foundation model specs

Return type:

dict or generator

**Example**

```
# GET CHAT FUNCTION CALLING MODEL SPECS
client.foundation_models.get_chat_function_calling_model_specs()

# GET CHAT FUNCTION CALLING MODEL SPECS BY MODEL_ID
client.foundation_models.get_chat_function_calling_model_specs(model_id="meta-llama/llama-3-1-70b-instruct")

```

get\_chat\_model\_specs( _model\_id=None_, _limit=None_, _asynchronous=False_, _get\_all=False_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models_manager.html#FoundationModelsManager.get_chat_model_specs) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html#ibm_watsonx_ai.foundation_models_manager.FoundationModelsManager.get_chat_model_specs "Link to this definition")

Operations to retrieve the list of chat foundation models specifications.

Parameters:

- **model\_id** ( _str_ _or_ [_ModelTypes_](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.utils.enums.ModelTypes "ibm_watsonx_ai.foundation_models.utils.enums.ModelTypes") _,_ _optional_) – Id of the model, defaults to None (all models specs are returned).

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, it will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, it will get all entries in ‘limited’ chunks


Returns:

list of deployed foundation model specs

Return type:

dict or generator

**Example**

```
# GET CHAT MODEL SPECS
client.foundation_models.get_chat_model_specs()

# GET CHAT MODEL SPECS BY MODEL_ID
client.foundation_models.get_chat_model_specs(model_id="ibm/granite-13b-chat-v2")

```

get\_custom\_model\_specs( _model\_id=None_, _limit=None_, _asynchronous=False_, _get\_all=False_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models_manager.html#FoundationModelsManager.get_custom_model_specs) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html#ibm_watsonx_ai.foundation_models_manager.FoundationModelsManager.get_custom_model_specs "Link to this definition")

Get details on available custom model(s) as a dictionary or as a generator ( `asynchronous`).
If `asynchronous` or `get_all` is set, then `model_id` is ignored.

Parameters:

- **model\_id** ( _str_ _,_ _optional_) – ID of the model, defaults to None (all models specifications are returned)

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, will get all entries in ‘limited’ chunks


Returns:

details of supported custom models, None if no supported custom models are found for the given model\_id

Return type:

dict or generator

**Example:**

```
client.foundation_models.get_custom_models_spec()
client.foundation_models.get_custom_models_spec()
client.foundation_models.get_custom_models_spec(model_id='mistralai/Mistral-7B-Instruct-v0.2')
client.foundation_models.get_custom_models_spec(limit=20)
client.foundation_models.get_custom_models_spec(limit=20, get_all=True)
for spec in client.foundation_models.get_custom_model_specs(limit=20, asynchronous=True, get_all=True):
    print(spec, end="")

```

get\_embeddings\_model\_specs( _model\_id=None_, _limit=None_, _asynchronous=False_, _get\_all=False_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models_manager.html#FoundationModelsManager.get_embeddings_model_specs) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html#ibm_watsonx_ai.foundation_models_manager.FoundationModelsManager.get_embeddings_model_specs "Link to this definition")

Retrieves the specifications of an embeddings model.

Parameters:

- **model\_id** ( _str_ _,_ _optional_) – ID of the model, defaults to None (all models specifications are returned)

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, will get all entries in ‘limited’ chunks


Returns:

specifications of the embeddings model

Return type:

dict or generator

**Example:**

```
client.foundation_models.get_embeddings_model_specs()
client.foundation_models.get_embeddings_model_specs('ibm/slate-125m-english-rtrvr')

```

get\_model\_lifecycle( _model\_id_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models_manager.html#FoundationModelsManager.get_model_lifecycle) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html#ibm_watsonx_ai.foundation_models_manager.FoundationModelsManager.get_model_lifecycle "Link to this definition")

Retrieves a list of lifecycle data of a foundation model.

Parameters:

**model\_id** ( _str_) – ID of the model

Returns:

list of lifecycle data of a foundation model

Return type:

list

**Example:**

```
client.foundation_models.get_model_lifecycle(
    model_id="ibm/granite-13b-instruct-v2"
    )

```

get\_model\_specs( _model\_id=None_, _limit=None_, _asynchronous=False_, _get\_all=False_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models_manager.html#FoundationModelsManager.get_model_specs) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html#ibm_watsonx_ai.foundation_models_manager.FoundationModelsManager.get_model_specs "Link to this definition")

Retrieves a list of specifications for a deployed foundation model.

Parameters:

- **model\_id** ( _str_ _or_ [_ModelTypes_](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.utils.enums.ModelTypes "ibm_watsonx_ai.foundation_models.utils.enums.ModelTypes") _,_ _optional_) – ID of the model, defaults to None (all models specifications are returned)

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, will get all entries in ‘limited’ chunks


Returns:

list of specifications for the deployed foundation model

Return type:

dict or generator

**Example:**

```
# GET ALL MODEL SPECS
client.foundation_models.get_model_specs()

# GET MODEL SPECS BY MODEL_ID
client.foundation_models.get_model_specs(model_id="google/flan-ul2")

```

get\_model\_specs\_with\_fine\_tuning\_support( _model\_id=None_, _limit=None_, _asynchronous=False_, _get\_all=False_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models_manager.html#FoundationModelsManager.get_model_specs_with_fine_tuning_support) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html#ibm_watsonx_ai.foundation_models_manager.FoundationModelsManager.get_model_specs_with_fine_tuning_support "Link to this definition")

Operations to query the details of the deployed foundation models with fine-tuning support.

Parameters:

- **model\_id** ( _str_ _,_ _optional_) – Id of the model, defaults to None (all models specs are returned).

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, it will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, it will get all entries in ‘limited’ chunks


Returns:

list of deployed foundation model specs with fine-tuning support

Return type:

dict or generator

**Example**

```
client.foundation_models.get_model_specs_with_fine_tuning_support()
client.foundation_models.get_model_specs_with_fine_tuning_support('bigscience/bloom')

```

get\_model\_specs\_with\_lora\_fine\_tuning\_support( _model\_id=None_, _limit=None_, _asynchronous=False_, _get\_all=False_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models_manager.html#FoundationModelsManager.get_model_specs_with_lora_fine_tuning_support) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html#ibm_watsonx_ai.foundation_models_manager.FoundationModelsManager.get_model_specs_with_lora_fine_tuning_support "Link to this definition")

Operations to query the details of the deployed foundation models with lora fine-tuning support.

Parameters:

- **model\_id** ( _str_ _,_ _optional_) – Id of the model, defaults to None (all models specs are returned).

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, it will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, it will get all entries in ‘limited’ chunks


Returns:

list of deployed foundation model specs with lora fine-tuning support

Return type:

dict or generator

**Example**

```
client.foundation_models.get_model_specs_with_lora_fine_tuning_support()
client.foundation_models.get_model_specs_with_lora_fine_tuning_support('bigscience/bloom')

```

get\_model\_specs\_with\_prompt\_tuning\_support( _model\_id=None_, _limit=None_, _asynchronous=False_, _get\_all=False_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models_manager.html#FoundationModelsManager.get_model_specs_with_prompt_tuning_support) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html#ibm_watsonx_ai.foundation_models_manager.FoundationModelsManager.get_model_specs_with_prompt_tuning_support "Link to this definition")

Queries the details of deployed foundation models with prompt tuning support.

Parameters:

- **model\_id** ( _str_ _,_ _optional_) – ID of the model, defaults to None (all models specifications are returned)

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, will get all entries in ‘limited’ chunks


Returns:

list of specifications of a deployed foundation model with prompt tuning support

Return type:

dict or generator

**Example:**

```
client.foundation_models.get_model_specs_with_prompt_tuning_support()
client.foundation_models.get_model_specs_with_prompt_tuning_support('google/flan-t5-xl')

```

get\_rerank\_model\_specs( _model\_id=None_, _limit=None_, _asynchronous=False_, _get\_all=False_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models_manager.html#FoundationModelsManager.get_rerank_model_specs) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html#ibm_watsonx_ai.foundation_models_manager.FoundationModelsManager.get_rerank_model_specs "Link to this definition")

Retrieves the specifications of a rerank model.

Parameters:

- **model\_id** ( _str_ _,_ _optional_) – ID of the model, defaults to None (all models specifications are returned)

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, will get all entries in ‘limited’ chunks


Returns:

specifications of the rerank model

Return type:

dict or generator

**Example:**

```
client.foundation_models.get_rerank_model_specs()
client.foundation_models.get_rerank_model_specs('ibm/slate-125m-english-rtrvr-v2')

```

get\_time\_series\_model\_specs( _model\_id=None_, _limit=None_, _asynchronous=False_, _get\_all=False_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models_manager.html#FoundationModelsManager.get_time_series_model_specs) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html#ibm_watsonx_ai.foundation_models_manager.FoundationModelsManager.get_time_series_model_specs "Link to this definition")

Retrieves the specifications of an time series model.

Parameters:

- **model\_id** ( _str_ _,_ _optional_) – ID of the model, defaults to None (all models specifications are returned)

- **limit** ( _int_ _,_ _optional_) – limit number of fetched records

- **asynchronous** ( _bool_ _,_ _optional_) – if True, will work as a generator

- **get\_all** ( _bool_ _,_ _optional_) – if True, will get all entries in ‘limited’ chunks


Returns:

specifications of the time series model

Return type:

dict or generator

**Example:**

```
client.foundation_models.get_time_series_model_specs()
client.foundation_models.get_time_series_model_specs('ibm/granite-ttm-1536-96-r2')

```

ibm\_watsonx\_ai.foundation\_models.get\_model\_specs( _url_, _model\_id=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/utils/utils.html#get_model_specs) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html#ibm_watsonx_ai.foundation_models.get_model_specs "Link to this definition")

Retrieve the list of deployed foundation models specifications.

**Decrecated:** From `ibm_watsonx_ai` 1.0, the get\_model\_specs() function is deprecated, use the client.foundation\_models.get\_model\_specs() function instead.

Parameters:

- **url** ( _str_) – URL of the environment

- **model\_id** ( _Optional_ _\[_ _str_ _,_ [_ModelTypes_](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.utils.enums.ModelTypes "ibm_watsonx_ai.foundation_models.utils.enums.ModelTypes") _\]_ _,_ _optional_) – ID of the model, defaults to None (all models specs are returned).


Returns:

list of deployed foundation model specs

Return type:

dict

**Example:**

```
from ibm_watsonx_ai.foundation_models import get_model_specs

# GET ALL MODEL SPECS
get_model_specs(
    url="https://us-south.ml.cloud.ibm.com"
    )

# GET MODEL SPECS BY MODEL_ID
get_model_specs(
    url="https://us-south.ml.cloud.ibm.com",
    model_id="google/flan-ul2"
    )

```

ibm\_watsonx\_ai.foundation\_models.get\_model\_lifecycle( _url_, _model\_id_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/utils/utils.html#get_model_lifecycle) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html#ibm_watsonx_ai.foundation_models.get_model_lifecycle "Link to this definition")

Retrieve the list of model lifecycle data.

**Decrecated:** From `ibm_watsonx_ai` 1.0, the get\_model\_lifecycle() function is deprecated, use client.foundation\_models.get\_model\_lifecycle() function instead.

Parameters:

- **url** ( _str_) – URL of environment

- **model\_id** ( _str_) – the type of model to use


Returns:

list of deployed foundation model lifecycle data

Return type:

list

**Example:**

```
from ibm_watsonx_ai.foundation_models import get_model_lifecycle

get_model_lifecycle(
    url="https://us-south.ml.cloud.ibm.com",
    model_id="ibm/granite-13b-instruct-v2"
    )

```

ibm\_watsonx\_ai.foundation\_models.get\_model\_specs\_with\_prompt\_tuning\_support( _url_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/utils/utils.html#get_model_specs_with_prompt_tuning_support) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html#ibm_watsonx_ai.foundation_models.get_model_specs_with_prompt_tuning_support "Link to this definition")

Query the details of the deployed foundation models with prompt tuning support.

**Decrecated:** From `ibm_watsonx_ai` 1.0, the get\_model\_specs\_with\_prompt\_tuning\_support() function is deprecated, use the client.foundation\_models.get\_model\_specs\_with\_prompt\_tuning\_support() function instead.

Parameters:

**url** ( _str_) – URL of environment

Returns:

list of deployed foundation model specs with prompt tuning support

Return type:

dict

**Example:**

```
from ibm_watsonx_ai.foundation_models import get_model_specs_with_prompt_tuning_support

get_model_specs_with_prompt_tuning_support(
    url="https://us-south.ml.cloud.ibm.com"
    )

```

ibm\_watsonx\_ai.foundation\_models.get\_supported\_tasks( _url_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/utils/utils.html#get_supported_tasks) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html#ibm_watsonx_ai.foundation_models.get_supported_tasks "Link to this definition")

Retrieves a list of tasks that are supported by the foundation models.

Parameters:

**url** ( _str_) – URL of the environment

Returns:

list of tasks that are supported by the foundation models

Return type:

dict

**Example:**

```
from ibm_watsonx_ai.foundation_models import get_supported_tasks

get_supported_tasks(
    url="https://us-south.ml.cloud.ibm.com"
    )

```