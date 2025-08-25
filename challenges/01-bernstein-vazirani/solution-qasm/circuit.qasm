OPENQASM 2.0;
include "qelib1.inc";
qreg q[4];
creg c[3];
// prepare ancilla qubit q[3] in |1>
x q[3];
// apply Hadamard gates to all qubits
h q[0];
h q[1];
h q[2];
h q[3];
// oracle for secret string s=101: controlled-NOT from q[0] and q[2] to ancilla
cx q[0], q[3];
cx q[2], q[3];
// apply Hadamard to input qubits again
h q[0];
h q[1];
h q[2];
// measure input qubits
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
