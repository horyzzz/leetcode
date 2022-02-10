class Solution:
    """
    https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/solution/jian-zhi-offer-56-i-shu-zu-zhong-shu-zi-tykom/
    """
    def singleNumbers(self, nums):
        x, y = 0, 0
        n, m = 0, 1
        """
        异或运算有个重要的性质,两个相同数字异或为0 ,
        即对于任意整数a有a⊕a=0 。
        因此,若将 nums 中所有数字执行异或运算,
        留下的结果则为出现一次的数字x 
        """
        for num in nums:
            n ^= num
        
        while n & m == 0:
            m <<= 1

        for num in nums:
            if num & m:
                x ^= num
            else:
                y ^= num

        return [x, y] 