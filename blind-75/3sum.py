class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        sortList= sorted(nums)
        for i, a  in enumerate(sortList):

            if i > 0 and a == sortList[i -1]: continue
            left = i + 1
            right = len(sortList) - 1

            while(left < right):
                curr = a + sortList[left] + sortList[right] 
                if curr < 0: left+=1
                elif curr > 0: right-=1
                else: 
                    ret.append([a, sortList[left], sortList[right]])
                    left+=1
                    while sortList[left] == sortList[left - 1] and left < right:
                        left+=1   

        return ret