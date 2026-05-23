# [ADR-004] Agnostic API Gateway for External Integrations
- **Status**: Accepted
- **Context**: The platform will need to exchange data with external national health systems, primarily the RNDS (Rede Nacional de Dados em Saúde). Tying core business logic directly to RNDS APIs creates vendor/system lock-in.
- **Decision**: Introduce a dedicated, agnostic API export/integration module that acts as a facade between the core platform and any external systems.
- **Considered Options**:
  - *Option 1: Direct point-to-point integration within core services.* Rejected because any changes to the RNDS API or the introduction of new external systems would require refactoring core business logic.
- **Consequences**:
  - *Pros:* Decouples platform logic from external API contracts, allowing the system to easily connect to diverse external platforms in the future.
  - *Cons:* Adds an extra layer of abstraction and networking overhead that must be developed and maintained.