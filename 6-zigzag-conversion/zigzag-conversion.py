class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Base case: if there's only 1 row or rows exceed string length, return as is
        if numRows == 1 or numRows >= len(s):
            return s
            
        # FIX: Initialize with empty strings "", not spaces " "
        rows = [""] * numRows
        current_row = 0
        going_down = False
        
        # Iterate through each character in the string
        for char in s:
            rows[current_row] += char
            
            # FIX: Indent these lines so they run INSIDE the loop
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
                
            # FIX: Indent this line so current_row updates after every character
            current_row += 1 if going_down else -1
            
        # Combine all rows into a single string
        return "".join(rows)
