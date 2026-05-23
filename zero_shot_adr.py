from dotenv import load_dotenv
import constants
from google import genai
from langchain_tavily import TavilySearch
import datetime
import os

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

client = genai.Client(api_key=gemini_api_key, vertexai=True)
tavily_search = TavilySearch(topic="general", max_results=3, api_key=tavily_api_key)


def get_model_response(prompt, model_name="gemini-3-flash-preview"):
    response = client.models.generate_content(model=model_name, contents=prompt)
    return response.text


def generate_multiple_adrs_prompt_eng(transcript):
    """
    Prompt Engineering Approach: Consolidates detection, extraction, internal search,
    and formatting of multiple ADRs into a single flow.
    """
    current_date = datetime.date.today().strftime("%Y-%m-%d")

    mega_prompt = f"""
    ROLE:
    You are a Senior Software Architect. Your task is to process a meeting transcript and
    produce a series of formal, high-quality Architecture Decision Records (ADRs).
    Human-written ADRs avoid fluff and focus strictly on technical rationale.

    INSTRUCTIONS:
    1. LANGUAGE CHECK: If the transcript is not in English, translate the core technical
      concepts internally before processing. The final output MUST be in English.
    2. EXTRACTION: Identify ALL distinct architectural decisions.
      - Group related minor choices into a single ADR (e.g., Auth provider + Auth protocol).
      - Separate distinct domains (e.g., Database choice vs. Frontend framework).
    3. QUALITY FILTER: Focus ONLY on technical/architectural impact. Ignore meta-talk
      (logistics, "can you hear me?"). Be concise; no filler sentences.

    STRUCTURE FOR EACH ADR (Strict Nygard Standard):
    Each ADR must follow this exact markdown structure, separated by '---':

    # [ADR-00X] <concise technical title>
    - **Status**: Proposed | Accepted (infer from the discussion tone and consensus in the transcript)
    - **Context**: The problem, forces at play, and urgency if deadlines are mentioned.
    - **Decision**: The chosen solution, stated clearly and objectively.
    - **Considered Options**: At least 2 alternatives with a brief, sharp rationale for rejection.
    - **Consequences**: Deep tradeoff analysis (Pros / Cons) grounded in technical data and architectural impact.

    MEETING TRANSCRIPT (Date: {current_date}):
    \"\"\"{transcript}\"\"\"

    FINAL OUTPUT (Strict Markdown block containing all ADRs):
    """

    print("--- PROCESSING MEGA-PROMPT (Multi-ADR Extraction) ---")

    response = get_model_response(mega_prompt, model_name="gemini-3.1-pro-preview")

    adrs = response.split("---")
    for i, adr_content in enumerate(adrs):
        if adr_content.strip():
            filename = f"adr_decision_{i+1}.md"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(adr_content.strip())
            print(f"ADR {i+1} extraída e salva como {filename}")

    return response


generate_multiple_adrs_prompt_eng(constants.transcript)
