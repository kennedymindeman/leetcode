class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        value_list = [roman_numerals_dict[character] for character in s]
        sum_ = 0
        for left_value, right_value in zip(value_list, value_list[1:]):
            if left_value < right_value:
                sum_ -= left_value
            else:
                sum_ += left_value

        return sum_ + value_list[-1]
