class MaxQueue:

    def __init__(self):
        self.queue = []
        self.sub_q = []

    def max_value(self) -> int:
        if not self.queue:
            return -1
        return self.sub_q[0]

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        self.sub_q.append(value)
        self.sub_q.sort(reverse=True)

    def pop_front(self) -> int:
        if not self.queue:
            return -1
        self.sub_q.remove(self.queue[0])
        return self.queue.pop()



# Your MaxQueue object will be instantiated and called as such:
obj = MaxQueue()
param_1 = obj.max_value()
obj.push_back(2)
param_3 = obj.pop_front()