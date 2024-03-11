import pytest

@pytest.mark.scope
def test_m1():
    assert 1==1


def test_m2():
    assert True==False


@pytest.mark.sample
def test_m3():
    assert 0 == 0