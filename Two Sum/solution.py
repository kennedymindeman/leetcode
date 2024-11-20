class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict: dict[int, int] = {}
        for index, num in enumerate(nums):
            compliment = target - num
            if compliment in nums_dict:
                return [nums_dict[compliment], index]

            nums_dict[num] = index

        raise ValueError("Solution not in list")
