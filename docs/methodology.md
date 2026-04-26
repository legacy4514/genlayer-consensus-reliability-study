# Methodology

## Goal

Evaluate how custom validator logic affects consensus reliability in GenLayer Intelligent Contracts under nondeterministic execution.

## Process

1. Deploy each contract in GenLayer Studio.
2. Execute each write method multiple times.
3. Inspect validator votes.
4. Decode `eq_outputs` where available.
5. Record `nondet_disagree` / `NOTIFY_NONDET_DISAGREEMENT`.
6. Read contract state after success and failure.
7. Compare behavior across contracts.

## Metrics

- Agreement ratio
- Disagreement ratio
- Presence of nondet disagreement signals
- Consensus outcome
- State mutation after success/failure
- Output structure
- Validator criterion
