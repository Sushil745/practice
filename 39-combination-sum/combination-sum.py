class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        
        def backtrack(remain, current_combination, start_index):
            if remain == 0:
                result.append(list(current_combination))
                return
            for i in range(start_index, len(candidates)):
                if candidates[i] > remain:
                    break
                
                current_combination.append(candidates[i])
               
                backtrack(remain - candidates[i], current_combination, i)
                current_combination.pop()
                
        backtrack(target, [], 0)
        return result  