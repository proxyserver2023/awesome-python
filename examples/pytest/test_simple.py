def inc(value):
    """takes a value and increment by 1

    Arguments:
        value {int} -- the number to increment

    Returns:
        int -- the increased number
    """

    return value+1


def test_answer():
    assert inc(10) == 12
