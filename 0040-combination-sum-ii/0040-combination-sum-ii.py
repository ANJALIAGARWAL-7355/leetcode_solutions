class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []

        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # No point continuing
                if candidates[i] > target:
                    break

                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return result