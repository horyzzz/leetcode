class Solution:
    def lastRemaining0(self, n: int, m: int) -> int:
        if n == 0:
            return None
        nums = list(range(n))
        while len(nums) > 1:
            drop_index = (m + len(nums) - 1) % len(nums)
            nums.pop(drop_index-1)
        return nums[0]

    """
        leetcode题解
        https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/jian-zhi-offer-62-yuan-quan-zhong-zui-ho-dcow/
        dp
        输入 n, m,记此约瑟夫环问题为 「n, m问题」 ,设解（即最后留下的数字）为 f(n) ,则有：

        [n, m]问题」：数字环为 0, 1, 2, ..., n - 10,1,2,...,n−1 ,解为 f(n)f(n) ；
        [n-1, m]问题」：数字环为 0, 1, 2, ..., n - 20,1,2,...,n−2 ,解为 f(n-1)f(n−1) ；
        以此类推……

        对于n,m 问题,首轮删除环中第 m 个数字后,得到一个长度为 n - 1 的数字环。
        由于有可能 m > n ,因此删除的数字为 (m - 1) % n,删除后的数字环从下个数字（即 m % n）开始,
        设m%n ,可得数字环：

            t, t + 1, t + 2, ..., 0, 1, ..., t - 3, t - 2
            t,t+1,t+2,...,0,1,...,t−3,t−2
    
            f(n)=(f(n−1)+t)%n  
            f(1) = 0                                                          
    """

    def lastRemaining(self, n: int, m: int) -> int:
        x = 0
        for i in range(2, n + 1):
            x = (x + m) % i
        return x


sol = Solution()
n = 88
m = 10
print(sol.lastRemaining(n, m))
