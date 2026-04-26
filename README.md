# GenLayer Consensus Reliability Study

A structured experimental study of validator agreement and consensus reliability in GenLayer Intelligent Contracts under non-deterministic execution.

## Overview

This repository documents experiments conducted on the GenLayer Bradbury testnet using GenLayer Studio. The goal is to understand how validator logic, structured outputs, schema validation, and failed consensus affect Intelligent Contract reliability.

The study focuses on GenLayer's Equivalence Principle using `gl.vm.run_nondet_unsafe`.

## Key Findings

1. Validator logic drives consensus outcomes more than raw nondeterministic output.
2. Exact-match validation on nondeterministic values is unreliable.
3. Structured JSON outputs improve validator robustness and debugging.
4. Schema enforcement is critical for safe validation.
5. Failed consensus does not mutate contract state.
6. `NOTIFY_NONDET_DISAGREEMENT` is a useful signal for nondeterministic validation failure.

## Experiments

| Phase | Contract | Purpose |
|---|---|---|
| 1A | `StableDieRoll` | Stable nondeterministic baseline |
| 1B | `UnstableDieRoll` | Exact-match failure mode |
| 2 | `StructuredDieRoll` | JSON-structured validation |
| 3 | `BrokenSchemaRoll` | Intentional schema breach |
| 8 | `StorageConsensusRoll` | State atomicity under failed consensus |

## Repository Structure

```text
contracts/
  stable_die_roll.py
  unstable_die_roll.py
  structured_die_roll.py
  broken_schema_roll.py
  storage_consensus_roll.py

reports/
  consensus_reliability_report.md

data/
  experiment_summary.csv
  log_template.json

docs/
  contribution_pr.md
  methodology.md
```

## How to Reproduce

1. Open GenLayer Studio.
2. Create a new contract file.
3. Paste one contract from the `contracts/` directory.
4. Deploy on Bradbury testnet.
5. Execute `roll()` or the relevant method.
6. Inspect:
   - validator votes
   - `eq_outputs`
   - `NOTIFY_NONDET_DISAGREEMENT`
   - contract state after success/failure
7. Record results using `data/experiment_summary.csv`.

## Runtime Notes

All contracts use:

```python
# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *
```

Important GenLayer Studio observations:

- Use `from genlayer import *`, not `import gl`.
- Contract classes inherit from `gl.Contract`.
- `validator_fn` accepts one argument: `leader_result`.
- Use `getattr(leader_result, "calldata", leader_result)` to unwrap leader results.
- Avoid direct `gl.llm.run(...)` in this runtime.
- Use `gl.vm.run_nondet_unsafe(nondet_fn, validator_fn)` for custom nondeterministic validation.

## Contribution Goal

This study is intended as a developer-facing contribution to help GenLayer builders design safer Intelligent Contracts under non-deterministic execution.

## License

MIT
