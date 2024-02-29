import numpy as np
from qham.FHM.fhm import HubbardModel  

def test_hubbard_model_initialization():
    model = HubbardModel(num_sites=2, t=1.0, U=2.0)
    assert model.num_sites == 2
    assert model.t == 1.0
    assert model.U == 2.0
    assert model.H.shape == (16, 16)  # 4^num_sites

def test_hamiltonian_diagonalization():
    model = HubbardModel(num_sites=2, t=1.0, U=2.0)
    energies, _ = model.diagonalize()
    assert len(energies) == 16  # Ensure we have the correct number of energy levels
    assert np.all(np.diff(energies) >= 0)  # Ensure energy levels are sorted

def test_hamiltonian_symmetry():
    model = HubbardModel(num_sites=2, t=1.0, U=2.0)
    # The Hamiltonian should be Hermitian, meaning it equals its own transpose
    assert np.allclose(model.H, model.H.T)

def test_plot_energy_levels_runs():
    model = HubbardModel(num_sites=2, t=1.0, U=2.0)
    energies, _ = model.diagonalize()
    # Test simply runs the function to ensure no errors; it doesn't check the plot output
    model.plot_energy_levels(energies)
    assert True  # If the function runs without errors, this test passes