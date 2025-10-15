# Circuito transpilado automáticamente
# ßackend : ibm_brisbane
# Time: 0.04862046241760254
from qiskit import QuantumCircuit

class TranspiledCircuit:
	def __init__(self, qubits=None):
		original_qubits = [12, 13, 17]
		self.qubits = range(0, 3)  if qubits is None else original_qubits

	def get_circuit(self, targetQubits=None):
		circuit = QuantumCircuit(127, 3)
		if targetQubits is None:
			targetQubits = self.qubits
		circuit.rz(1.5707963267948966, targetQubits[0])
		circuit.sx(targetQubits[0])
		circuit.rz(-0.7853981633974483, targetQubits[0])
		circuit.rz(1.5707963267948966, targetQubits[1])
		circuit.sx(targetQubits[1])
		circuit.rz(2.324097895616613, targetQubits[1])
		circuit.rz(1.5707963267948966, targetQubits[2])
		circuit.sx(targetQubits[2])
		circuit.rz(-0.7853981633974492, targetQubits[2])
		circuit.sx(targetQubits[2])
		circuit.rz(1.5707963267948966, targetQubits[2])
		circuit.ecr(targetQubits[0], targetQubits[2])
		circuit.rz(0.7853981633974483, targetQubits[0])
		circuit.sx(targetQubits[0])
		circuit.rz(-2.4391114359904016, targetQubits[0])
		circuit.sx(targetQubits[0])
		circuit.rz(1.5707963267948966, targetQubits[0])
		circuit.ecr(targetQubits[1], targetQubits[0])
		circuit.rz(1.5707963267948966, targetQubits[0])
		circuit.sx(targetQubits[0])
		circuit.rz(2.4391114359904025, targetQubits[0])
		circuit.rz(0.7533015688217155, targetQubits[1])
		circuit.sx(targetQubits[1])
		circuit.rz(-1.5707963267948966, targetQubits[1])
		circuit.barrier(targetQubits[1])
		circuit.rz(1.5707963267948966, targetQubits[2])
		circuit.sx(targetQubits[2])
		circuit.rz(-2.356194490192345, targetQubits[2])
		circuit.barrier(targetQubits[2])
		circuit.barrier(targetQubits[2])
		circuit.barrier(targetQubits[2])
		#circuit.measure(targetQubits[1], 0)
		#circuit.measure(targetQubits[0], 1)
		#circuit.measure(targetQubits[2], 2)
		#print(circuit)
		return circuit


if __name__ == "__main__":
	tc = TranspiledCircuit()
	tc.get_circuit()