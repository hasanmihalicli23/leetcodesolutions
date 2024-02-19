class Solution(object):
    def containsDuplicate(self, nums):
        mySet = set()
        
        for i in nums:
            if i in mySet:
                return True
            mySet.add(i)
        return False
