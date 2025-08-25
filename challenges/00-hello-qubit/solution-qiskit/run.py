from qiskit import QuantumCircuit, Aer, execute
import json
from pathlib import Path


def main():
    circuit = QuantumCircuit(1, 1)
    circuit.h(0)
    circuit.measure(0, 0)
    simulator = Aer.get_backend('qasm_simulator')
    shots = 1024
    job = execute(circuit, simulator, shots=shots)
    result = job.result()
    counts = result.get_counts()

    metrics = {
        "shots": shots,
        "counts": {str(k): int(v) for k, v in counts.items()}
    }

    results_dir = Path(__file__).resolve().parents[1] / 'results'
    results_dir.mkdir(exist_ok=True)
    with open(results_dir / 'metrics.json', 'w') as f:
        json.dump(metrics, f)


if __name__ == "__main__":
    main()
