from qham.HBM.hmbslq import SquareLattice, create_heisenberg_lattice_circuit
from qiskit.circuit import QuantumCircuit, Parameter

def test_create_heisenberg_lattice_circuit():
    rows, cols = 2, 2
    lattice = SquareLattice(rows, cols)
    t = Parameter('t')
    qc = create_heisenberg_lattice_circuit(lattice, t)
    
    # Check if the circuit is not None
    assert qc is not None
    # Check if the circuit has the correct number of qubits
    assert qc.num_qubits == rows * cols
    # Check if the correct number of neighbor interactions are in the circuit
    # Each site except for edge sites should interact with 4 neighbors
    # Edge sites will have fewer interactions, so we count the interactions
    num_interactions = sum(len(neighbors) for neighbors in lattice.adjacency_list.values())
    expected_gate_count = 3 * num_interactions  # 3 gates per interaction (rxx, ryy, rzz)
    assert len(qc) == expected_gate_count
