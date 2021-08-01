def find(A,B,m,n,K_req):
    i=0
    j=0
    k=0
    while i<m and j<n:
        if A[i]<B[j]:
            k+=1
            if k==K_req:
                return A[i]
            i+=1
        else:
            k+=1
            if k==K_req:
                return B[j]
            j+=1
    #if B[] is completely traversed
    while i<m:
        if k==K_req:
            return A[i]
        i+=1
    while j<n:
        if k==K_req:
            return B[i]
        j+=1
A = [2, 3, 6, 7, 9]
B = [1, 4, 8, 10]
k = 5;
print(find(A, B, 5, 4, k))