class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        myList = []
        for i in operations:
            if i == "D":
                myList.append(2 * myList[-1])
            elif i == "C":
                myList.pop()
            elif i == "+":
                myList.append(myList[-1] + myList[-2])
            else:
                myList.append(int(i))
        return sum(myList)