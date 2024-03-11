import pytest

@pytest.fixture(scope="module")
def myFixture():
    print("setup method")
    yield "hii"
    print("teardown method")

@pytest.mark.scope
def test_m1(myFixture):
    assert len(myFixture) == 3


def test_m2(myFixture):
    assert "h" in myFixture


@pytest.mark.sample
def test_m3(myFixture):
    assert myFixture == "hii"