ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_llamaindex.html#furo-main-content)

[Back to top](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_llamaindex.html#)

[View this page](https://ibm.github.io/watsonx-ai-python-sdk/_sources/fm_extensions_llamaindex.rst.txt "View this page")

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# LlamaIndex [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_llamaindex.html\#llamaindex "Link to this heading")

IBM integration with LlamaIndex is available under [IBM and LlamaIndex LLM integration documentation](https://docs.llamaindex.ai/en/stable/examples/llm/ibm_watsonx/), while for embedding integration you may visit [IBM and LlamaIndex Embedding integration documentation](https://docs.llamaindex.ai/en/stable/examples/embeddings/ibm_watsonx/).

Note

The `llama-index-llms-ibm==0.2.x` package relies on version `0.11.x` of the `llama-index-core` package and `ibm_watsonx_ai` in version `>=1.1.x`.

## Installation and Setup [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_llamaindex.html\#installation-and-setup "Link to this heading")

Install the integration package with

```
pip install -qU llama-index-llms-ibm

```

Get an IBM watsonx.ai api key and set it as an environment variable ( `WATSONX_APIKEY`)

```
import os

os.environ["WATSONX_APIKEY"] = watsonx_api_key

```

## LLMs [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_llamaindex.html\#llms "Link to this heading")

See detailed example how to load a model in the following [link](https://docs.llamaindex.ai/en/stable/examples/llm/ibm_watsonx/#load-the-model)

```
from llama_index.llms.ibm import WatsonxLLM

```

## Embedding Models [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_llamaindex.html\#embedding-models "Link to this heading")

Install the integration package with

```
pip install -qU llama-index-embeddings-ibm

```

Note

The `llama-index-embeddings-ibm==0.1.x` package relies on version `0.11.x` of the `llama-index-core` package and `ibm_watsonx_ai` in version `>=1.0.x`.

Usage example:

```
from llama_index.embeddings.ibm import WatsonxEmbeddings

```

More details can be found [here](https://docs.llamaindex.ai/en/stable/examples/embeddings/ibm_watsonx/)

## API reference [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_llamaindex.html\#api-reference "Link to this heading")

For detailed documentation of all IBM watsonx.ai features and configurations head to the [API reference](https://docs.llamaindex.ai/en/stable/api_reference/llms/ibm/)