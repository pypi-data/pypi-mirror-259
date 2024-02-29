import torch
import pytest
from qham.TFIM.tfim import TFIMSimulation  

def test_tfim_initialization():
    size = 10
    beta = 0.4
    h = 0.05
    steps = 100
    sim = TFIMSimulation(size, beta, h, steps)
    assert sim.size == size
    assert sim.beta == beta
    assert sim.h == h
    assert sim.steps == steps
    assert sim.lattice.shape == (size, size)

def test_tfim_step():
    size = 10
    sim = TFIMSimulation(size, 0.4, 0.05, 100)
    initial_lattice = sim.lattice.clone()
    sim.tfim_step()
    assert not torch.equal(sim.lattice, initial_lattice)  # Expect some changes

def test_run_simulation():
    size = 10
    sim = TFIMSimulation(size, 0.4, 0.05, 1)
    initial_lattice = sim.lattice.clone()
    sim.run_simulation()
    assert not torch.equal(sim.lattice, initial_lattice)  # Expect some changes after running the simulation

def test_plot_lattice_runs():
    size = 10
    sim = TFIMSimulation(size, 0.4, 0.05, 100)
    sim.run_simulation()
    # Test simply runs the function to ensure no errors; it doesn't check the plot output
    sim.plot_lattice()
    assert True  # If the function runs without errors, this test passes
