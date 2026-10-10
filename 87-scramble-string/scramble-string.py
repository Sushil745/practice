class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        memo = {}
        
        def dp(s1, s2):
            if s1 == s2:
                return True
            
            if sorted(s1) != sorted(s2):
                return False
                
            key = (s1, s2)
            if key in memo:
                return memo[key]
                
            n = len(s1)
            for i in range(1, n):
                # Condition 1: Without swapping
                if dp(s1[:i], s2[:i]) and dp(s1[i:], s2[i:]):
                    memo[key] = True
                    return True
                
                # Condition 2: With swapping (Moved inside the loop)
                if dp(s1[:i], s2[n-i:]) and dp(s1[i:], s2[:n-i]):
                    memo[key] = True
                    return True
            
            memo[key] = False
            return False
            
        return dp(s1, s2)
