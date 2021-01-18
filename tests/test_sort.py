from ..algorithms.bubble_sort import bubble_sort
from ..algorithms.selection_sort import selection_sort
from hypothesis import given
import hypothesis.strategies as some


@given(some.lists(some.integers()))
def test_bubble(a_list):
    """Test bubble_sort"""
    got = bubble_sort(a_list)
    want = sorted(a_list)
    assert got == want


@given(some.lists(some.integers()))
def test_selection(a_list):
    """Test selection_sort"""
    got = selection_sort(a_list)
    want = sorted(a_list)
    assert got == want
