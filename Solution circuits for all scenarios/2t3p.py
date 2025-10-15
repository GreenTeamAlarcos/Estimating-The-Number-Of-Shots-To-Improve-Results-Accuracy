from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

ALGORITHM = "2t3p"
circuit_name = "2t3p"
qubits = 3
outputQubits = 3
shots = 4156

expected = [(1, 0.5),(6, 0.5)]
ORIGINAL_QUBITS = 3
SPLIT = False

circuits = [QuantumCircuit(qubits, qubits)]

qreg_q = QuantumRegister(qubits, 'q')
creg_c = ClassicalRegister(qubits, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuits[0].h(qreg_q[0])
circuits[0].cx(qreg_q[0], qreg_q[1])
circuits[0].x(qreg_q[1])
circuits[0].barrier(qreg_q[0])
circuits[0].barrier(qreg_q[0])
circuits[0].cx(qreg_q[1], qreg_q[2])
circuits[0].barrier(qreg_q[0])
circuits[0].x(qreg_q[1])
circuits[0].barrier(qreg_q[2])
# circuits[0].measure(qreg_q[0], creg_c[0])
# circuits[0].measure(qreg_q[1], creg_c[1])
# circuits[0].measure(qreg_q[2], creg_c[2])

startQubit = qubits-outputQubits
for i in range(0, len(circuits)) :
	for j in range(startQubit, qubits) :
		circuits[i].measure(j, qubits-j-1)