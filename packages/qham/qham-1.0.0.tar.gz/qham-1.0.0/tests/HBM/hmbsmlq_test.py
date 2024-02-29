import numpy as np
import pytest
from qiskit.circuit import QuantumCircuit, Parameter
from qham.HBM.hmbsmlq import SquareLatticeMatrix, create_heisenberg_square_lattice_matrix_circuit 

def test_square_lattice_matrix_adjacency():
    rows, cols = 2, 2
    lattice = SquareLatticeMatrix(rows, cols)
    adjacency_matrix = lattice.adjacency_matrix
    assert adjacency_matrix.shape == (rows * cols, rows * cols)
    # For a 2x2 lattice, we can manually check if the neighbors are correct
    assert adjacency_matrix[0, 1] == 1  # Right neighbor
    assert adjacency_matrix[0, 2] == 1  # Down neighbor
    assert np.sum(adjacency_matrix) == 2 * 4  # Each site has 2 neighbors in a 2x2 lattice

def test_are_neighbors():
    rows, cols = 2, 2
    lattice = SquareLatticeMatrix(rows, cols)
    assert lattice.are_neighbors(0, 1) is True
    assert lattice.are_neighbors(0, 3) is False  # Diagonal, not direct neighbors

def test_create_heisenberg_square_lattice_matrix_circuit():
    rows, cols = 2, 2
    lattice_matrix = SquareLatticeMatrix(rows, cols)
    t = Parameter('t')
    qc = create_heisenberg_square_lattice_matrix_circuit(lattice_matrix, t)
    assert isinstance(qc, QuantumCircuit)
    # For a 2x2 lattice, there should be 3 * 2 * 2 = 12 gates
    # (3 gates per interaction, 2 interactions per qubit for a square lattice)
    assert len(qc.data) == 12