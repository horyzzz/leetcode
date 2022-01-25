# class StockPrice:

#     def __init__(self):
#         self.dic = {}
#         self.cur = 0
#         self.val_list = []

#     def update(self, timestamp: int, price: int) -> None:
#         if timestamp not in self.dic:
#             n = len(self.dic)
#             self.dic[timestamp] = n
#             if timestamp > self.cur:
#                 self.cur = n
#             self.val_list.append(price)
#         else:
#             ind = self.dic[timestamp]
#             self.val_list[ind] = price


#     def current(self) -> int:
#         return self.val_list[self.cur]


#     def maximum(self) -> int:
#         return max(self.val_list)

#     def minimum(self) -> int:
#         return min(self.val_list)

from sortedcontainers import SortedList

class StockPrice:
    def __init__(self):
        self.price = SortedList()
        self.timePriceMap = {}
        self.maxTimestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.timePriceMap:
            self.price.discard(self.timePriceMap[timestamp])
        self.price.add(price)
        self.timePriceMap[timestamp] = price
        self.maxTimestamp = max(self.maxTimestamp, timestamp)

    def current(self) -> int:
        return self.timePriceMap[self.maxTimestamp]

    def maximum(self) -> int:
        return self.price[-1]

    def minimum(self) -> int:
        return self.price[0]


# Your StockPrice object will be instantiated and called as such:
obj = StockPrice()
obj.update(1, 10)
obj.update(2, 5)
param_2 = obj.current()
print(param_2)
param_3 = obj.maximum()
print(param_3)
obj.update(1, 3)
param_4 = obj.maximum()
print(param_4)
obj.update(4, 2)
param_5 = obj.minimum()
print(param_5)
