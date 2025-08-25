# 00 – Hello Qubit (Difficulty: beginner)

## Problem
Prepare a single qubit in superposition and measure it many times. Verify that the results
are ~50/50 between `0` and `1` within statistical tolerance.

## Theory Snapshot
- Apply a Hadamard gate to |0⟨ to get (|0⟨ + |1⟨)/√2.
- Measuring yields 0 or 1 with equal probability (ideally).

## What to Build
1. Build a one-qubit circuit with H then measure.
2. Execute with a few thousand shots on a simulator.
3. Save counts to `results/metrics.json`.

## Acceptance Criteria
- Sum of counts equals `shots` in `metrics.json`.
- Ratio of `0` and `1` within ±10% of 50/50 (loose tolerance for noise).

## Run
```
make run CHALLENGE=00-hello-qubit BACKEND=qiskit
make test CHALLENGE=00-hello-qubit
```
