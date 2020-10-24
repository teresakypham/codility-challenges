def solution(A, K):
    
    N = len(A)

    if N == 0:
        return A

    i = 0
    while i < K:
        last = A[N-1]
        for j in range(1,N):
            A[-j] = A[-j-1]
        
        A[0] = last
        i+=1

    return A
        

if __name__ == "__main__":
    print(solution([3, 8, 9, 7, 6], 3))
    print(solution([0, 0, 0], 1))
    print(solution([1, 2, 3, 4], 4))
    print(solution([1], 100))
    print(solution([], 4))
    print(solution([3, 8, 9, 7, 6], 8))