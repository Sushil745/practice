class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #base cases : negative numbers and numbers ending in 0 ( expert  0 itself)
        #cannot be palindromws 
        if x < 0 or (x % 10 == 0 and x != 0 ):
            return False 

        reversed_half = 0
        #reverse the digits of the secondhalf of the number 
        while x > reversed_half :
            reversed_half = reversed_half * 10 + x % 10 
            x //= 10

        #for even-length numbers : x ==reversed_half
        #for odd_length numbers : x == reversed_half // half 10 (removes the middle digits )
        return x == reversed_half or x == reversed_half // 10        