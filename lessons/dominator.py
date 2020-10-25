# Make sure you read the question properly, we need to retirn the INDEX from the ORIGINAL array

def solution(A):
    N = len(A)
    
    if N == 0: return -1
    if N == 1: return 0
    B = A.copy()
    A.sort()
    count = 0
    val = A[N//2]
    
    for i in range(N):
        if B[i] == val:
            count+=1
            index = i

    if count > N//2:
        return index
    else:
        return -1

if __name__ == "__main__":
    print(solution([3,4,3,2,3,-1,3,3]))
    print(solution([1]))
    print(solution([]))
    print(solution([1, 2, 1]))

