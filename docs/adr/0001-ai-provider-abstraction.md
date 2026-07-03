# ADR-0001: AI Provider Abstraction

## Status

Accepted

## Context

The application integrates with external AI providers for resume parsing and summary generation.

To avoid vendor lock-in and make future provider additions straightforward, an abstraction layer was required.

## Decision

Introduce the following architecture:

AI Client

↓

Provider Factory

↓

Gemini Provider

Groq Provider

Each provider implements a common interface.

The AI Client communicates only with the abstraction layer and remains independent of any specific AI provider.

## Consequences

### Advantages

- Easy provider replacement
- Supports fallback providers
- Better unit testing
- Open/Closed Principle
- Clean Architecture

### Trade-offs

- Slight increase in project complexity
- Additional abstraction layer