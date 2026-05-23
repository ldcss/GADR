# [ADR-005] Component Reuse for Video Collaboration
- **Status**: Accepted
- **Context**: A core feature of the platform is the ability to conduct teleconsultations and remote interventions. Building a scalable, secure WebRTC or video streaming module from scratch is highly complex and time-consuming.
- **Decision**: Integrate the existing RNP (Rede Nacional de Ensino e Pesquisa) video collaboration component to handle all teleconsultation and tele-education video streaming.
- **Considered Options**:
  - *Option 1: Custom WebRTC implementation.* Rejected due to the massive development effort, infrastructure costs, and unnecessary reinvention of the wheel.
  - *Option 2: Third-party commercial APIs (e.g., Zoom, Twilio).* Rejected to favor existing government/academic infrastructure and avoid licensing costs and data sovereignty issues.
- **Consequences**:
  - *Pros:* Drastically accelerates time-to-market for the teleconsultation module and leverages a pre-validated, compliant infrastructure.
  - *Cons:* The application becomes dependent on the uptime, performance, and specific API constraints of the RNP video component.