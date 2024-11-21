from solution import Solution


def test_3():
    assert Solution().romanToInt("III") == 3


def test_58():
    assert Solution().romanToInt("LVIII") == 58


def test_1994():
    assert Solution().romanToInt("MCMXCIV") == 1994
