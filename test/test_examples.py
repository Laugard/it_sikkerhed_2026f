import pytest


def test_pass():
    assert 1 + 1 == 2


@pytest.mark.xfail(reason="Denne test skal med vilje fejle (til demo)")
def test_fail():
    assert 1 * 1 == 3


@pytest.mark.skip(reason="Springes over med vilje")
def test_skip():
    pass


@pytest.mark.xfail(reason="Denne test skal med vilje crashe (til demo)")
def test_crash():
    raise RuntimeError("Test crashede med vilje")


# ---------------------------
# 4 nye sjove tests (pipeline OK)
# ---------------------------

@pytest.mark.xfail(reason="Jeg nægter at passere i dag 😈")
def test_fail_with_message():
    pytest.fail("Jeg nægter at passere i dag 😈")


@pytest.mark.xfail(reason="Crashes med vilje (ZeroDivisionError)")
def test_crash_zero_division():
    _ = 1 / 0


def test_skip_runtime():
    pytest.skip("Springer over fordi jeg lige skulle hente kaffe ☕")


@pytest.mark.xfail(reason="Kendt bug: 2 + 2 burde være 5 (i min verden) 😂")
def test_xfail_expected_fail():
    assert 2 + 2 == 5
