class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        res = []
        cnt = m * n
        c = 0
        j = 0
        i = 0
        i_start = 1
        i_end = m - 1
        j_start = 0
        j_end = n - 1
        j_direction = i_direction = 1
        while c < cnt:
            while j_start <= j <= j_end:
                res.append(matrix[i][j])
                j += j_direction
                c += 1
            if j > j_end:
                j_direction = -1
                j_end = j_end - 1
                j -= 1
                i += 1
            elif j < j_start:
                j_direction = 1
                j_start = j_start + 1
                j += 1
                i -= 1

            # if j_start < 0 or j_end >= m or c >= cnt:
            #     break

            while i_start <= i <= i_end:
                res.append(matrix[i][j])
                i += i_direction
                c += 1
            if i > i_end:
                i_direction = -1
                i_end -= 1
                i -= 1
                j -= 1
            elif i < i_start:
                i_direction = 1
                i_start += 1
                i += 1
                j += 1

            # if i_start < 0 or i_end >= n or c >= cnt:
            #     break
        
        return res

sol = Solution()
matrix = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
print(sol.spiralOrder(matrix=matrix))       
            
            

            
            

        