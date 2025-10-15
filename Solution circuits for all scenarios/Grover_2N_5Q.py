from qiskit import QuantumCircuit
from math import pi

qubits = 5
shots = 1024
	
circuits = [QuantumCircuit(qubits, qubits),]
ALGORITHM = "Grover"
	  
ONE = [0, 1]
ZERO = [1, 0]

expected = [(0, 0.5),(31, 0.5),]

TEMPLATE = 'common.solo_circuit.splitting.template.txt'
ORIGINAL_QUBITS = 5
SPLIT = False
def oracle_0() :	 # Looks for 0
	U = QuantumCircuit(5)
	U.x(0)
	U.x(1)
	U.x(2)
	U.x(3)
	U.x(4)
	U.mcp(pi, [0, 1, 2, 3], 4)
	U.x(0)
	U.x(1)
	U.x(2)
	U.x(3)
	U.x(4)
	return U
def oracle_1() :	 # Looks for 31
	U = QuantumCircuit(5)
	U.mcp(pi, [0, 1, 2, 3], 4)
	return U
def diffuser() :
	U = QuantumCircuit(5)
	U.h(0)
	U.h(1)
	U.h(2)
	U.h(3)
	U.h(4)
	U.x(0)
	U.x(1)
	U.x(2)
	U.x(3)
	U.x(4)
	U.mcp(pi, [0, 1, 2, 3], 4)
	U.x(0)
	U.x(1)
	U.x(2)
	U.x(3)
	U.x(4)
	U.h(0)
	U.h(1)
	U.h(2)
	U.h(3)
	U.h(4)
	return U


for i in range(0, len(circuits)) :
	for j in range (0, qubits) :
		circuits[i].h(j)

for i in range (0, 3) :
	circuits[0].append(oracle_0(), [0,1,2,3,4])
	circuits[0].append(oracle_1(), [0,1,2,3,4])
	circuits[0].append(diffuser(), [0,1,2,3,4])


for i in range(0, len(circuits)) :
	for j in range(0, qubits) :
		circuits[i].measure(j, qubits-j-1)