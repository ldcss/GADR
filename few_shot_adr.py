import constants
from google import genai
from langchain_tavily import TavilySearch
import datetime
from dotenv import load_dotenv
import os

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

client = genai.Client(api_key=gemini_api_key, vertexai=True)
tavily_search = TavilySearch(topic="general", max_results=3)


def get_model_response(prompt, model_name="gemini-3-flash-preview"):
    response = client.models.generate_content(model=model_name, contents=prompt)
    return response.text


def generate_multiple_adrs_prompt_eng(transcript):
    """
    Abordagem de Prompt Engineering: Consolida detecção, extração,
    pesquisa interna e formatação de múltiplas ADRs em um único fluxo.
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

    EXAMPLES OF EXPECTED OUTPUT AND TONE:

    # [ADR-001] Presenters for Views with Internal Logic
    - **Status**: Accepted
    - **Context**: In VIPER architecture, every view controller has its presenter. However, when dealing with subviews or list cells containing internal business logic, the logic is often left embedded directly in the view layer. This violates separation of concerns and prevents isolated testing.
    - **Decision**: Implement dedicated presenters for any subview or cell that contains internal business logic.
    - **Considered Options**:
      - *Option 1: Keep logic inside views.* Rejected because it bloats the view layer and makes unit testing the UI components impossible.
      - *Option 2: Handle subview logic inside the parent ViewController's Presenter.* Rejected because it creates massive, tightly coupled presenters that are hard to maintain.
    - **Consequences**:
      - *Pros:* Complete separation of business logic from the UI layer; enables full unit testing capabilities for specific view/cell components.
      - *Cons:* Increased boilerplate code due to additional presenter files and protocols for minor UI components.

    ---

    # [ADR-012] Projections for JMAP Messages
    - **Status**: Accepted
    - **Context**: JMAP core RFC8620 requires the server to respond only with properties explicitly requested by the client. Currently, the server computes all properties regardless of their cost or client demands, causing severe latencies and unnecessary resource consumption.
    - **Decision**: Introduce two new specific data structures representing JMAP messages (Metadata-only and Metadata + Headers) on top of the existing storage APIs, routing requests to the most appropriate structure based on client criteria.
    - **Considered Options**:
      - *Option 1: Modify existing message storage APIs directly.* Rejected because it would require a massive, high-risk refactor of core storage layer APIs.
      - *Option 2: Perform dynamic run-time property filtering on full entities.* Rejected because it does not solve the underlying database read and computation overhead.
    - **Consequences**:
      - *Pros:* Significant reduction in database overhead. Performance testing under a constant load of 5000 users/hour showed a drop in timeout rates from 20% to 0%. Mean time for GetMessages improved 1000x (from 27,159 ms to 27 ms), and P99 dropped to 1,383 ms.
      - *Cons:* Increased codebase complexity due to managing multiple data structures and routing logic based on requested properties.

    ---

    MEETING TRANSCRIPT (Date: {current_date}):
    \"\"\"{transcript}\"\"\"

    FINAL OUTPUT (Strict Markdown block containing all ADRs):
    """

    print("--- PROCESSING MEGA-PROMPT (Multi-ADR Extraction) ---")

    # LLM only call
    response = get_model_response(mega_prompt, model_name="gemini-3.1-pro-preview")

    # File saving
    adrs = response.split("---")
    for i, adr_content in enumerate(adrs):
        if adr_content.strip():
            filename = f"adr_decision_{i+1}.md"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(adr_content.strip())
            print(f"ADR {i+1} extraída e salva como {filename}")

    return response


generate_multiple_adrs_prompt_eng(constants.transcript)
