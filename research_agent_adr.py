from typing import TypedDict, Annotated
from dotenv import load_dotenv
from google import genai
import os
import constants
import chromadb
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_tavily import TavilySearch, tavily_search
import re
import json
import datetime
import operator
from langgraph.graph import StateGraph, START, END
from langgraph.types import Send

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

client = genai.Client(api_key=gemini_api_key, vertexai=True)

client = chromadb.PersistentClient(path="./chroma_db")

# # Delete existing collection to start fresh if you re-run this cell
# try:
#     client.delete_collection(name='adr_md')
# except:
#     pass

collection = client.get_or_create_collection(name="adr_md")

# Define headers to split on
headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]
splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)


def ingest_from_sample_data(folder_path="./dataset_adrs"):
    """
    Targets the sample_data folder and ingests all .md files found.
    """
    if not os.path.exists(folder_path):
        print(f"Error: Folder {folder_path} not found.")
        return

    # Filter for markdown files specifically
    files_to_process = [f for f in os.listdir(folder_path) if f.endswith(".md")]

    if not files_to_process:
        print(f"No markdown files found in {folder_path}.")
        return

    print(f"Found {len(files_to_process)} markdown files. Starting ingestion...")

    for filename in files_to_process:
        file_path = os.path.join(folder_path, filename)

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Split based on Markdown headers
        sections = splitter.split_text(content)

        if not sections:
            continue

        documents = [s.page_content for s in sections]
        metadatas = [{"source": filename, **s.metadata} for s in sections]
        ids = [f"{filename}_{i}" for i in range(len(sections))]

        collection.add(documents=documents, metadatas=metadatas, ids=ids)
        print(f"Ingested {len(sections)} chunks from: {filename}")


# ingest_from_sample_data() # Uncomment to run ingestion, and update collection with ADRs  from the dataset_adrs folder


def get_model_response(prompt, model_name="gemini-3-flash-preview"):
    response = client.models.generate_content(model=model_name, contents=prompt)
    return response.text


class GraphState(TypedDict):
    original_transcript: str
    transcript_en: str
    language: str
    current_date: str
    decisions: list
    critique: str  # feedback from the critique node
    iteration: int  # loop counter
    adrs: Annotated[list, operator.add]


def language_detector_node(state: GraphState):
    print("--- DETECTING LANGUAGE---")
    text = state["original_transcript"]

    # Take a 1000-character sample starting a bit further into the text.
    start_idx = min(1000, len(text) // 3)
    sample_text = text[start_idx : start_idx + 1000]

    # Instruct the model to ignore headers and focus on the dialogue
    prompt = (
        "Is the spoken dialogue in the following meeting transcript primarily in English? "
        "Ignore system headers, timestamps, metadata, or tool summaries. Focus strictly on the human conversation. "
        "Respond only with 'yes' or 'no'.\n\n"
        f"Text Sample:\n{sample_text}"
    )
    res = (
        get_model_response(prompt, model_name="gemini-3.1-pro-preview").strip().lower()
    )

    return {"language": "en" if "yes" in res else "other"}


def translate_node(state: GraphState):
    print("---TRANSLATING TRANSCRIPT---")
    prompt = (
        "Translate this meeting transcript to English. "
        "Output ONLY the translation, nothing else.\n\n"
        f"TRANSCRIPT:\n{state['original_transcript']}"
    )
    return {
        "transcript_en": get_model_response(prompt, model_name="gemini-3-flash-preview")
    }


def passthrough_en_node(state: GraphState):
    print("---ENGLISH DETECTED, SKIPPING TRANSLATION---")
    return {"transcript_en": state["original_transcript"]}


def language_router(state: GraphState):
    return "Translate" if state["language"] == "other" else "Passthrough_EN"


def extract_decisions_node(state: GraphState):
    iteration = state.get("iteration", 0) + 1
    text = state["transcript_en"]
    critique = state.get("critique", "")
    previous = state.get("decisions", [])
    previous_extraction = json.dumps(
        [{"summary": d["summary"], "relevant_context": d["context"]} for d in previous],
        indent=2,
    )

    print(f"---🔎 EXTRACTING DECISIONS (iteration {iteration})---")

    if iteration == 1:
        # ── FIRST PASS: extract from scratch ─────────────────────
        prompt = f"""You are a Senior Software Architect analyzing a meeting transcript.

Identify the architectural and technical decisions that DIRECTLY IMPACT how the
project is built, deployed, structured, or operated.

For each decision, extract:
- summary: one sentence describing the committed choice
- relevant_context: verbatim excerpt(s) from the transcript where this is discussed

GUIDELINES FOR GROUPING:
- A decision and its rejected alternative belong to the SAME decision
  (e.g., "chose GOV.BR auth" and "rejected Google Auth" = one decision about
  Authentication Strategy, not two separate decisions).
- Decisions about the same domain that cannot exist independently should be ONE decision
  (e.g., "adopt data standard X" + "core entity is Y within that standard" = one
  decision about Data Modeling).
- A high-level scope summary that merely restates other individual decisions is NOT
  its own decision. Distribute that context into the relevant individual decisions.
- Decisions about DIFFERENT architectural concerns MUST stay separate even if discussed
  in the same conversation segment.

EXCLUDE:
- Meta-conversation (meeting logistics, documentation tools, recording methods)
- Teaching moments with no project choice attached
- Vague intentions without team commitment ("maybe someday...")

TRANSCRIPT:
{text}

Respond in strict JSON (no markdown fences):
[
  {{"summary": "...", "relevant_context": "..."}},
  ...
]"""

    else:
        # ── REFINEMENT PASS: adjust based on critique ────────────
        prompt = f"""You are a Senior Software Architect. You previously extracted these
decisions from a meeting transcript, but a review found issues.

PREVIOUS EXTRACTION:
{previous_extraction}

CRITIQUE / ISSUES FOUND:
{critique}

ORIGINAL TRANSCRIPT:
{text}

Based on the critique, produce a CORRECTED list of decisions. You may:
- MERGE decisions that the critique says are overlapping or part of the same concern
- SPLIT decisions that the critique says bundle unrelated concerns
- REMOVE decisions that the critique identifies as non-project-impacting
- ADD decisions that the critique says were missed
- KEEP decisions the critique marked as correct (do not change them)

GUIDELINES FOR GROUPING:
- A decision and its rejected alternative = ONE decision
- Tightly coupled domain decisions = ONE decision
- Scope summaries that restate others = ABSORB, not standalone
- Different architectural concerns = SEPARATE decisions

Respond in strict JSON (no markdown fences):
[
  {{"summary": "...", "relevant_context": "..."}},
  ...
]"""

    res = get_model_response(prompt, model_name="gemini-3.1-pro-preview")
    cleaned = re.sub(r"```json\s*|```", "", res).strip()
    raw = json.loads(cleaned)

    decisions = [
        {
            "id": i + 1,
            "summary": d["summary"],
            "context": d["relevant_context"],
        }
        for i, d in enumerate(raw)
    ]

    print(f"   Extracted {len(decisions)} decision(s)")
    for d in decisions:
        print(f"   • {d['summary']}")

    return {"decisions": decisions, "iteration": iteration}


def critique_decisions_node(state: GraphState):
    """Reviews extracted decisions for quality issues."""
    decisions = state["decisions"]
    text = state["transcript_en"]
    iteration = state.get("iteration", 1)
    decisions_json = json.dumps(
        [{"id": d["id"], "summary": d["summary"]} for d in decisions], indent=2
    )

    print(f"---CRITIQUING DECISIONS (iteration {iteration})---")

    prompt = f"""You are a Principal Software Architect reviewing a set of extracted
decisions from a meeting transcript. Your job is to find QUALITY ISSUES.

EXTRACTED DECISIONS:
{decisions_json}

ORIGINAL TRANSCRIPT (for reference):
{text}

Evaluate the extraction against these criteria:

1. OVERLAP CHECK: Are any two decisions actually part of the same architectural concern?
   Example problem: "Chose GOV.BR auth" and "Rejected Google Auth" listed separately
   when they should be one "Authentication Strategy" decision.

2. FRAGMENTATION CHECK: Are decisions split too granularly? Each ADR should represent
   a meaningful, self-contained architectural choice, not a sub-detail of another.

3. MISSING CHECK: Are there real architectural decisions in the transcript that were
   NOT captured? Scan the transcript for technology choices, pattern selections,
   infrastructure commitments, or trade-off resolutions that are absent from the list.

4. NOISE CHECK: Are any extracted decisions actually meta-conversation, process remarks,
   documentation choices, or vague intentions rather than project-impacting commitments?

5. SCOPE CHECK: Are any decisions just high-level summaries that restate what other
   individual decisions already cover?

Respond in strict JSON (no markdown fences):
{{
  "status": "PASS" or "REFINE",
  "issues": [
    {{
      "type": "OVERLAP" | "FRAGMENTATION" | "MISSING" | "NOISE" | "SCOPE_DUPLICATE",
      "decision_ids": [list of affected decision ids, empty for MISSING],
      "description": "what's wrong and what to do about it"
    }},
    ...
  ],
  "summary": "one sentence overall assessment"
}}

Rules:
- If there are NO issues at all, return {{"status": "PASS", "issues": [], "summary": "..."}}.
- Be strict but fair. Do not invent problems. Only flag genuine quality issues.
- Minor wording improvements are NOT issues. Focus on structural problems.
- Between 4 and 9 decisions is a healthy range for a substantial meeting. Do NOT flag
  the count as a problem if it falls in this range and each is genuinely distinct."""

    res = get_model_response(prompt, model_name="gemini-3.1-pro-preview")
    cleaned = re.sub(r"```json\s*|```", "", res).strip()
    critique_data = json.loads(cleaned)

    status = critique_data.get("status", "PASS")
    issues = critique_data.get("issues", [])
    summary = critique_data.get("summary", "")

    print(f"   Status: {status}")
    print(f"   Summary: {summary}")
    for issue in issues:
        print(f"ISSUE: [{issue['type']}] {issue['description']}")

    # Store the full critique as a string for the refinement prompt
    critique_text = f"Overall: {summary}\n\nIssues:\n"
    for issue in issues:
        ids = issue.get("decision_ids", [])
        critique_text += (
            f"- [{issue['type']}] (decisions {ids}): {issue['description']}\n"
        )

    return {"critique": critique_text if status == "REFINE" else "PASS"}


MAX_ITERATIONS = 3


def quality_router(state: GraphState):
    """Routes to Refine (loop back) or fan-out (proceed)."""
    critique = state.get("critique", "PASS")
    iteration = state.get("iteration", 1)

    if critique == "PASS":
        print(f"Quality check PASSED at iteration {iteration}")
        return "Proceed"

    if iteration >= MAX_ITERATIONS:
        print(
            f"Max iterations ({MAX_ITERATIONS}) reached. Proceeding with current decisions."
        )
        return "Proceed"

    print(f"Sending back for refinement (iteration {iteration})")
    return "Refine"


def fan_out_decisions(state: GraphState):
    if not state["decisions"]:
        print("---NO ACTIONABLE DECISIONS FOUND---")
        return []

    today = state.get("current_date", datetime.date.today().strftime("%Y-%m-%d"))
    return [
        Send(
            "ProcessDecision",
            {
                "decision_id": d["id"],
                "decision_summary": d["summary"],
                "relevant_context": d["context"],
                "transcript_en": state["transcript_en"],
                "current_date": today,
                "total_decisions": len(state["decisions"]),
            },
        )
        for d in state["decisions"]
    ]


def process_decision_node(state: dict):
    did = state["decision_id"]
    total = state["total_decisions"]
    summary = state["decision_summary"]
    context = state["relevant_context"]
    full_text = state["transcript_en"]
    today = state["current_date"]

    tag = f"[ADR-{did:03d}/{total}]"

    # ── 1. RESEARCH ──────────────────────────────────────────────
    print(f"---{tag} RESEARCHING: {summary}---")

    db_results = collection.query(query_texts=[summary], n_results=5)
    db_docs = db_results["documents"][0]

    web_res = tavily_search.invoke(
        {"query": f"Best practices and pros/cons for {summary}"}
    )
    web_docs = [r["content"] for r in web_res["results"]]

    all_docs = db_docs + web_docs
    rerank_prompt = f"""As a Software Architect, pick only the relevant technical facts
for the decision: "{summary}".
Ignore any context belonging to a different platform or technology.

DATA:
{all_docs}

Return the top 5 relevant facts as bullet points."""

    final_context = get_model_response(
        rerank_prompt, model_name="gemini-3.1-pro-preview"
    )

    # ── 2. GENERATE ADR ─────────────────────────────────────────
    print(f"---{tag} GENERATING ADR---")

    gen_prompt = f"""You are a Senior Software Architect. Write a CONCISE, professional ADR
following the Nygard standard. Human-written ADRs avoid fluff and focus on
technical rationale.

INPUTS:
- Decision: {summary}
- Relevant Discussion: {context}
- Broader Meeting Context (for cross-references only): {full_text}
- Tech Research: {final_context}
- Date: {today}

STRUCTURE (strict Nygard):
1. Title: "[ADR-{did:03d}] <concise technical title>"
2. Status: Proposed | Accepted (infer from the discussion tone and consensus)
3. Context: The problem, forces at play, urgency if deadlines are mentioned
4. Decision: The chosen solution, stated clearly
5. Considered Options: At least 2 alternatives with brief rationale for rejection
6. Consequences: Tradeoff analysis (Pros / Cons) grounded in the research data

LANGUAGE: English.
FORMAT: Strict Markdown. Be concise, no filler sentences.

ADR STRTUCTURE EXAMPLE TO BE FOLLOWED:

# [ADR-X] TITLE

**Date:** yyyy-mm-dd

## Status
Status here

## Context
Context Here

## Decision
Decision here

## Consequences
Consequences here
"""

    adr_content = get_model_response(gen_prompt, model_name="gemini-3.1-pro-preview")

    # ── 3. EXPORT ────────────────────────────────────────────────
    print(f"---{tag} EXPORTING MARKDOWN---")

    first_line = adr_content.split("\n")[0]
    clean_title = (
        re.sub(r"[^a-zA-Z0-9\s]", "", first_line).lower().strip().replace(" ", "-")
    )
    filename = f"{clean_title[:60]}.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(adr_content)

    print(f"Saved: {filename}")

    return {
        "adrs": [
            {
                "decision_id": did,
                "summary": summary,
                "filename": filename,
                "content": adr_content,
            }
        ]
    }


def critique_router_with_fanout(state: GraphState):
    """Returns either a node name (string) to loop back, or a list of Send() to fan out."""
    critique = state.get("critique", "PASS")
    iteration = state.get("iteration", 1)

    needs_refinement = critique != "PASS" and iteration < MAX_ITERATIONS

    if needs_refinement:
        print(f"Looping back for refinement (iteration {iteration})")
        # String return → LangGraph routes to this node name directly
        return "ExtractDecisions"

    # List of Send() → LangGraph fans out to ProcessDecision nodes
    print(f"Proceeding to ADR generation with {len(state['decisions'])} decision(s)")
    sends = fan_out_decisions(state)
    if not sends:
        return END
    return sends


# ── Build Graph ──────────────────────────────────────────────────
workflow = StateGraph(GraphState)

workflow.add_node("DetectLanguage", language_detector_node)
workflow.add_node("Translate", translate_node)
workflow.add_node("Passthrough_EN", passthrough_en_node)
workflow.add_node("ExtractDecisions", extract_decisions_node)
workflow.add_node("CritiqueDecisions", critique_decisions_node)
workflow.add_node("ProcessDecision", process_decision_node)

workflow.add_edge(START, "DetectLanguage")
workflow.add_conditional_edges(
    "DetectLanguage",
    language_router,
    {"Translate": "Translate", "Passthrough_EN": "Passthrough_EN"},
)
workflow.add_edge("Translate", "ExtractDecisions")
workflow.add_edge("Passthrough_EN", "ExtractDecisions")
workflow.add_edge("ExtractDecisions", "CritiqueDecisions")

# No mapping dict - LangGraph handles both strings and Send() natively
workflow.add_conditional_edges(
    "CritiqueDecisions",
    critique_router_with_fanout,
)

workflow.add_edge("ProcessDecision", END)

adr_agent = workflow.compile()

result = adr_agent.invoke(
    {
        "original_transcript": constants.transcript,
        "transcript_en": "",
        "language": "",
        "current_date": datetime.date.today().strftime("%Y-%m-%d"),
        "decisions": [],
        "adrs": [],
    }
)

# ── Summary ──
print(f"\n{'=' * 60}")
print(f"Generated {len(result['adrs'])} ADR(s):\n")
for adr in sorted(result["adrs"], key=lambda x: x["decision_id"]):
    print(f"  [{adr['decision_id']:03d}] {adr['summary']}")
    print(f"        -> {adr['filename']}\n")
