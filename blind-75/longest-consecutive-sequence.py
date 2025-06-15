class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        val = set(nums)
        ret = 0
        for n in nums:
            if (n - 1) not in val:
                seq = 1
                while (n + seq) in val:
                    seq += 1
                ret = max(ret, seq)
        return ret