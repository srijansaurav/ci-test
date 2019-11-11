from . import a


def test_calculate():
    res = a.calculate(1,2)
    assert res == 3
