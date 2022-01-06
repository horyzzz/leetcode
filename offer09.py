"""
    用两个栈实现队列
"""
class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def appendTail(self, value: int) -> None:
        self.stack1.append(value)


    def deleteHead(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        if not self.stack1:
            return -1
        while self.stack1:
            self.stack2.append(self.stack1.pop())
            print(self.stack1)
        return self.stack2.pop()

            



# Your CQueue object will be instantiated and called as such:
# ["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
obj = CQueue()
print(obj.deleteHead(), obj.appendTail(5), obj.appendTail(2), obj.deleteHead(), obj.deleteHead())
