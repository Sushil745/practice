class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Since the array is sorted, the first element is always unique.
        # we start writing unique elements from index 1.
        write_index = 1
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous one, it's unique
            if nums[i] != nums[i - 1]:
                nums[write_index] = nums[i]
                write_index += 1
                
        # The write_index represents the total count of unique elements
        return write_index
