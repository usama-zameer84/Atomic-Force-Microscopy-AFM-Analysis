import pytest
from afm_analysis.data_loader import load_heights, load_force_data

def test_load_heights():
    heights = load_heights('path/to/test_heights.npy')
    assert heights is not None

def test_load_force_data():
    force_data = load_force_data('path/to/test_force.pkl')
    assert isinstance(force_data, dict)
