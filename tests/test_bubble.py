from ..algorithms.bubble_sort import bubble_sort


def test_bubble():
    """Test bubble_sort"""
    the_list = [-1, 3, 1, 2, 5, 4]
    got = bubble_sort(the_list)
    want = [-1, 1, 2, 3, 4, 5]
    assert got == want
