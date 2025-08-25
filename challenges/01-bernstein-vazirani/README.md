# 01 – Bernstein‑Vazirani (Difficulty: beginner)

## Problem
Given an unknown binary string s, design a quantum circuit using the Bernstein–Vazirani algorithm to determine s with one oracle query. For example, take a three‑bit secret string (e.g., 101). Your circuit should output the correct bitstring with high probability.

## Theory Snapshot
- Prepare n input qubits in state |0...0⟩ and 1 ancilla qubit in |1⟩, then apply Hadamard gates.
- The oracle encodes the function f_s(x) = s·x ⊕ b, which flips the phase of the ancilla when the inner product is 1.
- After a second layer of Hadamards, measuring the input qubits yields s.

## What to Build
1. Choose a secret bitstring (e.g., `s = 101`) and encode it in the oracle.
2. Construct the circuit using OpenQASM or Qiskit to implement the algorithm.
3. Simulate the circuit and demonstrate that measurement results match s.

## Acceptance Criteria
- The measured bitstring equals the chosen secret string with probability ≥90%.
- Unit tests pass.

## Run
Use Qiskit to run the circuit via:
```
bash
python run.py
```
