class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = Counter(nums)

        heap = heapq.nlargest(k, dict.items(), lambda x:x[1])

        ret = []
        for key, value in heap:
            ret.append(key)
        return ret