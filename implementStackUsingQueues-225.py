from collections import deque 

class MyStack(object):

    def __init__(self):
        self.myQueue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.myQueue.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        for i in range(len(self.myQueue) - 1):
            self.myQueue.append(self.myQueue.popleft())
        return self.myQueue.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.myQueue[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.myQueue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()