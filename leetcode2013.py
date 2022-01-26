from collections import *

class DetectSquares:

    def __init__(self):
        self.dict = defaultdict(Counter)

    def add(self, point) -> None:
        x, y = point
        self.dict[y][x] += 1 

    def count(self, point) -> int:
        res = 0
        x, y = point
        if y not in self.dict:
            return 0
        ycnt = self.dict[y]

        for col, colcnt in self.dict.items():
            if col != y:
                d = col - y
                res += colcnt[x] * ycnt[x+d] * colcnt[x+d]
                res += colcnt[x] * ycnt[x-d] * colcnt[x-d]
        
        return res



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)