ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#furo-main-content)

[Back to top](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#)

[View this page](https://ibm.github.io/watsonx-ai-python-sdk/_sources/fm_embeddings.rst.txt "View this page")

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Embeddings [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html\#embeddings "Link to this heading")

## Embeddings [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html\#id1 "Link to this heading")

_class_ ibm\_watsonx\_ai.foundation\_models.embeddings.Embeddings( _\*_, _model\_id_, _params=None_, _credentials=None_, _project\_id=None_, _space\_id=None_, _api\_client=None_, _verify=None_, _persistent\_connection=True_, _batch\_size=1000_, _concurrency\_limit=5_, _max\_retries=None_, _delay\_time=None_, _retry\_status\_codes=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/embeddings/embeddings.html#Embeddings) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#ibm_watsonx_ai.foundation_models.embeddings.Embeddings "Link to this definition")

Bases: [`BaseEmbeddings`](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#ibm_watsonx_ai.foundation_models.embeddings.base_embeddings.BaseEmbeddings "ibm_watsonx_ai.foundation_models.embeddings.base_embeddings.BaseEmbeddings"), `WMLResource`

Instantiate the embeddings service.

Parameters:

- **model\_id** ( _str_ _,_ _optional_) – the type of model to use

- **params** ( _dict_ _,_ _optional_) – parameters to use during generate requests, use `ibm_watsonx_ai.metanames.EmbedTextParamsMetaNames().show()` to view the list of MetaNames

- **credentials** ( _dict_ _,_ _optional_) – credentials for the Watson Machine Learning instance

- **project\_id** ( _str_ _,_ _optional_) – ID of the Watson Studio project

- **space\_id** ( _str_ _,_ _optional_) – ID of the Watson Studio space

- **api\_client** ( [_APIClient_](https://ibm.github.io/watsonx-ai-python-sdk/base.html#client.APIClient "client.APIClient") _,_ _optional_) – initialized APIClient object with a set project ID or space ID. If passed, `credentials` and `project_id`/ `space_id` are not required.

- **verify** ( _bool_ _or_ _str_ _,_ _optional_) –

You can pass one of following as verify:


  - the path to a CA\_BUNDLE file

  - the path of a directory with certificates of trusted CAs

  - True \- default path to truststore will be taken

  - False \- no verification will be made


- **persistent\_connection** ( _bool_ _,_ _optional_) – defines whether to keep a persistent connection when evaluating the generate, ‘embed\_query’, and ‘embed\_documents\` methods with one prompt
or batch of prompts that meet the length limit. For more details, see [Generate embeddings](https://cloud.ibm.com/apidocs/watsonx-ai#text-embeddings).
To close the connection, run embeddings.close\_persistent\_connection(), defaults to True. Added in 1.1.2.

- **batch\_size** ( _int_ _,_ _optional_) – Number of elements to be embedded sending in one call, defaults to 1000

- **concurrency\_limit** ( _int_ _,_ _optional_) – number of requests to be sent in parallel when generating embedding vectors, max is 10, defaults to 5

- **max\_retries** ( _int_ _,_ _optional_) – number of retries performed when request was not successful and status code is in retry\_status\_codes, defaults to 10

- **delay\_time** ( _float_ _,_ _optional_) – delay time to retry request, factor in exponential backoff formula: wx\_delay\_time \* pow(2.0, attempt), defaults to 0.5s

- **retry\_status\_codes** ( _list_ _\[_ _int_ _\]_ _,_ _optional_) – list of status codes which will be considered for retry mechanism, defaults to \[429, 503, 504, 520\]


Note

When the `credentials` parameter is passed, one of these parameters is required: \[ `project_id`, `space_id`\].

Hint

You can copy the project\_id from the Project’s Manage tab (Project -> Manage -> General -> Details).

**Example:**

```
 from ibm_watsonx_ai import Credentials
 from ibm_watsonx_ai.foundation_models import Embeddings
 from ibm_watsonx_ai.metanames import EmbedTextParamsMetaNames as EmbedParams
 from ibm_watsonx_ai.foundation_models.utils.enums import EmbeddingTypes

embed_params = {
     EmbedParams.TRUNCATE_INPUT_TOKENS: 3,
     EmbedParams.RETURN_OPTIONS: {
     'input_text': True
     }
 }

 embedding = Embeddings(
     model_id=EmbeddingTypes.IBM_SLATE_30M_ENG,
     params=embed_params,
     credentials=Credentials(
         api_key = IAM_API_KEY,
         url = "https://us-south.ml.cloud.ibm.com"),
     project_id="*****"
     )

```

close\_persistent\_connection() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/embeddings/embeddings.html#Embeddings.close_persistent_connection) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#ibm_watsonx_ai.foundation_models.embeddings.Embeddings.close_persistent_connection "Link to this definition")

Only applicable if persistent\_connection was set to True in Embeddings initialization.
Calling this method closes the current httpx.Client and recreates a new httpx.Client with default values:
timeout: httpx.Timeout(read=30 \* 60, write=30 \* 60, connect=10, pool=30 \* 60)
limit: httpx.Limits(max\_connections=10, max\_keepalive\_connections=10, keepalive\_expiry=HTTPX\_KEEPALIVE\_EXPIRY)

embed\_documents( _texts_, _params=None_, _concurrency\_limit=5_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/embeddings/embeddings.html#Embeddings.embed_documents) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#ibm_watsonx_ai.foundation_models.embeddings.Embeddings.embed_documents "Link to this definition")

Returns list of embedding vectors for provided texts.

Parameters:

- **texts** ( _list_ _\[_ _str_ _\]_) – list of texts for which embedding vectors will be generated

- **params** ( _ParamsType_ _\|_ _None_ _,_ _optional_) – MetaProps for the embedding generation, use `ibm_watsonx_ai.metanames.EmbedTextParamsMetaNames().show()` to view the list of MetaNames, defaults to None

- **concurrency\_limit** ( _int_ _,_ _optional_) – number of requests to be sent in parallel, max is 10, defaults to 5


Returns:

list of embedding vectors

Return type:

list\[list\[float\]\]

**Example:**

```
q = [\
    "What is a Generative AI?",\
    "Generative AI refers to a type of artificial intelligence that can original content."\
    ]

embedding_vectors = embedding.embed_documents(texts=q)
print(embedding_vectors)

```

embed\_query( _text_, _params=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/embeddings/embeddings.html#Embeddings.embed_query) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#ibm_watsonx_ai.foundation_models.embeddings.Embeddings.embed_query "Link to this definition")

Returns an embedding vector for a provided text.

Parameters:

- **text** ( _str_) – text for which embedding vector will be generated

- **params** ( _ParamsType_ _\|_ _None_ _,_ _optional_) – MetaProps for the embedding generation, use `ibm_watsonx_ai.metanames.EmbedTextParamsMetaNames().show()` to view the list of MetaNames, defaults to None


Returns:

embedding vector

Return type:

list\[float\]

**Example:**

```
q = "What is a Generative AI?"
embedding_vector = embedding.embed_query(text=q)
print(embedding_vector)

```

generate( _inputs_, _params=None_, _concurrency\_limit=5_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/embeddings/embeddings.html#Embeddings.generate) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#ibm_watsonx_ai.foundation_models.embeddings.Embeddings.generate "Link to this definition")

Generate embeddings vectors for the given input with the given
parameters. Returns a REST API response.

Parameters:

- **inputs** ( _list_ _\[_ _str_ _\]_) – list of texts for which embedding vectors will be generated

- **params** ( _ParamsType_ _\|_ _None_ _,_ _optional_) – MetaProps for the embedding generation, use `ibm_watsonx_ai.metanames.EmbedTextParamsMetaNames().show()` to view the list of MetaNames, defaults to None

- **concurrency\_limit** ( _int_ _,_ _optional_) – number of requests to be sent in parallel, max is 10, defaults to 5


Returns:

scoring results containing generated embeddings vectors

Return type:

dict

to\_dict() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/embeddings/embeddings.html#Embeddings.to_dict) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#ibm_watsonx_ai.foundation_models.embeddings.Embeddings.to_dict "Link to this definition")

Serialize Embeddings.

Returns:

serializes this Embeddings so that it can be reconstructed by `from_dict` class method.

Return type:

dict

## BaseEmbeddings [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html\#baseembeddings "Link to this heading")

_class_ ibm\_watsonx\_ai.foundation\_models.embeddings.base\_embeddings.BaseEmbeddings [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/embeddings/base_embeddings.html#BaseEmbeddings) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#ibm_watsonx_ai.foundation_models.embeddings.base_embeddings.BaseEmbeddings "Link to this definition")

Bases: `ABC`

LangChain-like embedding function interface.

_abstract_ embed\_documents( _texts_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/embeddings/base_embeddings.html#BaseEmbeddings.embed_documents) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#ibm_watsonx_ai.foundation_models.embeddings.base_embeddings.BaseEmbeddings.embed_documents "Link to this definition")

Embed search docs.

_abstract_ embed\_query( _text_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/embeddings/base_embeddings.html#BaseEmbeddings.embed_query) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#ibm_watsonx_ai.foundation_models.embeddings.base_embeddings.BaseEmbeddings.embed_query "Link to this definition")

Embed query text.

_classmethod_ from\_dict( _data_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/embeddings/base_embeddings.html#BaseEmbeddings.from_dict) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#ibm_watsonx_ai.foundation_models.embeddings.base_embeddings.BaseEmbeddings.from_dict "Link to this definition")

Deserialize `BaseEmbeddings` into a concrete one using arguments.

Returns:

concrete Embeddings or None if data is incorrect

Return type:

[BaseEmbeddings](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#ibm_watsonx_ai.foundation_models.embeddings.base_embeddings.BaseEmbeddings "ibm_watsonx_ai.foundation_models.embeddings.base_embeddings.BaseEmbeddings") \| None

to\_dict() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/embeddings/base_embeddings.html#BaseEmbeddings.to_dict) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#ibm_watsonx_ai.foundation_models.embeddings.base_embeddings.BaseEmbeddings.to_dict "Link to this definition")

Serialize Embeddings.

Returns:

serializes this Embeddings so that it can be reconstructed by `from_dict` class method.

Return type:

dict

## Enums [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html\#enums "Link to this heading")

_class_ metanames.EmbedTextParamsMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#EmbedTextParamsMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#metanames.EmbedTextParamsMetaNames "Link to this definition")

Set of MetaNames for Foundation Model Embeddings Parameters.

Available MetaNames:

|     |     |     |     |
| --- | --- | --- | --- |
| MetaName | Type | Required | Example value |
| TRUNCATE\_INPUT\_TOKENS | int | N | `2` |
| RETURN\_OPTIONS | dict | N | `{'input_text': True}` |

_class_ EmbeddingModels [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#EmbeddingModels "Link to this definition")

Bases: `StrEnum`

This represents a dynamically generated Enum for Embedding Models.

**Example of getting EmbeddingModels**

```
# GET EmbeddingModels ENUM
client.foundation_models.EmbeddingModels

# PRINT dict of Enums
client.foundation_models.EmbeddingModels.show()

```

**Example Output:**

```
{'SLATE_125M_ENGLISH_RTRVR': 'ibm/slate-125m-english-rtrvr',
...
'SLATE_30M_ENGLISH_RTRVR': 'ibm/slate-30m-english-rtrvr'}

```

**Example of initialising Embeddings with EmbeddingModels Enum:**

```
from ibm_watsonx_ai.foundation_models import Embeddings

embeddings = Embeddings(
    model_id=client.foundation_models.EmbeddingModels.SLATE_30M_ENGLISH_RTRVR,
    credentials=Credentials(...),
    project_id=project_id,
)

```

_class_ ibm\_watsonx\_ai.foundation\_models.utils.enums.EmbeddingTypes( _value_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/utils/enums.html#EmbeddingTypes) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#ibm_watsonx_ai.foundation_models.utils.enums.EmbeddingTypes "Link to this definition")

Bases: `Enum`

Deprecated since version 1.0.5: Use [`EmbeddingModels()`](https://ibm.github.io/watsonx-ai-python-sdk/fm_embeddings.html#EmbeddingModels "EmbeddingModels") instead.

Supported embedding models.

Note

You can check the current list of supported embeddings model types of various environments with
[`get_embeddings_model_specs()`](https://ibm.github.io/watsonx-ai-python-sdk/fm_helpers.html#ibm_watsonx_ai.foundation_models_manager.FoundationModelsManager.get_embeddings_model_specs "ibm_watsonx_ai.foundation_models_manager.FoundationModelsManager.get_embeddings_model_specs")
or by referring to the [watsonx.ai](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-models-embed.html?context=wx)
documentation.