ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_langchain.html#furo-main-content)

[Back to top](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_langchain.html#)

[View this page](https://ibm.github.io/watsonx-ai-python-sdk/_sources/fm_extensions_langchain.rst.txt "View this page")

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# LangChain [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_langchain.html\#langchain "Link to this heading")

IBM integration with LangChain is available under [IBM and LangChain integration documentation](https://python.langchain.com/docs/integrations/providers/ibm).

Note

The `langchain_ibm==0.3.x` package relies on version `0.3.x` of the `langchain_core` package.

For detailed migration instructions, please refer to the documentation [LangChain v0.3](https://python.langchain.com/docs/versions/v0_3/)

## Installation and Setup [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_langchain.html\#installation-and-setup "Link to this heading")

Install the integration package with

```
pip install -qU langchain-ibm

```

Get an IBM watsonx.ai api key and set it as an environment variable ( `WATSONX_APIKEY`)

```
import os

os.environ["WATSONX_APIKEY"] = "your IBM watsonx.ai api key"

```

## Chat Model [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_langchain.html\#chat-model "Link to this heading")

See a [usage example of Chat Model](https://python.langchain.com/docs/integrations/chat/ibm_watsonx/)

```
from langchain_ibm import ChatWatsonx

```

## LLMs [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_langchain.html\#llms "Link to this heading")

See a [usage example of LLMs](https://python.langchain.com/docs/integrations/llms/ibm_watsonx/)

```
from langchain_ibm import WatsonxLLM

```

## Embedding Models [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_langchain.html\#embedding-models "Link to this heading")

See a [usage example of Embedding Models](https://python.langchain.com/docs/integrations/text_embedding/ibm_watsonx/)

```
from langchain_ibm import WatsonxEmbeddings

```

## Rerank [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_langchain.html\#rerank "Link to this heading")

See a [usage example of Rerank](https://python.langchain.com/docs/integrations/retrievers/ibm_watsonx_ranker/)

```
from langchain_ibm import WatsonxRerank

```

## API reference [¶](https://ibm.github.io/watsonx-ai-python-sdk/fm_extensions_langchain.html\#api-reference "Link to this heading")

For detailed documentation of all IBM watsonx.ai features and configurations head to the API reference: [langchain-ibm](https://python.langchain.com/api_reference/ibm/index.html)