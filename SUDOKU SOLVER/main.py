class Solution:
    #function to print grids of sudoku
    def printGrid(self,arr):
        for i in range(9):
            for j in range(9):
                print(arr[i][j],end="")

    #function for rows matches the given number
    def used_in_row(self,arr,row,num):
        for i in range(9):
            if arr[row][i]==num:
                return True
        return False
    #funcyion for col matches the given number
    def used_in_col(self,arr,col,num):
        for i in range(9):
            if arr[i][col]==num:
                return True
        return False

    #function for 3x3 box matches the given number
    def used_in_box(self,arr,row,col,num):
        for i in range(3):
            for j in range(3):
                if arr[i+row][j+col]==num:
                    return True
        return False
    #function to indicate whether it will be legal to assign num to the given row and col
    def check_location(self,arr,row,col,num):
        return not self.used_in_row(arr,row,num) and not self.used_in_col(arr,col,num) and not self.used_in_box(arr,row-row%3,col-col%3,num)

    def find_empty_location(self,arr,l):
        for row in range(9):
            for col in range(9):
                if arr[row][col]==0:
                    l[0]=row
                    l[1]=col
                    return True
        return False
    def solveSudoku(self,grid):
        l[0,0]
        if not self.find_empty_location(grid,l):
            return True
        row=l[0]
        col=l[1]
        #consider digits from 1 to 9
        for num in range(1,10):
            if self.check_location(grid,row,col,num):
                grid[row][col]=num
                if self.solveSudoku(grid):
                    return True
                grid[row][col]=0
        return False
if __name__=="__main__":
    t=int(input())
    while t>0:
        gird=[[0 for i in range(9)]for j in range(9)]
        row=[int(x) for x in input().strip().split()]
        k=0
        for i in range(9):
            for j in range(9):
                grid[i][j]=row[k]
                k+=1
        ob=Solution()
        if ob.Solution(grid)==True:
            ob.printgrid(grid)
            print()
        else:
            print("No solution ")
        t=t-1
        