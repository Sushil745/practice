class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) < 1:
            return ""
        
        start, end = 0, 0
        
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome found
            return right - left - 1

        for i in range(len(s)):
            # Case 1: Odd length palindromes (e.g., "aba", center is 'b')
            len1 = expandAroundCenter(i, i)
            # Case 2: Even length palindromes (e.g., "abba", center is between 'b' and 'b')
            len2 = expandAroundCenter(i, i + 1)
            
            # Get the maximum length found at the current center
            max_len = max(len1, len2)
            
            # Update the start and end indices if a longer palindrome is found
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start:end + 1]
