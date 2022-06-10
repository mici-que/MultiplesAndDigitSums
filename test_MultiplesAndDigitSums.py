from MultiplesAndDigitSums import main

# 1 initial test and input validation
def test_NoInput():
    """If no parameters passed, return False"""
    param = None
    assert main() == False


def test_StringInput():
    """Wrong input type passed, return False"""
    param = "string"
    assert main(param) == False


def test_FloatInput():
    """Wrong input type passed, return False"""
    param = 11.5
    assert main(param) == False


def test_OutOfRange():
    """Input is out of range, return False"""
    param = 101
    assert main(param) == False


def test_OutOfRangeNeg():
    """Input is out of range, return False"""
    param = -1
    assert main(param) == False


def test_CorrectInput():
    """Input is correct, expecting integer return value"""
    param = 10
    assert isinstance(main(param), int) == True


# 2 CALCULATION


def test_Thirty():
    """30 should return 18"""
    param = 30
    assert main(param) == 18


def test_Twelve():
    """12 should return 72"""
    param = 12
    assert main(param) == 72


def test_FortyNine():
    """49 should return 30"""
    param = 49
    assert main(param) == 30


def test_Zero():
    """0 should return 0"""
    param = 0
    assert main(param) == 0
