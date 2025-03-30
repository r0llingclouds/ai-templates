ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://ibm.github.io/watsonx-ai-python-sdk/fm_text_extraction.html#furo-main-content)

[Back to top](https://ibm.github.io/watsonx-ai-python-sdk/fm_text_extraction.html#)

[View this page](https://ibm.github.io/watsonx-ai-python-sdk/_sources/fm_text_extraction.rst.txt "View this page")

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Text Extractions [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_text_extraction.html\#text-extractions "Link to this heading")

_class_ ibm\_watsonx\_ai.foundation\_models.extractions.TextExtractions( _credentials=None_, _project\_id=None_, _space\_id=None_, _api\_client=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extractions/text_extractions.html#TextExtractions) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_text_extraction.html#ibm_watsonx_ai.foundation_models.extractions.TextExtractions "Link to this definition")

Bases: `WMLResource`

Instantiate the Text Extraction service.

Parameters:

- **credentials** ( [_Credentials_](https://ibm.github.io/watsonx-ai-python-sdk/base.html#credentials.Credentials "credentials.Credentials") _,_ _optional_) – credentials to the Watson Machine Learning instance

- **project\_id** ( _str_ _,_ _optional_) – ID of the Watson Studio project, defaults to None

- **space\_id** ( _str_ _,_ _optional_) – ID of the Watson Studio space, defaults to None

- **api\_client** ( [_APIClient_](https://ibm.github.io/watsonx-ai-python-sdk/base.html#client.APIClient "client.APIClient") _,_ _optional_) – initialized APIClient object with a set project ID or space ID. If passed, `credentials` and `project_id`/ `space_id` are not required, defaults to None


Raises:

- **InvalidMultipleArguments** – raised if space\_id and project\_id or credentials and api\_client are provided simultaneously

- **WMLClientError** – raised if the CPD version is less than 5.0


```
 from ibm_watsonx_ai import Credentials
 from ibm_watsonx_ai.foundation_models.extractions import TextExtractions

extraction = TextExtractions(
     credentials=Credentials(
                         api_key = IAM_API_KEY,
                         url = "https://us-south.ml.cloud.ibm.com"),
     project_id="*****"
     )

```

cancel\_job( _extraction\_id_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extractions/text_extractions.html#TextExtractions.cancel_job) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_text_extraction.html#ibm_watsonx_ai.foundation_models.extractions.TextExtractions.cancel_job "Link to this definition")

Cancel a text extraction job.

Returns:

return “SUCCESS” if the cancellation succeeds

Return type:

str

**Example:**

```
extraction.cancel_job(extraction_id="<extraction_id>")

```

delete\_job( _extraction\_id_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extractions/text_extractions.html#TextExtractions.delete_job) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_text_extraction.html#ibm_watsonx_ai.foundation_models.extractions.TextExtractions.delete_job "Link to this definition")

Delete a text extraction job.

Returns:

return “SUCCESS” if the deletion succeeds

Return type:

str

**Example:**

```
extraction.delete_job(extraction_id="<extraction_id>")

```

_static_ get\_id( _extraction\_details_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extractions/text_extractions.html#TextExtractions.get_id) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_text_extraction.html#ibm_watsonx_ai.foundation_models.extractions.TextExtractions.get_id "Link to this definition")

Get the unique ID of a stored extraction request.

Parameters:

**extraction\_details** ( _dict_) – metadata of the stored extraction

Returns:

unique ID of the stored extraction request

Return type:

str

**Example:**

```
extraction_details = extraction.get_job_details(extraction_id)
extraction_id = extraction.get_id(extraction_details)

```

get\_job\_details( _extraction\_id=None_, _limit=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extractions/text_extractions.html#TextExtractions.get_job_details) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_text_extraction.html#ibm_watsonx_ai.foundation_models.extractions.TextExtractions.get_job_details "Link to this definition")

Return text extraction job details. If extraction\_id is None, returns the details of all text extraction jobs.

Parameters:

- **extraction\_id** ( _str_ _\|_ _None_ _,_ _optional_) – ID of the text extraction job, defaults to None

- **limit** ( _int_ _\|_ _None_ _,_ _optional_) – limit number of fetched records, defaults to None


Returns:

details of the text extraction job

Return type:

dict

**Example:**

```
extraction.get_job_details(extraction_id="<extraction_id>")

```

get\_results\_reference( _extraction\_id_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extractions/text_extractions.html#TextExtractions.get_results_reference) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_text_extraction.html#ibm_watsonx_ai.foundation_models.extractions.TextExtractions.get_results_reference "Link to this definition")

Get a DataConnection instance that is a reference to the results stored on COS.

Parameters:

**extraction\_id** ( _str_) – ID of text extraction job

Returns:

location of the Data Connection to text extraction job results

Return type:

[DataConnection](https://ibm.github.io/watsonx-ai-python-sdk/dataconnection_modules.html#ibm_watsonx_ai.helpers.connections.connections.DataConnection "ibm_watsonx_ai.helpers.connections.connections.DataConnection")

**Example:**

```
results_reference = extraction.get_results_reference(extraction_id="<extraction_id>")

```

list\_jobs( _limit=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extractions/text_extractions.html#TextExtractions.list_jobs) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_text_extraction.html#ibm_watsonx_ai.foundation_models.extractions.TextExtractions.list_jobs "Link to this definition")

List text extraction jobs. If limit is None, all jobs will be listed.

Parameters:

**limit** ( _int_ _\|_ _None_ _,_ _optional_) – limit number of fetched records, defaults to None

Returns:

job information of a pandas DataFrame with text extraction

Return type:

pandas.DataFrame

**Example:**

```
extraction.list_jobs()

```

run\_job( _document\_reference_, _results\_reference_, _steps=None_, _results\_format='json'_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/extractions/text_extractions.html#TextExtractions.run_job) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_text_extraction.html#ibm_watsonx_ai.foundation_models.extractions.TextExtractions.run_job "Link to this definition")

Start a request to extract text and metadata from a document.

Parameters:

- **document\_reference** ( [_DataConnection_](https://ibm.github.io/watsonx-ai-python-sdk/dataconnection_modules.html#ibm_watsonx_ai.helpers.connections.connections.DataConnection "ibm_watsonx_ai.helpers.connections.connections.DataConnection")) – reference to the document in the bucket from which text will be extracted

- **results\_reference** ( [_DataConnection_](https://ibm.github.io/watsonx-ai-python-sdk/dataconnection_modules.html#ibm_watsonx_ai.helpers.connections.connections.DataConnection "ibm_watsonx_ai.helpers.connections.connections.DataConnection")) – reference to the location in the bucket where results will saved

- **steps** ( _dict_ _\|_ _None_ _,_ _optional_) – steps for the text extraction pipeline, defaults to None

- **results\_format** ( _Literal_ _\[_ _"json"_ _,_ _"markdown"_ _\]_ _,_ _optional_) – results format for the text extraction, defaults to “json”


Returns:

raw response from the server with the text extraction job details

Return type:

dict

**Example:**

```
from ibm_watsonx_ai.metanames import TextExtractionsMetaNames
from ibm_watsonx_ai.helpers import DataConnection, S3Location

document_reference = DataConnection(
    connection_asset_id="<connection_id>",
    location=S3Location(bucket="<bucket_name>", path="path/to/file"),
    )

results_reference = DataConnection(
    connection_asset_id="<connection_id>",
    location=S3Location(bucket="<bucket_name>", path="path/to/file"),
    )

response = extraction.run_job(
    document_reference=document_reference,
    results_reference=results_reference,
    steps={
        TextExtractionsMetaNames.OCR: {"languages_list": ["en", "fr"]},
        TextExtractionsMetaNames.TABLE_PROCESSING: {"enabled": True},
        },
    results_format="markdown"
)

```

## Enums [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_text_extraction.html\#enums "Link to this heading")

_class_ metanames.TextExtractionsMetaNames [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/metanames.html#TextExtractionsMetaNames) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_text_extraction.html#metanames.TextExtractionsMetaNames "Link to this definition")

Set of MetaNames for Text Extraction Steps.

Available MetaNames:

|     |     |     |     |
| --- | --- | --- | --- |
| MetaName | Type | Required | Example value |
| OCR | dict | N | `{'languages_list': ['en']}` |
| TABLE\_PROCESSING | dict | N | `{'enabled': True}` |

Note

For more details about Text Extraction Steps, see [https://cloud.ibm.com/apidocs/watsonx-ai](https://cloud.ibm.com/apidocs/watsonx-ai)