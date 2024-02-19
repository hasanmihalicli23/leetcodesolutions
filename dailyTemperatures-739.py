class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        myList = []
        result = [0] * len(temperatures)
        for ix, temperature in enumerate(temperatures):
            while myList and temperature > myList[-1][0]:
                stackTemp, stackIndex = myList.pop()
                result[stackIndex] = ix - stackIndex
            myList.append([temperature,ix])
        return result