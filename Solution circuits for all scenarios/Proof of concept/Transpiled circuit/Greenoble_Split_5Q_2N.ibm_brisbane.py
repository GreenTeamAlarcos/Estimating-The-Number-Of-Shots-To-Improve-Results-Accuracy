# Circuito transpilado automáticamente
# ßackend : ibm_brisbane
# Time: 0.08139467239379883
from qiskit import QuantumCircuit

class TranspiledCircuit:
	def __init__(self, qubits=None):
		original_qubits = [4, 5, 12, 18, 21, 22, 47, 52, 71, 118]
		self.qubits = range(0, 10)  if qubits is None else original_qubits

	def get_circuit(self, targetQubits=None):
		circuit = QuantumCircuit(127, 10)
		if targetQubits is None:
			targetQubits = self.qubits
		circuit.sx(targetQubits[0])
		circuit.rz(-3.141592609878403, targetQubits[0])
		circuit.sx(targetQubits[0])
		circuit.sx(targetQubits[1])
		circuit.rz(-3.141592609878403, targetQubits[1])
		circuit.sx(targetQubits[1])
		circuit.sx(targetQubits[2])
		circuit.rz(-4.371139006309477e-08, targetQubits[2])
		circuit.sx(targetQubits[2])
		circuit.sx(targetQubits[3])
		circuit.rz(-3.141592609878403, targetQubits[3])
		circuit.sx(targetQubits[3])
		circuit.sx(targetQubits[4])
		circuit.rz(-4.371139006309477e-08, targetQubits[4])
		circuit.sx(targetQubits[4])
		circuit.sx(targetQubits[5])
		circuit.rz(-4.371139006309477e-08, targetQubits[5])
		circuit.sx(targetQubits[5])
		circuit.sx(targetQubits[6])
		circuit.rz(-4.371139006309477e-08, targetQubits[6])
		circuit.sx(targetQubits[6])
		circuit.sx(targetQubits[7])
		circuit.rz(-4.371139006309477e-08, targetQubits[7])
		circuit.sx(targetQubits[7])
		circuit.sx(targetQubits[8])
		circuit.rz(-3.141592609878403, targetQubits[8])
		circuit.sx(targetQubits[8])
		circuit.sx(targetQubits[9])
		circuit.rz(-3.141592609878403, targetQubits[9])
		circuit.sx(targetQubits[9])
		#circuit.measure(targetQubits[4], 0)
		#circuit.measure(targetQubits[5], 1)
		#circuit.measure(targetQubits[2], 2)
		#circuit.measure(targetQubits[6], 3)
		#circuit.measure(targetQubits[7], 4)
		#circuit.measure(targetQubits[0], 5)
		#circuit.measure(targetQubits[1], 6)
		#circuit.measure(targetQubits[3], 7)
		#circuit.measure(targetQubits[8], 8)
		#circuit.measure(targetQubits[9], 9)
		#print(circuit)
		return circuit


if __name__ == "__main__":
	tc = TranspiledCircuit()
	tc.get_circuit()