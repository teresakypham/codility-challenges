# O(N^2) brute solution
# def solutionBrute(A):
#     N = len(A)
#     maxProfit = 0

#     for i in range(N):
#         price = A[i]
#         for j in range(i+1, N):
#             maxProfit = max(maxProfit, A[j] - price)

#     return maxProfit

def solutionEff(A):
    N = len(A)

    if N == 0 or N == 1:
        return 0

    maxProfit = 0
    price = A[0]

    for i in range(1,N):
        price = min(price, A[i])
        maxProfit = max(maxProfit, A[i] - price)

    return maxProfit

if __name__ == "__main__":
    print(solutionEff([23171, 21011, 21123, 21366, 21013, 21367]))
    print(solutionEff([]))
    print(solutionEff([23171]))
