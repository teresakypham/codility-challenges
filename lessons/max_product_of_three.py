def solution(A):
    A.sort()
    N = len(A)
    
    # Need to consider case where two negative multiples = positive
    return max(A[N-1] * A[N-2] * A[N-3], A[0] * A[1] * A[N-1])

if __name__ == "__main__":
    print(solution([-3,1,2,-2,5,6]))
    print(solution([-5,-5,5,4]))
    print(solution([-2,4,1,6]))