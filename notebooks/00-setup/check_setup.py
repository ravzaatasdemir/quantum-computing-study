"""Environment check: builds a Bell state and runs it on the local Aer simulator."""
import qiskit
import qiskit_aer
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

print(f"qiskit {qiskit.__version__}, qiskit-aer {qiskit_aer.__version__}")

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()
print(qc.draw())

sim = AerSimulator()
counts = sim.run(transpile(qc, sim), shots=1000).result().get_counts()
print("Counts:", counts)
assert set(counts) <= {"00", "11"}, "Unexpected outcomes — check your installation."
print("Setup OK")
