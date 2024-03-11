import pytest

@pytest.mark.skip("For sample purpose")
def test_m1():
    assert 1==1


def test_m2():
    assert True==False


@pytest.mark.skipif(100<2, reason="Conditional statisfied")
def test_m3():
    assert 0 == 0