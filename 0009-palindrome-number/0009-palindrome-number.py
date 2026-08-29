class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        reversed_num = num[::-1]

        if num == reversed_num:
            return True
        else:
            return False