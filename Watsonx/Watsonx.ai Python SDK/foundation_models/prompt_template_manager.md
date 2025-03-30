ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#furo-main-content)

[Back to top](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#)

[View this page](https://ibm.github.io/watsonx-ai-python-sdk/_sources/prompt_template_manager.rst.txt "View this page")

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Prompt Template Manager [¶](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html\#prompt-template-manager "Link to this heading")

_class_ ibm\_watsonx\_ai.foundation\_models.prompts.PromptTemplateManager( _credentials=None_, _\*_, _project\_id=None_, _space\_id=None_, _verify=None_, _api\_client=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/prompts/prompt_template.html#PromptTemplateManager) [¶](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.PromptTemplateManager "Link to this definition")

Bases: `WMLResource`

Instantiate the prompt template manager.

Parameters:

- **credentials** ( [_Credentials_](https://ibm.github.io/watsonx-ai-python-sdk/base.html#credentials.Credentials "credentials.Credentials") _or_ _dict_ _,_ _optional_) – credentials for the watsonx.ai instance

- **project\_id** ( _str_ _,_ _optional_) – ID of the project

- **space\_id** ( _str_ _,_ _optional_) – ID of the space

- **verify** ( _bool_ _or_ _str_ _,_ _optional_) – You can pass one of the following as verify:
\\* the path to a CA\_BUNDLE file
\\* the path of directory with certificates of trusted CAs
\\* True \- default path to truststore will be taken
\\* False \- no verification will be made


Note

One of these parameters is required: \[‘project\_id ‘, ‘space\_id’\]

**Example:**

```
from ibm_watsonx_ai import Credentials

from ibm_watsonx_ai.foundation_models.prompts import PromptTemplate, PromptTemplateManager

prompt_mgr = PromptTemplateManager(
                credentials=Credentials(
                    api_key=IAM_API_KEY,
                    url="https://us-south.ml.cloud.ibm.com"
                ),
                project_id="*****"
                )

prompt_template = PromptTemplate(name="My prompt",
                                 model_id='meta-llama/llama-3-3-70b-instruct',
                                 input_prefix="Human:",
                                 output_prefix="Assistant:",
                                 input_text="What is {object} and how does it work?",
                                 input_variables=['object'],
                                 examples=[['What is the Stock Market?',\
                                            'A stock market is a place where investors buy and sell shares of publicly traded companies.']])

stored_prompt_template = prompt_mgr.store_prompt(prompt_template)
print(stored_prompt_template.prompt_id)   # id of prompt template asset

```

Note

Here’s an example of how you can pass variables to your deployed prompt template:

```
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames

meta_props = {
    client.deployments.ConfigurationMetaNames.NAME: "SAMPLE DEPLOYMENT PROMPT TEMPLATE",
    client.deployments.ConfigurationMetaNames.ONLINE: {},
    client.deployments.ConfigurationMetaNames.BASE_MODEL_ID: 'meta-llama/llama-3-3-70b-instruct'
    }

deployment_details = client.deployments.create(stored_prompt_template.prompt_id, meta_props)

client.deployments.generate_text(
    deployment_id=deployment_details["metadata"]["id"],
    params={
        GenTextParamsMetaNames.PROMPT_VARIABLES: {
            "object": "brain"
        }
    }
)

```

add\_chat\_items( _prompt\_id_, _chat\_items_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/prompts/prompt_template.html#PromptTemplateManager.add_chat_items) [¶](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.PromptTemplateManager.add_chat_items "Link to this definition")

Add a new chat items to a prompt.

Parameters:

- **prompt\_id** ( _str_) – ID of the prompt template

- **chat\_items** ( _list_ _\[_ _dict_ _\]_) – Chat items to be added to prompt


Returns:

status (“SUCCESS” if succeeded)

Return type:

str

**Example:**

```
prompt_mgr.add_chat_items(
    prompt_id="<PROMPT_ID>",
    chat_items=[\
        {\
            "type": "<CHAT ITEM TYPE>",\
            "content": "<CHAT ITEM CONTENT>",\
            "status": "<CHAT ITEM STATUS>",\
            "timestamp": <TIMESTAMP_AS_INT>,\
        },\
        {\
            "type": "<CHAT ITEM TYPE>",\
            "content": "<CHAT ITEM CONTENT>",\
            "status": "<CHAT ITEM STATUS>",\
            "timestamp": <TIMESTAMP_AS_INT>,\
        }\
    ]
)

```

delete\_prompt( _prompt\_id_, _\*_, _force=False_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/prompts/prompt_template.html#PromptTemplateManager.delete_prompt) [¶](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.PromptTemplateManager.delete_prompt "Link to this definition")

Remove a prompt template from a project or space.

Parameters:

- **prompt\_id** ( _str_) – ID of the prompt template to be deleted

- **force** ( _bool_) – if True, then the prompt template is unlocked and then deleted, defaults to False.


Returns:

status ‘SUCCESS’ if the prompt template is successfully deleted

Return type:

str

**Example:**

```
prompt_mgr.delete_prompt(prompt_id)  # delete if asset is unlocked

```

get\_lock( _prompt\_id_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/prompts/prompt_template.html#PromptTemplateManager.get_lock) [¶](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.PromptTemplateManager.get_lock "Link to this definition")

Get the current locked state of a prompt template.

Parameters:

**prompt\_id** ( _str_) – ID of the prompt template

Returns:

information about the locked state of a prompt template asset

Return type:

dict

**Example:**

```
print(prompt_mgr.get_lock(prompt_id))

```

list( _\*_, _limit=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/prompts/prompt_template.html#PromptTemplateManager.list) [¶](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.PromptTemplateManager.list "Link to this definition")

List all available prompt templates in the DataFrame format.

Parameters:

**limit** ( _int_ _,_ _optional_) – limit number of fetched records, defaults to None.

Returns:

DataFrame of fundamental properties of available prompts.

Return type:

pandas.core.frame.DataFrame

**Example:**

```
prompt_mgr.list(limit=5)    # list of 5 recent created prompt template assets

```

Hint

Additionally you can sort available prompt templates by “LAST MODIFIED” field.

```
df_prompts = prompt_mgr.list()
df_prompts.sort_values("LAST MODIFIED", ascending=False)

```

load\_prompt( _prompt\_id_, _astype=PromptTemplateFormats.PROMPTTEMPLATE_, _\*_, _prompt\_variables=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/prompts/prompt_template.html#PromptTemplateManager.load_prompt) [¶](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.PromptTemplateManager.load_prompt "Link to this definition")

Retrieve a prompt template asset.

Parameters:

- **prompt\_id** ( _str_) – ID of the processed prompt template

- **astype** ( [_PromptTemplateFormats_](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.utils.enums.PromptTemplateFormats "ibm_watsonx_ai.foundation_models.utils.enums.PromptTemplateFormats")) – type of return object

- **prompt\_variables** ( _dict_ _\[_ _str_ _,_ _str_ _\]_) – dictionary of input variables and values that will replace the input variables


Returns:

prompt template asset

Return type:

[FreeformPromptTemplate](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.FreeformPromptTemplate "ibm_watsonx_ai.foundation_models.prompts.FreeformPromptTemplate") \| [PromptTemplate](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.PromptTemplate "ibm_watsonx_ai.foundation_models.prompts.PromptTemplate") \| [DetachedPromptTemplate](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.DetachedPromptTemplate "ibm_watsonx_ai.foundation_models.prompts.DetachedPromptTemplate") \| [ChatPrompt](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.ChatPrompt "ibm_watsonx_ai.foundation_models.prompts.ChatPrompt") \| str \| langchain.prompts.PromptTemplate

**Example:**

```
loaded_prompt_template = prompt_mgr.load_prompt(prompt_id)
loaded_prompt_template_lc = prompt_mgr.load_prompt(prompt_id, PromptTemplateFormats.LANGCHAIN)
loaded_prompt_template_string = prompt_mgr.load_prompt(prompt_id, PromptTemplateFormats.STRING)

```

lock( _prompt\_id_, _force=False_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/prompts/prompt_template.html#PromptTemplateManager.lock) [¶](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.PromptTemplateManager.lock "Link to this definition")

Lock a prompt template if it is unlocked and you have permission to lock it.

Parameters:

- **prompt\_id** ( _str_) – ID of the prompt template

- **force** ( _bool_) – if True, lock is forcefully overwritten


Returns:

locked prompt template

Return type:

dict

**Example:**

```
prompt_mgr.lock(prompt_id)

```

store\_prompt( _prompt\_template_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/prompts/prompt_template.html#PromptTemplateManager.store_prompt) [¶](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.PromptTemplateManager.store_prompt "Link to this definition")

Store a new prompt template.

Parameters:

**prompt\_template** ( _(_ [_FreeformPromptTemplate_](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.FreeformPromptTemplate "ibm_watsonx_ai.foundation_models.prompts.FreeformPromptTemplate") _\|_ [_PromptTemplate_](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.PromptTemplate "ibm_watsonx_ai.foundation_models.prompts.PromptTemplate") _\|_ [_DetachedPromptTemplate_](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.DetachedPromptTemplate "ibm_watsonx_ai.foundation_models.prompts.DetachedPromptTemplate") _\|_ [_ChatPrompt_](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.ChatPrompt "ibm_watsonx_ai.foundation_models.prompts.ChatPrompt") _\|_ _langchain.prompts.PromptTemplate_ _)_) – PromptTemplate to be stored.

Returns:

PromptTemplate object that is initialized with values provided in the server response object.

Return type:

[FreeformPromptTemplate](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.FreeformPromptTemplate "ibm_watsonx_ai.foundation_models.prompts.FreeformPromptTemplate") \| [PromptTemplate](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.PromptTemplate "ibm_watsonx_ai.foundation_models.prompts.PromptTemplate") \| [DetachedPromptTemplate](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.DetachedPromptTemplate "ibm_watsonx_ai.foundation_models.prompts.DetachedPromptTemplate") \| [ChatPrompt](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.ChatPrompt "ibm_watsonx_ai.foundation_models.prompts.ChatPrompt")

unlock( _prompt\_id_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/prompts/prompt_template.html#PromptTemplateManager.unlock) [¶](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.PromptTemplateManager.unlock "Link to this definition")

Unlock a prompt template if it is locked and you have permission to unlock it.

Parameters:

**prompt\_id** ( _str_) – ID of the prompt template

Returns:

unlocked prompt template

Return type:

dict

**Example:**

```
prompt_mgr.unlock(prompt_id)

```

update\_prompt( _prompt\_id_, _prompt\_template_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/prompts/prompt_template.html#PromptTemplateManager.update_prompt) [¶](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.PromptTemplateManager.update_prompt "Link to this definition")

Update prompt template data.

Parameters:

- **prompt\_id** ( _str_) – ID of the prompt template to be updated

- **prompt\_template** ( [_FreeformPromptTemplate_](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.FreeformPromptTemplate "ibm_watsonx_ai.foundation_models.prompts.FreeformPromptTemplate") _\|_ [_PromptTemplate_](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.PromptTemplate "ibm_watsonx_ai.foundation_models.prompts.PromptTemplate") _\|_ [_DetachedPromptTemplate_](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.DetachedPromptTemplate "ibm_watsonx_ai.foundation_models.prompts.DetachedPromptTemplate") _\|_ [_ChatPrompt_](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.ChatPrompt "ibm_watsonx_ai.foundation_models.prompts.ChatPrompt")) – prompt template with new data


Returns:

metadata of the updated deployment

Return type:

dict

**Example:**

```
updated_prompt_template = PromptTemplate(name="New name")
prompt_mgr.update_prompt(prompt_id, prompt_template)  # {'name': 'New name'} in metadata

```

_class_ ibm\_watsonx\_ai.foundation\_models.prompts.PromptTemplate( _name=None_, _model\_id=None_, _model\_params=None_, _template\_version=None_, _task\_ids=None_, _description=None_, _input\_text=None_, _input\_variables=None_, _instruction=None_, _input\_prefix=None_, _output\_prefix=None_, _examples=None_, _validate\_template=True_, _\*\*kwargs_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/prompts/prompt_template.html#PromptTemplate) [¶](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.PromptTemplate "Link to this definition")

Bases: `BasePromptTemplate`

Parameter storage for a structured prompt template.

Parameters:

- **prompt\_id** ( _str_ _,_ _attribute setting not allowed_) – ID of the prompt template, defaults to None.

- **created\_at** ( _str_ _,_ _attribute setting not allowed_) – time that the prompt was created (UTC), defaults to None.

- **lock** ( _PromptTemplateLock_ _\|_ _None_ _,_ _attribute setting not allowed_) – locked state of the asset, defaults to None.

- **is\_template** ( _bool_ _\|_ _None_ _,_ _attribute setting not allowed_) – True if the prompt is a template, False otherwise; defaults to None.

- **name** ( _str_ _,_ _optional_) – name of the prompt template, defaults to None.

- **model\_id** ( [_ModelTypes_](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.utils.enums.ModelTypes "ibm_watsonx_ai.foundation_models.utils.enums.ModelTypes") _\|_ _str_ _\|_ _None_ _,_ _optional_) – ID of the Foundation model, defaults to None.

- **model\_params** ( _dict_ _,_ _optional_) – parameters of the model, defaults to None.

- **template\_version** ( _str_ _,_ _optional_) – semantic version for tracking in IBM AI Factsheets, defaults to None.

- **task\_ids** ( _list_ _\[_ _str_ _\]_ _\|_ _None_ _,_ _optional_) – List of task IDs, defaults to None.

- **description** ( _str_ _,_ _optional_) – description of the prompt template asset, defaults to None.

- **input\_text** ( _str_ _,_ _optional_) – input text for the prompt, defaults to None.

- **input\_variables** ( _(_ _list_ _\|_ _dict_ _\[_ _str_ _,_ _dict_ _\[_ _str_ _,_ _str_ _\]_ _\]_ _)_ _,_ _optional_) – Input variables can be present in fields: instruction,
input\_prefix, output\_prefix, input\_text, examples
and are identified by braces (‘{’ and ‘}’), defaults to None.

- **instruction** ( _str_ _,_ _optional_) – instruction for the model, defaults to None.

- **input\_prefix** ( _str_ _,_ _optional_) – prefix string placed before the input text, defaults to None.

- **output\_prefix** ( _str_ _,_ _optional_) – prefix placed before the model response, defaults to None.

- **examples** ( _list_ _\[_ _list_ _\[_ _str_ _\]_ _\]_ _,_ _optional_) – examples that might help the model adjust the response; \[\[input1, output1\], …\], defaults to None.

- **validate\_template** ( _bool_ _,_ _optional_) – if True, the prompt template is validated for the presence of input variables, defaults to True.


Raises:

**ValidationError** – raised when the set of input\_variables is not consistent with the input variables present in the template.
Raised only when validate\_template is set to True.

**Examples**

Example of an invalid prompt template:

```
prompt_template = PromptTemplate(
    name="My structured prompt",
    model_id="ibm/granite-13b-chat-v2"
    input_text='What are the most famous monuments in ?',
    input_variables=['country']
)

# Traceback (most recent call last):
#     ...
# ValidationError: Invalid prompt template; check for mismatched or missing input variables. Missing input variable: {'country'}

```

Example of a valid prompt template:

```
prompt_template = PromptTemplate(
    name="My structured prompt",
    model_id="ibm/granite-13b-chat-v2"
    input_text='What are the most famous monuments in {country}?',
    input_variables=['country']
)

```

_class_ ibm\_watsonx\_ai.foundation\_models.prompts.FreeformPromptTemplate( _name=None_, _model\_id=None_, _model\_params=None_, _template\_version=None_, _task\_ids=None_, _description=None_, _input\_text=None_, _input\_variables=None_, _validate\_template=True_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/prompts/prompt_template.html#FreeformPromptTemplate) [¶](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.FreeformPromptTemplate "Link to this definition")

Bases: `BasePromptTemplate`

Storage for Freeform prompt template asset parameters.

Parameters:

- **prompt\_id** ( _str_ _,_ _attribute setting not allowed_) – ID of the prompt template, defaults to None.

- **created\_at** ( _str_ _,_ _attribute setting not allowed_) – time that the prompt was created (UTC), defaults to None.

- **lock** ( _PromptTemplateLock_ _\|_ _None_ _,_ _attribute setting not allowed_) – locked state of the asset, defaults to None.

- **is\_template** ( _bool_ _\|_ _None_ _,_ _attribute setting not allowed_) – True if the prompt is a template, False otherwise; defaults to None.

- **name** ( _str_ _,_ _optional_) – name of the prompt template, defaults to None.

- **model\_id** ( [_ModelTypes_](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.utils.enums.ModelTypes "ibm_watsonx_ai.foundation_models.utils.enums.ModelTypes") _\|_ _str_ _\|_ _None_ _,_ _optional_) – ID of the foundation model, defaults to None.

- **model\_params** ( _dict_ _,_ _optional_) – parameters of the model, defaults to None.

- **template\_version** ( _str_ _,_ _optional_) – semantic version for tracking in IBM AI Factsheets, defaults to None.

- **task\_ids** ( _list_ _\[_ _str_ _\]_ _\|_ _None_ _,_ _optional_) – list of task IDs, defaults to None.

- **description** ( _str_ _,_ _optional_) – description of the prompt template asset, defaults to None.

- **input\_text** ( _str_ _,_ _optional_) – input text for the prompt, defaults to None.

- **input\_variables** ( _(_ _list_ _\|_ _dict_ _\[_ _str_ _,_ _dict_ _\[_ _str_ _,_ _str_ _\]_ _\]_ _)_ _,_ _optional_) – input variables can be present in field input\_text
and are identified by braces (‘{’ and ‘}’), defaults to None.

- **validate\_template** ( _bool_ _,_ _optional_) – if True, the prompt template is validated for the presence of input variables, defaults to True.


Raises:

**ValidationError** – raised when the set of input\_variables is not consistent with the input variables present in the template.
Raised only when validate\_template is set to True.

**Examples**

Example of an invalid Freeform prompt template:

```
prompt_template = FreeformPromptTemplate(
    name="My freeform prompt",
    model_id="ibm/granite-13b-chat-v2",
    input_text='What are the most famous monuments in ?',
    input_variables=['country']
)

# Traceback (most recent call last):
#    ...
# ValidationError: Invalid prompt template; check for mismatched or missing input variables. Missing input variable: {'country'}

```

Example of a valid Freeform prompt template:

```
prompt_template = FreeformPromptTemplate(
    name="My freeform prompt",
    model_id="ibm/granite-13b-chat-v2"
    input_text='What are the most famous monuments in {country}?',
    input_variables=['country']
)

```

_class_ ibm\_watsonx\_ai.foundation\_models.prompts.DetachedPromptTemplate( _name=None_, _model\_id=None_, _model\_params=None_, _template\_version=None_, _task\_ids=None_, _description=None_, _input\_text=None_, _input\_variables=None_, _detached\_prompt\_id=None_, _detached\_model\_id=None_, _detached\_model\_provider=None_, _detached\_prompt\_url=None_, _detached\_prompt\_additional\_information=None_, _detached\_model\_name=None_, _detached\_model\_url=None_, _validate\_template=True_, _instruction=None_, _input\_prefix=None_, _output\_prefix=None_, _examples=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/prompts/prompt_template.html#DetachedPromptTemplate) [¶](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.DetachedPromptTemplate "Link to this definition")

Bases: `BasePromptTemplate`

Storage for detached prompt template parameters.

Parameters:

- **prompt\_id** ( _str_ _,_ _attribute setting not allowed_) – ID of the prompt template, defaults to None.

- **created\_at** ( _str_ _,_ _attribute setting not allowed_) – time that the prompt was created (UTC), defaults to None.

- **lock** ( _PromptTemplateLock_ _\|_ _None_ _,_ _attribute setting not allowed_) – locked state of the asset, defaults to None.

- **is\_template** ( _bool_ _\|_ _None_ _,_ _attribute setting not allowed_) – True if the prompt is a template, False otherwise; defaults to None.

- **name** ( _str_ _,_ _optional_) – name of the prompt template, defaults to None.

- **model\_id** ( [_ModelTypes_](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.utils.enums.ModelTypes "ibm_watsonx_ai.foundation_models.utils.enums.ModelTypes") _\|_ _str_ _\|_ _None_ _,_ _optional_) – ID of the foundation model, defaults to None.

- **model\_params** ( _dict_ _,_ _optional_) – parameters of the model, defaults to None.

- **template\_version** ( _str_ _,_ _optional_) – semantic version for tracking in IBM AI Factsheets, defaults to None.

- **task\_ids** ( _list_ _\[_ _str_ _\]_ _\|_ _None_ _,_ _optional_) – list of task IDs, defaults to None.

- **description** ( _str_ _,_ _optional_) – description of the prompt template asset, defaults to None.

- **input\_text** ( _str_ _,_ _optional_) – input text for the prompt, defaults to None.

- **input\_variables** ( _(_ _list_ _\|_ _dict_ _\[_ _str_ _,_ _dict_ _\[_ _str_ _,_ _str_ _\]_ _\]_ _)_ _,_ _optional_) – input variables can be present in field: input\_text
and are identified by braces (‘{’ and ‘}’), defaults to None.

- **detached\_prompt\_id** ( _str_ _\|_ _None_ _,_ _optional_) – ID of the external prompt, defaults to None

- **detached\_model\_id** ( _str_ _\|_ _None_ _,_ _optional_) – ID of the external model, defaults to None

- **detached\_model\_provider** ( _str_ _\|_ _None_ _,_ _optional_) – external model provider, defaults to None

- **detached\_prompt\_url** ( _str_ _\|_ _None_ _,_ _optional_) – URL for the external prompt, defaults to None

- **detached\_prompt\_additional\_information** ( _list_ _\[_ _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\]_ _\|_ _None_ _,_ _optional_) – additional information of the external prompt, defaults to None

- **detached\_model\_name** ( _str_ _\|_ _None_ _,_ _optional_) – name of the external model, defaults to None

- **detached\_model\_url** ( _str_ _\|_ _None_ _,_ _optional_) – URL for the external model, defaults to None

- **validate\_template** ( _bool_ _,_ _optional_) – if True, the prompt template is validated for the presence of input variables, defaults to True

- **instruction** ( _str_ _,_ _optional_) – instruction for the model, defaults to None

- **input\_prefix** ( _str_ _,_ _optional_) – prefix string placed before the input text, defaults to None

- **output\_prefix** ( _str_ _,_ _optional_) – prefix placed before the model response, defaults to None

- **examples** ( _list_ _\[_ _list_ _\[_ _str_ _\]_ _\]_ _,_ _optional_) – examples that might help the model adjust the response; \[\[input1, output1\], …\], defaults to None


Raises:

**ValidationError** – raised when the set of input\_variables is not consistent with the input variables present in the template.
Raised only when validate\_template is set to True.

**Examples**

Example of an invalid detached prompt template:

```
prompt_template = DetachedPromptTemplate(
    name="My detached prompt",
    model_id="<some model>",
    input_text='What are the most famous monuments in ?',
    input_variables=['country'],
    detached_prompt_id="<prompt id>",
    detached_model_id="<model id>",
    detached_model_provider="<provider>",
    detached_prompt_url="<url>",
    detached_prompt_additional_information=[{"key":"value"}],
    detached_model_name="<model name>",
    detached_model_url ="<model url>"
)

# Traceback (most recent call last):
#     ...
# ValidationError: Invalid prompt template; check for mismatched or missing input variables. Missing input variable: {'country'}

```

Example of a valid detached prompt template:

```
prompt_template = DetachedPromptTemplate(
    name="My detached prompt",
    model_id="<some model>",
    input_text='What are the most famous monuments in {country}?',
    input_variables=['country'],
    detached_prompt_id="<prompt id>",
    detached_model_id="<model id>",
    detached_model_provider="<provider>",
    detached_prompt_url="<url>",
    detached_prompt_additional_information=[{"key":"value"}],
    detached_model_name="<model name>",
    detached_model_url ="<model url>"
)

```

_class_ ibm\_watsonx\_ai.foundation\_models.prompts.ChatPrompt( _name=None_, _model\_id=None_, _model\_params=None_, _prompt\_version=None_, _task\_ids=None_, _description=None_, _chat\_items=None_, _system\_prompt=None_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/prompts/chat_prompt.html#ChatPrompt) [¶](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.ChatPrompt "Link to this definition")

Bases: `BasePrompt`

Storage for chat prompt parameters.

Parameters:

- **prompt\_id** ( _str_ _,_ _attribute setting not allowed_) – ID of the prompt, defaults to None.

- **created\_at** ( _str_ _,_ _attribute setting not allowed_) – time that the prompt was created (UTC), defaults to None.

- **lock** ( _PromptTemplateLock_ _\|_ _None_ _,_ _attribute setting not allowed_) – locked state of the asset, defaults to None.

- **is\_template** ( _bool_ _\|_ _None_ _,_ _attribute setting not allowed_) – True if the prompt is a template, False otherwise; defaults to None.

- **name** ( _str_ _,_ _optional_) – name of the prompt, defaults to None.

- **model\_id** ( [_ModelTypes_](https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.utils.enums.ModelTypes "ibm_watsonx_ai.foundation_models.utils.enums.ModelTypes") _\|_ _str_ _\|_ _None_ _,_ _optional_) – ID of the foundation model, defaults to None.

- **model\_params** ( _dict_ _,_ _optional_) – parameters of the model, defaults to None.

- **prompt\_version** ( _str_ _,_ _optional_) – semantic version for tracking in IBM AI Factsheets, defaults to None.

- **task\_ids** ( _list_ _\[_ _str_ _\]_ _\|_ _None_ _,_ _optional_) – list of task IDs, defaults to None.

- **description** ( _str_ _,_ _optional_) – description of the prompt asset, defaults to None.

- **chat\_items** ( _list_ _\[_ _dict_ _\]_ _,_ _optional_) – chat items, defaults to None.

- **system\_prompt** ( _str_ _,_ _optional_) – system prompt used by model, defaults to None.


**Examples**

Example of a valid chat prompt:

```
prompt = ChatPrompt(
    name="My chat prompt",
    model_id="<some model>",
    system_prompt="system prompt"
)

```

_property_ prompt\_version [¶](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.prompts.ChatPrompt.prompt_version "Link to this definition")

## Enums [¶](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html\#enums "Link to this heading")

_class_ ibm\_watsonx\_ai.foundation\_models.utils.enums.PromptTemplateFormats( _value_) [\[source\]](https://ibm.github.io/watsonx-ai-python-sdk/_modules/ibm_watsonx_ai/foundation_models/utils/enums.html#PromptTemplateFormats) [¶](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.utils.enums.PromptTemplateFormats "Link to this definition")

Bases: `Enum`

Supported formats of loaded prompt template.

LANGCHAIN _='langchain'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.utils.enums.PromptTemplateFormats.LANGCHAIN "Link to this definition")PROMPTTEMPLATE _='prompt'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.utils.enums.PromptTemplateFormats.PROMPTTEMPLATE "Link to this definition")STRING _='string'_ [¶](https://ibm.github.io/watsonx-ai-python-sdk/prompt_template_manager.html#ibm_watsonx_ai.foundation_models.utils.enums.PromptTemplateFormats.STRING "Link to this definition")