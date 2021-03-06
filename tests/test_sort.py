from ..algorithms.bubble_sort import bubble_sort
from ..algorithms.selection_sort import selection_sort
from ..algorithms.merge_sort import merge_sort
from hypothesis import given
import hypothesis.strategies as some
import pytest


@given(some.lists(some.integers()))
def test_bubble_sort(a_list):
    """Test bubble_sort"""
    got = bubble_sort(a_list)
    want = sorted(a_list)
    assert got == want


@given(some.lists(some.integers()))
def test_selection_sort(a_list):
    """Test selection_sort"""
    got = selection_sort(a_list)
    want = sorted(a_list)
    assert got == want


@given(some.lists(some.integers()))
def test_merge_sort(a_list):
    """Test selection_sort"""
    print(a_list)
    got = merge_sort(a_list)
    want = sorted(a_list)
    if got != want:
        pytest.fail(f"got {got} want {want}")
