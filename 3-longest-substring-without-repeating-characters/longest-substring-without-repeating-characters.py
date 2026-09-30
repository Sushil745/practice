class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to store the most recent index of each character
        char_map = {}
        max_length = 0
        start = 0
        
        for end in range(len(s)):
            # If the character is already in the window, move the start pointer
            if s[end] in char_map and char_map[s[end]] >= start:
                start = char_map[s[end]] + 1
                
            # Update the last seen index of the character
            char_map[s[end]] = end
            
            # Calculate the maximum length found so far
            max_length = max(max_length, end - start + 1)
            
        return max_length
