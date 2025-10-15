from qiskit import QuantumCircuit

qubits = 5
shots = 1024
	
circuits = [QuantumCircuit(qubits, qubits)]
ALGORITHM = "Greenoble"
	  
ONE = [0, 1]
ZERO = [1, 0]

expected = [(0, 0.5),(31, 0.5),]

TEMPLATE = 'common.solo_circuit.splitting.template.txt'
ORIGINAL_QUBITS = 5
SPLIT = False
def get0():
	U = QuantumCircuit(5, name="0")
	U.x(0)
	U.append(get1L().control(1), [0,1,2,3,4])
	U.x(0)
	U.append(get1R().control(1), [0,1,2,3,4])
	return U.to_gate()

def get1L():
	U = QuantumCircuit(4, name="1L")
	U.ry(-1.5707963705062866, 0)
	U.append(get2LL(), [1,2,3])
	return U.to_gate()

def get1R():
	U = QuantumCircuit(4, name="1R")
	U.ry(1.5707963705062866, 0)
	U.append(get2RR(), [1,2,3])
	return U.to_gate()

def get3RRR():
	U = QuantumCircuit(2, name="3RRR")
	U.ry(1.5707963705062866, 0)
	U.ry(1.5707963705062866, 1)
	return U.to_gate()

def get3LLL():
	U = QuantumCircuit(2, name="3LLL")
	U.ry(-1.5707963705062866, 0)
	U.ry(-1.5707963705062866, 1)
	return U.to_gate()

def get2RR():
	U = QuantumCircuit(3, name="2RR")
	U.ry(1.5707963705062866, 0)
	U.append(get3RRR(), [1,2])
	return U.to_gate()

def get2LL():
	U = QuantumCircuit(3, name="2LL")
	U.ry(-1.5707963705062866, 0)
	U.append(get3LLL(), [1,2])
	return U.to_gate()




for i in range(0, len(circuits)) :
	for j in range (0, qubits) :
		circuits[i].h(j)

circuits[0].append(get0(), [0,1,2,3,4])

for i in range(0, len(circuits)) :
	for j in range(0, qubits) :
		circuits[i].measure(j, qubits-j-1)