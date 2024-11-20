from solution import Solution


def test_palindrome():
    assert Solution().isPalindrome(121)


def test_negative():
    assert not Solution().isPalindrome(-121)


def test_not_palindrome():
    assert not Solution().isPalindrome(10)
