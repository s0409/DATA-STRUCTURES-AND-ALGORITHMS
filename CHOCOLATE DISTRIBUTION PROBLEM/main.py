def chocolate(arr,n,m):
    #if there are no chocolates and number of students
    if n==0 or m==0:
        return 0
    arr.sort()
    #if students are more than chocolates
    if n<m:
        return -1
    #largest chocolates
    min_diff=arr[n-1]-arr[0]
    for i in range(n-m+1):

        min_diff=min(min_diff,arr[i+m-1]-arr[i])
    return min_diff
if __name__ == "__main__":
    arr = [12, 4, 7, 9, 2, 23, 25, 41,
          30, 40, 28, 42, 30, 44, 48,
          43, 50]
    m = 7 # Number of students
    n = len(arr)
    print("Minimum difference is", chocolate(arr, n, m))