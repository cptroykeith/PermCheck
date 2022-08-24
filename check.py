def solution(A):
    if len(A)==0:
        return 0
    A.sort()
    for i in range(0,len(A)):
        if A[i]!=(i+1):
            return 0
    
    return 1