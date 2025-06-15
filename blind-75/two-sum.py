class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for index, number in enumerate(nums):
            if target - number in map:
                return [map[target - number], index]
            map[number] = index