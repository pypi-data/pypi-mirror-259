import pytest
from qiskit import QuantumCircuit
from qham.HBM.hmbq import create_heisenberg_circuit  

def test_heisenberg_circuit_creation():
    N = 4
    trotter_steps = 1
    qc = create_heisenberg_circuit(N, trotter_steps)
    
    # Check if the circuit has the correct number of qubits
    assert qc.num_qubits == N

    # Count the number of each gate type
    rxx_gates = qc.count_ops().get('rxx', 0)
    ryy_gates = qc.count_ops().get('ryy', 0)
    rzz_gates = qc.count_ops().get('rzz', 0)

    # Check if the number of gates is correct
    expected_gates_per_step = N  # N - 1 + 1 for periodic boundary
    assert rxx_gates == expected_gates_per_step * trotter_steps
    assert ryy_gates == expected_gates_per_step * trotter_steps
    assert rzz_gates == expected_gates_per_step * trotter_steps

    # Check for the existence of the time evolution parameter 't'
    parameters = qc.parameters
    assert len(parameters) == 1
    assert next(iter(parameters)).name == 't'

@pytest.mark.parametrize("N, trotter_steps", [(4, 1), (4, 2), (6, 3)])
def test_heisenberg_circuit_variations(N, trotter_steps):
    qc = create_heisenberg_circuit(N, trotter_steps)

    # Check that the number of trotter steps is reflected in the gate count
    expected_gates_per_step = N
    total_gates = expected_gates_per_step * trotter_steps

    assert qc.count_ops().get('rxx', 0) == total_gates
    assert qc.count_ops().get('ryy', 0) == total_gates
    assert qc.count_ops().get('rzz', 0) == total_gates