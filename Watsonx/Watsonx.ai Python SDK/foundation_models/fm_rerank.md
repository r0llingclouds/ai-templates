ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://ibm.github.io/watsonx-ai-python-sdk/fm_rerank.html#furo-main-content)

[Back to top](https://ibm.github.io/watsonx-ai-python-sdk/fm_rerank.html#)

[View this page](https://ibm.github.io/watsonx-ai-python-sdk/_sources/fm_rerank.rst.txt "View this page")

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Rerank [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_rerank.html\#rerank "Link to this heading")

_class_ ibm\_watsonx\_ai.foundation\_models.rerank.Rerank( _model\_id_, _params=None_, _credentials=None_, _project\_id=None_, _space\_id=None_, _verify=None_, _api\_client=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/rerank/rerank.html#Rerank) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_rerank.html#ibm_watsonx_ai.foundation_models.rerank.Rerank "Link to this definition")

Bases: `WMLResource`

Rerank texts based on some queries.

Parameters:

- **model\_id** ( _str_) – type of model to use

- **params** ( _dict_ _,_ [_RerankParameters_](https://ibm.github.io/watsonx-ai-python-sdk/fm_schema.html#ibm_watsonx_ai.foundation_models.schema.RerankParameters "ibm_watsonx_ai.foundation_models.schema.RerankParameters") _,_ _optional_) – parameters to use during request generation

- **credentials** ( [_Credentials_](https://ibm.github.io/watsonx-ai-python-sdk/base.html#credentials.Credentials "credentials.Credentials") _or_ _dict_ _,_ _optional_) – credentials for the Watson Machine Learning instance

- **project\_id** ( _str_ _,_ _optional_) – ID of the Watson Studio project

- **space\_id** ( _str_ _,_ _optional_) – ID of the Watson Studio space

- **verify** ( _bool_ _or_ _str_ _,_ _optional_) –

You can pass one of the following as verify:


  - the path to a CA\_BUNDLE file

  - the path of directory with certificates of trusted CAs

  - True \- default path to truststore will be taken

  - False \- no verification will be made


- **api\_client** ( [_APIClient_](https://ibm.github.io/watsonx-ai-python-sdk/base.html#client.APIClient "client.APIClient") _,_ _optional_) – initialized APIClient object with a set project ID or space ID. If passed, `credentials` and `project_id`/ `space_id` are not required.


**Example:**

```
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import Rerank

generate_params = {
    "truncate_input_tokens": 10
}

wx_ranker = Rerank(
    model_id="<RERANK MODEL>",
    params=generate_params,
    credentials=Credentials(
        api_key = IAM_API_KEY,
        url = "https://us-south.ml.cloud.ibm.com"),
    project_id=project_id
)

```

generate( _query_, _inputs_, _params=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/rerank/rerank.html#Rerank.generate) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_rerank.html#ibm_watsonx_ai.foundation_models.rerank.Rerank.generate "Link to this definition")

Calling this method generates the following auditing event.

Parameters:

- **query** ( _str_) – The rank query.

- **inputs** ( _list_ _\[_ _str_ _\]_ _,_ _list_ _\[_ _dict_ _\[_ _'text'_ _,_ _str_ _\]_ _\]_) – The rank input strings.

- **params** ( _dict_ _,_ [_RerankParameters_](https://ibm.github.io/watsonx-ai-python-sdk/fm_schema.html#ibm_watsonx_ai.foundation_models.schema.RerankParameters "ibm_watsonx_ai.foundation_models.schema.RerankParameters") _,_ _optional_)


**Example:**

```
query = "As a Youth, I craved excitement while in adulthood I followed Enthusiastic Pursuit."
inputs = [\
    "In my younger years, I often reveled in the excitement of spontaneous adventures and embraced the thrill of the unknown, whereas in my grownup life, I have come to appreciate the comforting stability of a well-established routine.",\
    "As a young man, I frequently sought out exhilarating experiences, craving the adrenaline rush of lifes novelties, while as a responsible adult, I have come to understand the profound value of accumulated wisdom and life experience."\
]
response = wx_ranker.generate(query=query, inputs=inputs)

# Print all response
print(response)

```

## Enums [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_rerank.html\#enums "Link to this heading")

_class_ RerankModels [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_rerank.html#RerankModels "Link to this definition")

Bases: `StrEnum`

This represents a dynamically generated Enum for Rerank Models.

**Example of getting RerankModels**

```
# GET RerankModels ENUM
client.foundation_models.RerankModels

# PRINT dict of Enums
client.foundation_models.RerankModels.show()

```

**Example Output:**

```
{'MS_MARCO_MINILM_L_12_V2': 'cross-encoder/ms-marco-minilm-l-12-v2',
...
'ALL_MINILM_L6_V2': 'sentence-transformers/all-minilm-l6-v2'}

```

**Example of initialising Rerank with RerankModels Enum:**

```
from ibm_watsonx_ai.foundation_models import Rerank

rerank = Rerank(
    model_id=client.foundation_models.RerankModels.MS_MARCO_MINILM_L_12_V2,
    credentials=Credentials(...),
    project_id=project_id,
)

```