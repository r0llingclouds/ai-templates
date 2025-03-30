# AI Templates Repository

This repository contains a collection of code templates, snippets, and SDK docs for AI projects. It is code I created during my previous projects and has some reusability.

## Overview

This repository serves as a central location for reusable code patterns across different AI domains, including:

- Retrieval Augmented Generation (RAG)
- Agent-based systems with BeeAI
- OpenAI API integration
- Document processing and extraction
- Vector database integration

## Repository Structure

```
ai-templates/
├── Agents                    # Agent-based systems and frameworks
│   └── BeeAI                 # BeeAI framework examples
├── OpenAI                    # OpenAI API integration templates
│   └── OpenAI Responses API  # Responses API documentation and examples
├── Retrieval augmented generation      # RAG implementation examples
│   ├── Advanced techniques             # Enhanced RAG techniques
│   ├── Document processors             # Document parsing and chunking
│   ├── Elastic search                  # Elasticsearch integration
│   └── Milvus                          # Milvus integration
└── Watsonx                   # WatsonX AI platform integration
    └── Watsonx.ai Python SDK # WatsonX Python SDK documentation
```

## Components

### Agents & BeeAI Framework

The BeeAI framework provides tools for building agent-based systems with LLMs. Key examples include:

- **Basic agents**: Foundation for building AI agents (`basics_notebook.py`)
- **ReAct agents**: Implementation of the ReAct (Reasoning and Acting) pattern (`agents_notebook.py`)
- **Travel agent example**: Complete agent implementation for travel recommendations (`travel-agent-notebook.py`/`.ipynb`)
- **Workflow implementation**: Process orchestration with BeeAI (`workflows_notebook.py`)
- **WatsonX integration**: Connecting BeeAI with WatsonX models (`watsonx_notebook.py`)

### OpenAI Integration

Documentation and examples for the OpenAI Responses API, covering:

- **Built-in tools**: Leverage OpenAI's built-in capabilities
- **Conversation state**: Managing multi-turn conversations
- **File search**: Retrieve information from uploaded files
- **Function calling**: Enable models to call your code
- **Images and vision**: Process and analyze images
- **Structured outputs**: Generate responses in specific formats
- **Text generation and prompting**: Core text generation capabilities
- **Web search**: Integrate web search functionality

### Retrieval Augmented Generation (RAG)

Templates and implementations for RAG systems, including:

#### Document Processors
- **MarkdownProcessor**: Process and chunk markdown documents
- **PDFChunker**: Extract and segment text from PDFs
- **PyMuPDFProcessor**: Alternative PDF processing with PyMuPDF
- **UnstructuredProcessor**: General document processing

#### Vector Databases
- **Elasticsearch integration**: Full implementation using Elasticsearch
- **Milvus integration**: Alternative implementation with Milvus

#### Advanced Techniques
- **Contextual Retrieval**: Enhance retrieval with contextually relevant questions

### WatsonX Integration

Documentation for the WatsonX.ai Python SDK, including:

- Base functionality
- Connection management
- Foundation models
- Extension frameworks

## Getting Started

### Prerequisites

This repository contains templates for different frameworks. Depending on the specific template, you'll need:

- Python 3.8+ 
- Required Python packages in the respective `requirements.txt` files

### Environment Setup

Most examples require API keys or other credentials. Set these up in a `.env` file based on the provided `env_example` files.

For WatsonX examples:
```
WATSONX_API_KEY=your_api_key
WATSONX_PROJECT_ID=your_project_id
WATSONX_URL=your_url
```

For Elasticsearch examples:
```
ELASTIC_URL=your_elastic_url
ELASTIC_USER=your_username
ELASTIC_PASSWORD=your_password
```

For Milvus examples:
```
MILVUS_HOST=localhost
MILVUS_PORT=19530
```

### Running Examples

Most examples are provided as Python scripts (`.py`) or Jupyter notebooks (`.ipynb`). To run:

1. Install the required dependencies
2. Set up your environment variables
3. Execute the example file:
   - For Python scripts: `python example.py`
   - For Jupyter notebooks: Open in Jupyter Lab/Notebook and run cells

## Key Technologies

- **BeeAI**: Framework for building AI agents
- **WatsonX.ai**: IBM's AI platform with language models and embeddings
- **OpenAI APIs**: Various OpenAI APIs, particularly the Responses API
- **Vector Databases**: Elasticsearch and Milvus
- **Document Processing Libraries**: PyMuPDF, PDF-Chunker, Unstructured

## Use Cases

These templates can be used for:

- Building conversational AI agents
- Implementing knowledge retrieval systems
- Processing and extracting information from documents
- Creating domain-specific assistants
- Developing travel recommendation systems
- Implementing question-answering systems over custom data

## Contributing

Feel free to add new templates or improve existing ones. Create a pull request with your changes or additions.

## License

[Specify your license information here]
