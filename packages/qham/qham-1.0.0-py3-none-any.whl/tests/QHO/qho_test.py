import torch
import pytest
from qham.QHO.qho import QuantumHarmonicOscillator  

def test_annihilation_operator():
    n = 10
    qho = QuantumHarmonicOscillator(n, 1.0)
    a = qho.create_annihilation_operator()
    assert a.shape == (n, n)
    assert torch.all(a[-1] == 0)  # Last row should be all zeros

def test_hamiltonian():
    n = 10
    omega = 1.0
    qho = QuantumHarmonicOscillator(n, omega)
    H = qho.create_hamiltonian()
    assert H.shape == (n, n)
    # Check if the Hamiltonian is Hermitian
    assert torch.allclose(H, H.T.conj())

def test_find_eigenstates():
    n = 10
    omega = 1.0
    qho = QuantumHarmonicOscillator(n, omega)
    eigenvalues, eigenvectors = qho.find_eigenstates()
    assert eigenvalues.shape == (n,)
    assert eigenvectors.shape == (n, n)
    # Check if eigenvectors are orthonormal
    identity_matrix = torch.eye(n)
    assert torch.allclose(eigenvectors.T.conj() @ eigenvectors, identity_matrix)

def test_eigenvalues():
    n = 10
    omega = 1.0
    qho = QuantumHarmonicOscillator(n, omega)
    eigenvalues, _ = qho.find_eigenstates()
    # For a quantum harmonic oscillator, the eigenvalues should be of the form (n+0.5) * omega
    expected_eigenvalues = torch.tensor([(i + 0.5) * omega for i in range(n)])
    assert torch.allclose(eigenvalues, expected_eigenvalues, atol=1e-5)
