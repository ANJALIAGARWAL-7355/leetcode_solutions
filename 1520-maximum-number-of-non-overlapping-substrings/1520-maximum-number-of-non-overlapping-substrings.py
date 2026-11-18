
class Solution(object):
    def maxNumOfSubstrings(self, s):
        first = {}
        last = {}

        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        res = []

        for i, ch in enumerate(s):
            if i != first[ch]:
                continue

            right = last[ch]
            j = i

            while j <= right:
                c = s[j]

                if first[c] < i:
                    break

                right = max(right, last[c])
                j += 1

            if j > right:
                if not res or i > res[-1][1]:
                    res.append([i, right])
                elif right < res[-1][1]:
                    res[-1] = [i, right]

        return [s[l:r+1] for l, r in res]
