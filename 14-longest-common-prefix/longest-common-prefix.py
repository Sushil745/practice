class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs : 
            return " "
        
        # use the first strung as a baseline reference 
        base = strs[0]
        for i in range (len(base)):
            #check the character as index i acrosss all other strings 
            for string in strs[1 : ]:
                #if out of bounds or characters , return the prefix up to index i
                if i >= len(string) or string[i] != base[i]:
                    return base [: i]

        return base 
