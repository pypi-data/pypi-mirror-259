import torch
import numpy as np
from qham.HBM.hmb import HeisenbergModel  

def test_heisenberg_model_initialization():
    N = 4
    J = 1
    model = HeisenbergModel(N, J)
    assert model.N == N
    assert model.J == J
    assert model.Sx.shape == (2, 2)
    assert model.Sy.shape == (2, 2)
    assert model.Sz.shape == (2, 2)
    assert model.I.shape == (2, 2)
    assert isinstance(model.H, torch.Tensor)
    assert model.H.shape == (2**N, 2**N)
    assert model.H.dtype == torch.complex64

def test_heisenberg_hamiltonian_hermitian():
    N = 4
    J = 1
    model = HeisenbergModel(N, J)
    hamiltonian = model.build_hamiltonian()
    # A Hermitian matrix is equal to its conjugate transpose
    assert torch.allclose(hamiltonian, hamiltonian.conj().t())

def test_heisenberg_solve_eigenvalues():
    N = 4
    J = 1
    model = HeisenbergModel(N, J)
    eigenvalues, eigenvectors = model.solve_eigenvalues()
    # The number of eigenvalues and eigenvectors should match the size of the Hamiltonian matrix
    assert eigenvalues.shape == (2**N,)
    assert eigenvectors.shape == (2**N, 2**N)
    # Eigenvalues should be real for a Hermitian matrix
    assert torch.allclose(eigenvalues.imag, torch.zeros_like(eigenvalues))

def test_plot_energy_levels_runs():
    N = 4
    J = 1
    model = HeisenbergModel(N, J)
    eigenvalues, _ = model.solve_eigenvalues()
    # Test simply runs the function to ensure no errors; it doesn't check the plot output
    model.plot_energy_levels(eigenvalues)
    assert True  # If the function runs without errors, this test passes

