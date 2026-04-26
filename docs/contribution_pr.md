# Contribution PR: Consensus Reliability Study for GenLayer Intelligent Contracts

## Summary

This PR contributes a structured experimental study on consensus reliability and validator agreement under nondeterministic execution in GenLayer Intelligent Contracts.

The contribution includes:

- Five GenLayer Studio-compatible contracts
- A structured research report
- Experiment methodology
- Summary data templates
- Practical design principles for safer Intelligent Contract development

## Motivation

GenLayer introduces nondeterministic execution through Intelligent Contracts. This requires developers to think carefully about how validators evaluate leader results.

This study demonstrates that consensus reliability depends primarily on validator logic, output structure, and schema validation.

## Included Experiments

| Contract | Purpose |
|---|---|
| `StableDieRoll` | Demonstrates stable nondeterministic validation |
| `UnstableDieRoll` | Demonstrates failure from exact-match validation |
| `StructuredDieRoll` | Demonstrates JSON-based robust validation |
| `BrokenSchemaRoll` | Demonstrates strict schema enforcement |
| `StorageConsensusRoll` | Demonstrates state atomicity after failed consensus |

## Key Findings

- Exact-match validation on nondeterministic output is unreliable.
- Structured JSON output improves validation reliability.
- Schema mismatch should be rejected before value validation.
- Failed consensus does not mutate contract state.
- `NOTIFY_NONDET_DISAGREEMENT` is useful for diagnosing validator disagreement.

## Testing

Contracts were tested manually in GenLayer Studio on the Bradbury testnet.

## Suggested Review Focus

- Accuracy of GenLayer VM assumptions
- Correctness of `validator_fn` patterns
- Usefulness of the design principles for developers
- Whether this should live in examples, docs, or a research folder
