# ADR Research Workspace

GADR is a research-focused repository for generating Architecture Decision Records (ADRs)
from real meeting transcripts. It compares multiple prompting strategies and an agentic
RAG pipeline, then evaluates output quality against a curated ADR dataset.

## Data Origins and Folders

- `adrs_json/`: JSON list files sourced from https://github.com/software-competence-center-hagenberg/ADR-Study-Dataset.
- `downloaded_adrs/`: ADRs downloaded via GitHub API requests using the repositories listed in `adrs_json/`.
- `dataset_adrs/`: Consolidated ADR dataset (each repository folder moved into a single folder).
- `chroma_db/`: Vector database (Chroma) built from `dataset_adrs/`.
- `evaluation/`: Form evaluation results (CSV) and the senior evaluation.
- `generated/`: Generated ADRs by three approaches; each approach folder has 3 rounds to validate deterministic behavior.
- `transcriptions/`: Real student meeting transcriptions.

## Technologies Used

- Google Gemini (Gemini 3.1 Pro using Vertex AI API from Google) for ADR generation.
- Tavily for web search augmentation.
- LangGraph for agentic/RAG orchestration.
- ChromaDB for vector storage and retrieval.

## Python Setup (venv)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

If you prefer, deactivate with:

```bash
deactivate
```

## Environment Variables

This repo includes a sample env file you can copy and fill in.

```bash
cp .env.example .env
```

Then edit `.env` with your API keys and load it before running scripts.

```bash
source .env
```

If you prefer loading inside Python, install `python-dotenv` and call `load_dotenv()`.

## How to Run

All scripts are Python files exported from Colab notebooks. They rely on a transcript defined in `constants.py` and may call external APIs (Google Gemini and Tavily). Update API keys or move them to environment variables before running.

```bash
python3 few_shot_adr.py
python3 zero_shot_adr.py
python3 research_agent_adr.py
```

## File Guide

- `constants.py`: Central place for the meeting transcript text used by the approaches.
- `few_shot_adr.py`: Prompt-engineering, few-shot approach to generate ADRs from the transcript.
- `zero_shot_adr.py`: Prompt-engineering, zero-shot approach to generate ADRs from the transcript.
- `research_agent_adr.py`: Agentic RAG pipeline; ingests `dataset_adrs/` into Chroma and uses retrieval + web search to support ADR generation.
- `requirements.txt`: Python dependencies for all approaches.
