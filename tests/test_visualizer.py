import pytest
from afm_analysis.visualizer import plot_force_distance_curve

def test_plot_force_distance_curve():
    curve = [0, 1, 2, 3, 4]
    slope = 1.0
    plot_force_distance_curve(curve, slope)
    assert True  # No errors should be raised
