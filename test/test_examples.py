import pytest


def test_pass():
    # Denne test vil passere
    assert 1 + 1 == 2


def test_fail():
    # Denne test vil fejle
    assert 1 * 1 == 3


@pytest.mark.skip(reason="Springes over med vilje")  # Denne test bliver slet ikke kørt
def test_skip():
    pass


def test_crash():
    # Denne test crasher med en exception
    raise RuntimeError("Test crashede med vilje")


# 4 nye unit tests

def test_fail_with_message():
    # Fejler med vilje med en sjov besked
    pytest.fail("Jeg nægter at tage et bad i dag")


def test_crash_zero_division():
    # Crasher med klassikeren
    _ = 1 / 0


def test_skip_runtime():
    # Skipper sig selv midt i testen
    pytest.skip("Springer over fordi jeg lige skulle hente kaffe")


@pytest.mark.xfail(reason="Kendt bug: 2 + 2 burde være 5 (i min verden)")
def test_xfail_expected_fail():
    # Forventet fail (xfail) = flot gul status i output
    assert 2 + 2 == 5
