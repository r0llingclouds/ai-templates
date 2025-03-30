ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://ibm.github.io/watsonx-ai-python-sdk/fm_ts_model_inference.html#furo-main-content)

[Back to top](https://ibm.github.io/watsonx-ai-python-sdk/fm_ts_model_inference.html#)

[View this page](https://ibm.github.io/watsonx-ai-python-sdk/_sources/fm_ts_model_inference.rst.txt "View this page")

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# TSModelInference [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_ts_model_inference.html\#tsmodelinference "Link to this heading")

_class_ ibm\_watsonx\_ai.foundation\_models.inference.TSModelInference( _model\_id_, _params=None_, _credentials=None_, _project\_id=None_, _space\_id=None_, _verify=None_, _api\_client=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/inference/ts_model_inference.html#TSModelInference) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_ts_model_inference.html#ibm_watsonx_ai.foundation_models.inference.TSModelInference "Link to this definition")

Bases: `WMLResource`

Instantiate the time series model interface

Parameters:

- **model\_id** ( _str_) – type of model to use

- **params** ( _dict_ _,_ [_TSForecastParameters_](https://ibm.github.io/watsonx-ai-python-sdk/fm_schema.html#ibm_watsonx_ai.foundation_models.schema.TSForecastParameters "ibm_watsonx_ai.foundation_models.schema.TSForecastParameters") _,_ _optional_) – parameters to use during request generation

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
from ibm_watsonx_ai.foundation_models import TSModelInference

forecasting_params = {
    "prediction_length": 10
}

ts_model = TSModelInference(
    model_id="<TIME SERIES MODEL>",
    params=forecasting_params,
    credentials=Credentials(
        api_key = IAM_API_KEY,
        url = "https://us-south.ml.cloud.ibm.com"),
    project_id=project_id
)

```

forecast( _data_, _params=None_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/inference/ts_model_inference.html#TSModelInference.forecast) [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_ts_model_inference.html#ibm_watsonx_ai.foundation_models.inference.TSModelInference.forecast "Link to this definition")

Generates a forecast based on the provided data and model parameters.

Parameters:

- **data** ( _dict_ _,_ _pd.DataFrame_ _,_ _required_) – A payload of data matching the schema provided. For more information about the data limitation see the product documentation [https://cloud.ibm.com/apidocs/watsonx-ai](https://cloud.ibm.com/apidocs/watsonx-ai).

- **params** ( _dict_ _,_ [_TSForecastParameters_](https://ibm.github.io/watsonx-ai-python-sdk/fm_schema.html#ibm_watsonx_ai.foundation_models.schema.TSForecastParameters "ibm_watsonx_ai.foundation_models.schema.TSForecastParameters") _,_ _optional_) – Contains basic metadata about your time series data input. These metadata are used by the server to understand which field represents a time stamp or which are unique identifiers for separating time series from different input channels.


**Example:**

```
# number of elements in the array for each field must be at least 512, 1024, or 1536 depending on the model; for example 512 for ibm/granite-ttm-512-96-r2
data = {
        "date": [\
            "2017-10-02T16:00:00",\
            "2017-10-02T17:00:00",\
            "2017-10-02T18:00:00"\
            ...\
        ],
        "HUFL": [\
            1.1,\
            2.2,\
            3.3\
            ...\
        ]
    }

params =  {
    "timestamp_column": "date",
    "target_columns": [\
        "HUFL",\
    ],
    "prediction_length": 10
    "freq": "1h"
},

# The number of elements in the array for each field must be the prediction length of the model depending on the model; for example 96 for ibm/granite-ttm-512-96-r2,

response = ts_model.forecast(data=data, params=params)

# Print all response
print(response)

```

## Enums [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_ts_model_inference.html\#enums "Link to this heading")

_class_ TimeSeriesModels [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_ts_model_inference.html#TimeSeriesModels "Link to this definition")

Bases: `StrEnum`

This represents a dynamically generated Enum for Time Series Foundation Models.

**Example of getting TimeSeriesModels:**

```
# GET TimeSeriesModels ENUM
client.foundation_models.TimeSeriesModels

# PRINT dict of Enums
client.foundation_models.TimeSeriesModels.show()

```

**Example Output:**

```
{'GRANITE_TTM_1024_96_R2': 'ibm/granite-ttm-1024-96-r2',
 'GRANITE_TTM_1536_96_R2': 'ibm/granite-ttm-1536-96-r2',
 'GRANITE_TTM_512_96_R2': 'ibm/granite-ttm-512-96-r2'}

```

**Example of initialising ModelInference with TimeSeriesModels Enum:**

```
from ibm_watsonx_ai.foundation_models import TSModelInference

model = TSModelInference(
    model_id=client.foundation_models.TimeSeriesModels.GRANITE_TTM_1024_96_R2,
    credentials=Credentials(...),
    project_id=project_id,
)

```