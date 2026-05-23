# [ADR-005] Video Collaboration Component for Telehealth
- **Status**: Accepted
- **Context**: The telemonitoring platform requires video streaming capabilities to support clinical interventions such as teleconsultations, tele-interconsultations, and tele-education. Building a robust video conferencing tool from scratch is highly complex.
- **Decision**: Integrate the existing RNP (Rede Nacional de Ensino e Pesquisa) video collaboration component into the platform rather than developing a custom video solution.
- **Considered Options**:
  - *Option 1: Develop a custom WebRTC-based service.* Rejected due to the high development cost, heavy maintenance burden, and unnecessary duplication of effort for a solved problem.
  - *Option 2: Commercial Off-The-Shelf (COTS) solutions (e.g., Zoom, Google Meet).* Rejected due to recurring licensing costs, potential privacy law (LGPD) conflicts regarding where the video data is routed, and poor integration capabilities with internal clinical records.
- **Consequences**:
  - *Pros:* Drastically reduces time-to-market; leverages a pre-validated, compliant component native to the academic/public network ecosystem; allows developers to focus entirely on clinical workflows and data capture rather than video streaming logistics.
  - *Cons:* Introduces a hard dependency on the RNP API/infrastructure, meaning the platform's video capabilities are subject to RNP's uptime and service limits.