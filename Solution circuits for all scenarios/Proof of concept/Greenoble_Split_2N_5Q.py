from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from math import pi

qubits = 10
outputQubits = 10
shots = 2


expected = [(0, 0.5),(31, 0.5),]
	
circuits = [QuantumCircuit(qubits, qubits),]
ALGORITHM = "Grenoble parallel"
	  
ONE = [0, 1]
ZERO = [1, 0]

TEMPLATE = 'common.solo_circuit.splitting.template.txt'
ORIGINAL_QUBITS = 5
SPLIT = False
def getcirc0_0_0() :
	U = QuantumCircuit(1, name="circ0_0_0")
	U.ry(-1.5707963705062866, 0)
	return U.to_gate()

def getcirc0_3LLL() :
	U = QuantumCircuit(2, name="circ0_3LLL")
	U.append(getcirc0_0_0(), range(0, 1))
	U.append(getcirc0_0_0(), range(1, 2))
	return U.to_gate()

def getcirc0_2LL() :
	U = QuantumCircuit(3, name="circ0_2LL")
	U.append(getcirc0_0_0(), range(0, 1))
	U.append(getcirc0_3LLL(), range(1, 3))
	return U.to_gate()

def getcirc0_1L() :
	U = QuantumCircuit(4, name="circ0_1L")
	U.append(getcirc0_0_0(), range(0, 1))
	U.append(getcirc0_2LL(), range(1, 4))
	return U.to_gate()

def getcirc0_0() :
	U = QuantumCircuit(5, name="circ0_0")
	U.append(getcirc0_0_0(), range(0, 1))
	U.append(getcirc0_1L(), range(1, 5))
	return U.to_gate()

def getcirc1_0_0() :
	U = QuantumCircuit(1, name="circ1_0_0")
	U.ry(1.5707963705062866, 0)
	return U.to_gate()

def getcirc1_3RRR() :
	U = QuantumCircuit(2, name="circ1_3RRR")
	U.append(getcirc1_0_0(), range(0, 1))
	U.append(getcirc1_0_0(), range(1, 2))
	return U.to_gate()

def getcirc1_2RR() :
	U = QuantumCircuit(3, name="circ1_2RR")
	U.append(getcirc1_0_0(), range(0, 1))
	U.append(getcirc1_3RRR(), range(1, 3))
	return U.to_gate()

def getcirc1_1R() :
	U = QuantumCircuit(4, name="circ1_1R")
	U.append(getcirc1_0_0(), range(0, 1))
	U.append(getcirc1_2RR(), range(1, 4))
	return U.to_gate()

def getcirc1_0() :
	U = QuantumCircuit(5, name="circ1_0")
	U.append(getcirc1_0_0(), range(0, 1))
	U.append(getcirc1_1R(), range(1, 5))
	return U.to_gate()





startQubit = qubits-outputQubits

########### OJO: dependiendo del problema, es posible que necesites que los cúbits se pongan en superposición al principio.
########### Si lo necesitas y el algoritmo no lo ha hecho, descomenta las líneas siguientes. ¡Feliz ejecución 🤪!


# for i in range(0, len(circuits)) :
# 	for j in range(startQubit, qubits) :
# 		circuits[i].h(j)

for i in range(0, len(circuits)) :
	for j in range(startQubit, qubits) :
		circuits[i].h(j)
circuits[0].append(getcirc0_0(), [0,1,2,3,4])
circuits[0].append(getcirc1_0(), [5,6,7,8,9])


for i in range(0, len(circuits)) :
	for j in range(startQubit, qubits) :
		circuits[i].measure(j, qubits-j-1)

# expanded = circuits[0].decompose(reps=2)   # Esto es para pintar el circuit. A mayor reps, más detalla.
# print(expanded)