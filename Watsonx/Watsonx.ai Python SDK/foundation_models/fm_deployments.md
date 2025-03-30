ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://ibm.github.io/watsonx-ai-python-sdk/fm_deployments.html#furo-main-content)

[Back to top](https://ibm.github.io/watsonx-ai-python-sdk/fm_deployments.html#)

[View this page](https://ibm.github.io/watsonx-ai-python-sdk/_sources/fm_deployments.rst.txt "View this page")

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# `ModelInference` for Deployments [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_deployments.html\#modelinference-for-deployments "Link to this heading")

This section shows how to use the ModelInference module with a created deployment.

You can infer text in one of two ways:

- the [deployments](https://ibm.github.io/watsonx-ai-python-sdk/pt_model_inference.html#generate-text-deployments) module

- the [ModelInference](https://ibm.github.io/watsonx-ai-python-sdk/pt_model_inference.html#generate-text-modelinference) module


## Infer text with deployments [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_deployments.html\#infer-text-with-deployments "Link to this heading")

You can directly query `generate_text` using the deployments module.

```
client.deployments.generate_text(
    prompt="Example prompt",
    deployment_id=deployment_id)

```

## Creating `ModelInference` instance [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_deployments.html\#creating-modelinference-instance "Link to this heading")

Start by defining the parameters. They will later be used by the module.

```
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

generate_params = {
    GenParams.MAX_NEW_TOKENS: 25,
    GenParams.STOP_SEQUENCES: ["\n"]
}

```

Create the ModelInference by using credentials and `project_id` / `space_id`, or the previously initialized APIClient (see [APIClient initialization](https://ibm.github.io/watsonx-ai-python-sdk/pt_model_inference.html#api-client-init)).

```
from ibm_watsonx_ai.foundation_models import ModelInference

deployed_model = ModelInference(
    deployment_id=deployment_id,
    params=generate_params,
    credentials=credentials,
    project_id=project_id
)

# OR

deployed_model = ModelInference(
    deployment_id=deployment_id,
    params=generate_params,
    api_client=client
)

```

You can directly query `generate_text` using the `ModelInference` object.

```
deployed_model.generate_text(prompt="Example prompt")

```

## Generate methods [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_deployments.html\#generate-methods "Link to this heading")

A detailed explanation of available generate methods with exact parameters can be found in the [ModelInferece class](https://ibm.github.io/watsonx-ai-python-sdk/fm_model_inference.html#model-inference-class).

With the previously created `deployed_model` object, it is possible to generate a text stream (generator) using a defined inference and the `generate_text_stream()` method.

```
for token in deployed_model.generate_text_stream(prompt=input_prompt):
    print(token, end="")
'$10 Powerchill Leggings'

```

And also receive more detailed result with `generate()`.

```
details = deployed_model.generate(prompt=input_prompt, params=gen_params)
print(details)
{
    'model_id': 'google/flan-t5-xl',
    'created_at': '2023-11-17T15:32:57.401Z',
    'results': [\
        {\
        'generated_text': '$10 Powerchill Leggings',\
        'generated_token_count': 8,\
        'input_token_count': 73,\
        'stop_reason': 'eos_token'\
        }\
    ],
    'system': {'warnings': []}
}

```