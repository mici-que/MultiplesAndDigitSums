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
