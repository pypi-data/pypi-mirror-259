from qiskit.circuit.library import CXGate, RZGate, RXGate
from qiskit.circuit import QuantumCircuit, Parameter
import pytest
from qham.TFIM.tfimq import create_tfim_circuit  

def test_create_tfim_circuit_without_periodic_boundary():
    n_qubits = 4
    theta_z = Parameter('theta_z')
    theta_x = Parameter('theta_x')
    
    qc = create_tfim_circuit(n_qubits, theta_z, theta_x)
    assert qc.num_qubits == n_qubits
    # Check the number of gates in the circuit
    # Expect 3 gates per interaction (CX, RZ, CX) times (n_qubits - 1) interactions
    # Plus n_qubits RX gates for the transverse field
    expected_gate_count = 3 * (n_qubits - 1) + n_qubits
    assert len(qc.data) == expected_gate_count

def test_create_tfim_circuit_with_periodic_boundary():
    n_qubits = 4
    theta_z = Parameter('theta_z')
    theta_x = Parameter('theta_x')
    
    qc = create_tfim_circuit(n_qubits, theta_z, theta_x, periodic_boundary=True)
    assert qc.num_qubits == n_qubits
    # Check the number of gates in the circuit
    # Expect 3 additional gates for the periodic boundary
    expected_gate_count = 3 * n_qubits + n_qubits
    assert len(qc.data) == expected_gate_count

def test_create_tfim_circuit_gate_types():
    n_qubits = 4
    theta_z = Parameter('theta_z')
    theta_x = Parameter('theta_x')
    
    qc = create_tfim_circuit(n_qubits, theta_z, theta_x)
    # Check if gate types in circuit match expected types
    gates = [data[0] for data in qc.data]
    assert all(isinstance(gate, (CXGate, RZGate, RXGate)) for gate in gates)
