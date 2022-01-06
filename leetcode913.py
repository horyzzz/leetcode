draw = 0
mouse_win = 1
cat_win = 2


class Solution:
    def catMouseGame(self, graph) -> int:
        n = len(graph)
        dp = [[[-1] * (n * 2) for _ in range(n)] for _ in range(n)]

        def getResult(mouse: int, cat: int, turns: int) -> int:
            if turns == n * 2:
                return draw
            res = dp[mouse][cat][turns]
            if res != -1:
                return res
            if mouse == 0:
                return mouse_win
            elif cat == mouse:
                return cat_win
            else:
                res = getNextResult(mouse, cat, turns)
            dp[mouse][cat][turns] = res
            return res

        def getNextResult(mouse, cat, turns):
            curMove = mouse if turns % 2 == 0 else cat
            defaultRes = mouse_win if curMove != mouse else cat_win
            res = defaultRes

            for next in graph[curMove]:
                if curMove == cat and next == 0:
                    continue
                nextMouse = next if curMove == mouse else mouse
                nextCat = next if curMove == cat else cat
                nextRes = getResult(nextMouse, nextCat, turns + 1)
                if nextRes != defaultRes:
                    res = nextRes
                    if res != draw:
                        break

            return res

        return getResult(1, 2, 0)


s = Solution()
graph = [[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]
res = s.catMouseGame(graph)
