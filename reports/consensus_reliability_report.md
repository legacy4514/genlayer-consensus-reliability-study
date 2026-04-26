# Consensus Reliability and Validator Agreement Under Non-Deterministic Execution

**Network:** Bradbury Testnet  
**Tool:** GenLayer Studio  
**Date:** April 2026  

## Abstract

This report presents a structured experimental evaluation of consensus reliability and validator agreement in GenLayer Intelligent Contracts under non-deterministic execution. Experiments were conducted on the Bradbury testnet using progressively complex contracts, generating empirical data across validator votes, nondeterministic disagreement signals, and contract state transitions.

The findings demonstrate that consensus outcomes in GenLayer are primarily determined by the logic defined within `validator_fn`, rather than the specific outputs produced by `nondet_fn`. Three key behaviors were identified and validated: probabilistic mismatch, structural schema enforcement, and state atomicity under consensus failure.

## 1. Introduction

GenLayer Intelligent Contracts extend traditional smart contract execution by allowing controlled non-deterministic operations while maintaining blockchain consensus. The key mechanism evaluated in this report is the Equivalence Principle, especially custom validation through `gl.vm.run_nondet_unsafe`.

## 2. Methodology

The study used five contracts:

| Phase | Contract | Purpose |
|---|---|---|
| 1A | StableDieRoll | Baseline consensus |
| 1B | UnstableDieRoll | Probabilistic failure |
| 2 | StructuredDieRoll | Schema normalization |
| 3 | BrokenSchemaRoll | Schema breach rejection |
| 8 | StorageConsensusRoll | State atomicity |

Each contract was deployed and executed on Bradbury using GenLayer Studio. Validator votes, `eq_outputs`, `nondet_disagree`, and contract state were inspected after each execution.

## 3. Results Summary

| Contract | Agreement | Disagreement | Reliability |
|---|---:|---:|---|
| StableDieRoll | 100% | 0% | High |
| UnstableDieRoll | 40% | 60% | Intentionally unstable |
| StructuredDieRoll | 100% | 0% | High, structured |
| BrokenSchemaRoll | 67% | 33% | Conditional |
| StorageConsensusRoll | N/A | N/A | Atomicity verified |

## 4. Key Findings

### 4.1 Validator Logic Drives Consensus

Consensus depends on `validator_fn` acceptance logic, not raw nondeterministic output.

### 4.2 Exact-Match Validation is an Anti-Pattern

Requiring validators to reproduce a nondeterministic result causes probabilistic disagreement.

### 4.3 Structured Output Improves Robustness

Returning JSON such as `{"roll": 4}` allows validators to separate schema correctness from value validity.

### 4.4 Schema Enforcement Matters

A payload like `{"value": 4}` may contain a valid die value, but should be rejected if the expected schema is `{"roll": N}`.

### 4.5 Failed Consensus Preserves State

The storage experiment confirmed that failed consensus produces no observable state mutation.

### 4.6 `NOTIFY_NONDET_DISAGREEMENT` is a Useful Diagnostic Signal

This signal identifies validator rejection at the nondeterministic boundary.

## 5. Design Principles

1. Avoid exact-match validation for nondeterministic outputs.
2. Return structured JSON from `nondet_fn`.
3. Validate schema before value.
4. Unwrap `leader_result` safely.
5. Wrap `validator_fn` in broad exception handling.
6. Use state counters to audit committed transactions.
7. Decode `eq_outputs` first when debugging consensus failures.

## 6. Conclusion

The primary engineering challenge in GenLayer is not eliminating nondeterminism, but designing validator functions that safely interpret and constrain it. Structured outputs, schema enforcement, and defensive validator logic significantly improve consensus reliability.
