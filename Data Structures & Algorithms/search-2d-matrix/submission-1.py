class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix[0])
        column=len(matrix)
        for i in range(column) :
            if matrix[i][-1] >= target  :
                left,right=0,row-1
                while left <= right :
                    if matrix[i][left] == target or matrix[i][right] == target  :
                        return True
                    if matrix[i][left] < target :
                        left+=1
                    if matrix[i][left] > target :
                        right-=1
        return False

                            

    
