class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)

        # 1. Find the first decreasing element from the right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2. If possible, find the next greater element
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1

            # Swap
            nums[i], nums[j] = nums[j], nums[i]

        # 3. Reverse the part after i
        left = i + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1