ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://ibm.github.io/watsonx-ai-python-sdk/base.html#furo-main-content)

[Back to top](https://ibm.github.io/watsonx-ai-python-sdk/base.html#)

[View this page](https://ibm.github.io/watsonx-ai-python-sdk/_sources/base.rst.txt "View this page")

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Base [¶](https://ibm.github.io/watsonx-ai-python-sdk/base.html\#base "Link to this heading")

## APIClient [¶](https://ibm.github.io/watsonx-ai-python-sdk/base.html\#apiclient "Link to this heading")

_class_ client.APIClient( _credentials=None_, _project\_id=None_, _space\_id=None_, _verify=None_, _httpx\_client=HttpClientConfig(timeout=Timeout(connect=10,read=1800,write=1800,pool=1800),limits=Limits(max\_connections=10,max\_keepalive\_connections=10,keepalive\_expiry=5))_, _async\_httpx\_client=HttpClientConfig(timeout=Timeout(connect=10,read=1800,write=1800,pool=1800),limits=Limits(max\_connections=10,max\_keepalive\_connections=10,keepalive\_expiry=5))_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/client.html#APIClient) [¶](https://ibm.github.io/watsonx-ai-python-sdk/base.html#client.APIClient "Link to this definition")

The main class of ibm\_watsonx\_ai. The very heart of the module. APIClient contains objects that manage the service reasources.

To explore how to use APIClient, refer to:

- [Setup](https://ibm.github.io/watsonx-ai-python-sdk/setup.html#setup) \- to check correct initialization of APIClient for a specific environment.

- [Core](https://ibm.github.io/watsonx-ai-python-sdk/core_api.html#core) \- to explore core properties of an APIClient object.


Parameters:

- **url** ( _str_) – URL of the service

- **credentials** ( [_Credentials_](https://ibm.github.io/watsonx-ai-python-sdk/base.html#credentials.Credentials "credentials.Credentials")) – credentials used to connect with the service

- **project\_id** ( _str_ _,_ _optional_) – ID of the project that is used

- **space\_id** ( _str_ _,_ _optional_) – ID of deployment space that is used

- **verify** ( _bool_ _,_ _optional_) – certificate verification flag, deprecated, use Credentials(verify=…) to set verify

- **httpx\_client** ( _httpx.Client_ _,_ _HttpClientConfig_ _,_ _optional_) –

A customizable httpx.Client for ModelInference, Embeddings and methods related to the deployments management and scoring.
The httpx.Client is used to improve performance across deployments, foundation models, and embeddings. This parameter accepts two types of input:


  - A direct instance of httpx.Client()

  - A set of parameters provided via the HttpClientConfig class


**Example:**

```
from ibm_watsonx_ai.utils.utils import HttpClientConfig

limits=httpx.Limits(
    max_connections=5
)
timeout = httpx.Timeout(7)
http_config = HttpClientConfig(timeout=timeout, limits=limits)

```

If not provided, a default instance of httpx.Client is created.

Note

If you need to adjust timeouts or limits, using `HttpClientConfig` is the recommended approach.
When the `proxies` parameter is provided in credentials, `httpx.Client` will use these proxies.
However, if you want to create a separate `httpx.Client`, all parameters must be provided by the user.

- **async\_httpx\_client** ( _httpx.AsyncClient_ _,_ _HttpClientConfig_ _,_ _optional_) –

A customizable httpx.AsyncClient for ModelInference. The httpx.AsyncClient is used to improve performance of foundation models inference. This parameter accepts two types of input:


  - A direct instance of httpx.AsyncClient

  - A set of parameters provided via the HttpClientConfig class


**Example:**

```
from ibm_watsonx_ai.utils.utils import HttpClientConfig

limits=httpx.Limits(
    max_connections=5
)
timeout = httpx.Timeout(7)
http_config = HttpClientConfig(timeout=timeout, limits=limits)

```

If not provided, a default instance of httpx.AsyncClient is created.

Note

If you need to adjust timeouts or limits, using `HttpClientConfig` is the recommended approach.
When the `proxies` parameter is provided in credentials, `httpx.Client` will use these proxies.
However, if you want to create a separate `httpx.Client`, all parameters must be provided by the user.

**Example:**

```
from ibm_watsonx_ai import APIClient, Credentials

credentials = Credentials(
    url = "<url>",
    api_key = IAM_API_KEY
)

client = APIClient(credentials, space_id="<space_id>")

client.models.list()
client.deployments.get_details()

client.set.default_project("<project_id>")

...

```

set\_headers( _headers_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/client.html#APIClient.set_headers) [¶](https://ibm.github.io/watsonx-ai-python-sdk/base.html#client.APIClient.set_headers "Link to this definition")

Method which allows refresh/set new User Request Headers.

Parameters:

**headers** ( _dict_) – User Request Headers

**Examples**

```
headers = {
    'Authorization': 'Bearer <USER AUTHORIZATION TOKEN>',
    'User-Agent': 'ibm-watsonx-ai/1.0.1 (lang=python; arch=x86_64; os=darwin; python.version=3.10.13)',
    'Content-Type': 'application/json'
}

client.set_headers(headers)

```

set\_token( _token_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/client.html#APIClient.set_token) [¶](https://ibm.github.io/watsonx-ai-python-sdk/base.html#client.APIClient.set_token "Link to this definition")

Method which allows refresh/set new User Authorization Token.

Note

Using this function will cause that token will not be automatically refreshed anymore, if password or apikey were passed.
The user needs to take care of token refresh using set\_token function from that point in time until they finish using the client instance.

Parameters:

**token** ( _str_) – User Authorization Token

**Examples**

```
client.set_token("<USER AUTHORIZATION TOKEN>")

```

## Credentials [¶](https://ibm.github.io/watsonx-ai-python-sdk/base.html\#credentials "Link to this heading")

_class_ credentials.Credentials( _\*_, _url=None_, _api\_key=None_, _name=None_, _iam\_serviceid\_crn=None_, _token=None_, _projects\_token=None_, _username=None_, _password=None_, _instance\_id=None_, _version=None_, _bedrock\_url=None_, _platform\_url=None_, _proxies=None_, _verify=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/credentials.html#Credentials) [¶](https://ibm.github.io/watsonx-ai-python-sdk/base.html#credentials.Credentials "Link to this definition")

This class encapsulate passed credentials and additional params.

Parameters:

- **url** ( _str_) – URL of the service

- **api\_key** ( _str_ _,_ _optional_) – service API key used in API key authentication

- **name** ( _str_ _,_ _optional_) – service name used during space creation for a Cloud environment

- **iam\_serviceid\_crn** ( _str_ _,_ _optional_) – service CRN used during space creation for a Cloud environment

- **token** ( _str_ _,_ _optional_) – service token, used in token authentication

- **projects\_token** ( _str_ _,_ _optional_) – service projects token used in token authentication

- **username** ( _str_ _,_ _optional_) – username, used in username/password or username/api\_key authentication, applicable for ICP only

- **password** ( _str_ _,_ _optional_) – password, used in username/password authentication, applicable for ICP only

- **instance\_id** ( _str_ _,_ _optional_) – instance ID, mandatory for ICP

- **version** ( _str_ _,_ _optional_) – IBM Cloud Pak® for Data two-digit version, if not provided the version will be recognized automatically for IBM Cloud Pak® for Data 4.8 release and higher.

- **bedrock\_url** ( _str_ _,_ _optional_) – Bedrock URL, applicable for ICP only

- **proxies** ( _dict_ _,_ _optional_) – dictionary of proxies, containing protocol and URL mapping (example: { “https”: “https://example.url.com” })

- **verify** ( _bool_ _,_ _optional_) – certificate verification flag


**Example of create Credentials object**

- IBM watsonx.ai for IBM Cloud


```
from ibm_watsonx_ai import Credentials

# Example of creating the credentials using an API key:
credentials = Credentials(
    url = "https://us-south.ml.cloud.ibm.com",
    api_key = IAM_API_KEY
)

# Example of creating the credentials using a token:
credentials = Credentials(
    url = "https://us-south.ml.cloud.ibm.com",
    token = "***********"
)

```

- IBM watsonx.ai software


```
import os
from ibm_watsonx_ai import Credentials

# Example of creating the credentials using username and password:
credentials = Credentials(
    url = "<URL>",
    username = "<USERNAME>",
    password = "<PASSWORD>",
    instance_id = "openshift"
)

# Example of creating the credentials using username and apikey:
credentials = Credentials(
    url = "<URL>",
    username = "<USERNAME>",
    api_key = IAM_API_KEY,
    instance_id = "openshift"
)

# Example of creating the credentials using a token:
access_token = os.environ['USER_ACCESS_TOKEN']
credentials = Credentials(
    url = "<URL>",
    token = access_token,
    instance_id = "openshift"
    version = "5.0" # optional
)

```

_static_ from\_dict( _credentials_, _\_verify=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/credentials.html#Credentials.from_dict) [¶](https://ibm.github.io/watsonx-ai-python-sdk/base.html#credentials.Credentials.from_dict "Link to this definition")

Create a Credentials object from dictionary.

Parameters:

**credentials** ( _dict_) – credentials in the dictionary

Returns:

initialised credentials object

Return type:

[Credentials](https://ibm.github.io/watsonx-ai-python-sdk/base.html#credentials.Credentials "credentials.Credentials")

**Example:**

```
from ibm_watsonx_ai import Credentials

credentials = Credentials.from_dict({
    'url': "<url>",
    'apikey': IAM_API_URL
})

```

to\_dict() [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/credentials.html#Credentials.to_dict) [¶](https://ibm.github.io/watsonx-ai-python-sdk/base.html#credentials.Credentials.to_dict "Link to this definition")

Get dictionary from the Credentials object.

Returns:

dictionary with credentials

Return type:

dict

**Example:**

```
from ibm_watsonx_ai import Credentials

credentials = Credentials.from_dict({
    'url': "<url>",
    'apikey': IAM_API_KEY
})

credentials_dict = credentials.to_dict()

```