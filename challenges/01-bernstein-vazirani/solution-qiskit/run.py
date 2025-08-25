from qiskit import QuantumCircuit, Aer, execute
import json
from pathlib import Path


def main():
    # Define secret bitstring for Bernstein–Vazirani (e.g., 101)
    secret = '101'
    n = len(secret)

    # Quantum circuit with n input qubits and one ancilla qubit
    qc = QuantumCircuit(n + 1, n)

    # Prepare ancilla in |1> and put all qubits in superposition
    qc.x(n)
    qc.h(n)
    for i in range(n):
        qc.h(i)

    # Oracle: apply CNOT from each input qubit to ancilla where secret bit is 1
    for i, bit in enumerate(secret):
        if bit == '1':
            qc.cx(i, n)

    # Apply Hadamard again to input qubits
    for i in range(n):
        qc.h(i)

    # Measure input qubits
    for i in range(n):
        qc.measure(i, i)

    # Run the circuit on the QASM simulator
    backend = Aer.get_backend('qasm_simulator')
    shots = 1024
    job = execute(qc, backend=backend, shots=shots)
    result = job.result()
    counts = result.get_counts()

    # Save results to metrics.json in the results directory
    here = Path(__file__).resolve()
    challenge_dir = here.parent.parent  # challenges/<id>-<slug>
    results_dir = challenge_dir / 'results'
    results_dir.mkdir(parents=True, exist_ok=True)
    metrics = {
        'shots': shots,
        'counts': counts
    }
    with open(results_dir / 'metrics.json', 'w') as f:
        json.dump(metrics, f, indent=2)


if __name__ == '__main__':
    main()
