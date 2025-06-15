class Solution:
    def isPalindrome(self, s: str) -> bool:
        val = "".join(char.lower() for char in s if char.isalnum())
        left = 0
        right = len(val) - 1

        while(left <= right):
            if val[left] != val[right]: return False
            else: 
                left+=1
                right-=1
        return True