def solution(A):

    N = len(A)

    prefixSums = [0] * (N+1)
    cars = 0

    # Note: Prefix sum captures the sum of the elements BEFORE it
    # Be careful of fence errors
    for i in range(1,N+1):
        prefixSums[i] = prefixSums[i-1] + A[i-1]

    # print(prefixSums)

    for i in range(N-1):
        if A[i] == 0:
            if i == 0:
                cars = cars + prefixSums[N]
            else:
                cars = cars + (prefixSums[N] - prefixSums[i])
            
        if cars > 1000000000:
            return -1 

    return cars

if __name__ == "__main__":
    print(solution([0,1,0,1,1]))
    print(solution([1,0,1,1,0]))
    print(solution([1]))