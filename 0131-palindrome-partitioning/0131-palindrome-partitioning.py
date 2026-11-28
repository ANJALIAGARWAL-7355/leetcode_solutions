class Solution(object):
    def partition(self, s):
        res = []
        path = []

        def backtrack(start):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start, len(s)):
                substring = s[start:end + 1]

                if substring == substring[::-1]:
                    path.append(substring)
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return res