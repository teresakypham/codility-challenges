# There is also error handling issue with this brute force solution for small elements...
# def solutionBrute(A):
#     N = len(A)
#     diff = []

#     for i in range(N):
#         j = 0
#         sumA = 0
#         sumB = 0
#         while j <= i:
#             sumA+=A[j]
#             j+=1
#         while j < N:
#             sumB+=A[j]
#             j+=1
#         diff.append(abs((sumB - sumA)))

#     return min(diff)

def solutionEff(A):
    N = len(A)
    diff = []
    sums = []
    sum = 0
    for i in range(N-1):
        sum+=A[i]
        sums.append(sum)
    
    sum = 0
    for i in range(1,N):
        sum+=A[-i]
        sums.append(sum)

    for i in range(N-1):
        diff.append(abs((sums[i] - sums[-i-1])))

    return min(diff)

if __name__=="__main__":
    # print(solutionBrute([3,1,2,4,3]))
    print(solutionEff([3,1,2,4,3]))
    print(solutionEff([1,2,3]))
    print(solutionEff([1,2,3,4]))