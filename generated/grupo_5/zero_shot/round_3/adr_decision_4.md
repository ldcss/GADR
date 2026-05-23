# [ADR-004] Reuse of RNP Video Collaboration Component for Telehealth
- **Status**: Accepted
- **Context**: The platform's telemonitoring protocols will trigger various telehealth interventions, including teleconsultations and tele-interconsultations between patients, caregivers, and medical specialists. These interventions require a secure, stable video communication channel.
- **Decision**: Integrate the existing RNP (Rede Nacional de Ensino e Pesquisa) video collaboration component into the platform rather than developing a custom video streaming service.
- **Considered Options**:
  - *Custom WebRTC Implementation*: Rejected. Reinventing the wheel would consume significant development time and resources better spent on core clinical logic.
  - *Commercial 3rd-Party APIs (e.g., Twilio, Zoom)*: Rejected. The project operates within an academic/public sector context where leveraging the pre-existing, validated RNP infrastructure is more cost-effective and aligned with institutional partnerships.
- **Consequences**:
  - **Pros**: Drastically reduces development time and complexity. Utilizes a battle-tested component already validated within the RNP ecosystem.
  - **Cons**: Creates a hard architectural dependency on the RNP component's API, release cycle, and uptime.