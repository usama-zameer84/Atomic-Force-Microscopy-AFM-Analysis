import pytest
from afm_analysis.slope_estimator import estimate_slope

def test_estimate_slope():
    curve = [0, 1, 2, 3, 4]
    s = [0, 1, 4, 9, 16]
    slope = estimate_slope(curve, s)
    assert slope is not None
