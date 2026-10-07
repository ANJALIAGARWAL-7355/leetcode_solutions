class Solution(object):
    def getPermutation(self, n, k):
        nums = [str(i) for i in range(1, n + 1)]
        k -= 1
        ans = ""

        for i in range(n, 0, -1):
            fact = 1
            for j in range(1, i):
                fact *= j

            index = k // fact
            ans += nums[index]
            nums.pop(index)
            k %= fact

        return ans