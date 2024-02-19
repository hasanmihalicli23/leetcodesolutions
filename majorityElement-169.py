class Solution(object):
    def majorityElement(self, nums):
        result = 0 
        count = 0

        for i in nums:
            if count == 0:
                result = i
            if result == i:
                count += 1
            else:
                count -= 1
        return result