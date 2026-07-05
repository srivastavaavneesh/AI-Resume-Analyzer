# ADR-0001: AI Provider Abstraction

- Date: 2026-07-04
- Status: Accepted
- Authors: Shipra
- Version: 1.0

## Context
The application integrates with external AI providers for resume parsing and summary generation.  
To avoid vendor lock-in and make future provider additions straightforward, an abstraction layer was required.

## Decision
Introduce the following architecture:

- **AI Client** → communicates only with abstraction layer
- **Provider Factory** → instantiates providers
- **Providers** → Gemini, Groq, future providers

Each provider implements a common interface (`ProviderInterface`) ensuring consistent methods for parsing and summarization.

## Consequences

### Advantages
- Easy provider replacement
- Supports fallback providers
- Better unit testing
- Aligns with Open/Closed Principle
- Clean architecture

### Trade-offs
- Slight increase in project complexity
- Additional abstraction layer

### Unknowns
- Performance differences between providers
- Cost implications of multi-provider support
- Need for monitoring/logging across providers