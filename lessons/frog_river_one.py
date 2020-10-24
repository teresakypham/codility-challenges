# There is also issue with single element arrays with brute force soln...
# def solutionBrute(X, A):
#     # A = [ 1, 3, 1, 4, 2, 3, 5, 4]
#     N = len(A)
#     count = [0] * (X+1)
    
#     for i in range(N-1):
#         count[A[i]]+=1
#         for j in range(1, X+1):
#             if count[j] > 0 and j != X:
#                 continue
#             elif count[j] > 0 and j == X:
#                 return i
#             else:
#                 break
    
#     return -1

def solutionEff(X, A):
    N = len(A)
    indexMarkers = [-1] * (X+1)

    for i in range(N):
        if indexMarkers[A[i]] == -1:
            indexMarkers[A[i]] = i

    for i in range(1,X+1):
        if indexMarkers[i] == -1:
            return -1
    
    return max(indexMarkers)

if __name__=="__main__":
    # print(solutionBrute(5, [ 1, 3, 1, 4, 2, 3, 5, 4]))
    print(solutionEff(5, [ 1, 3, 1, 4, 2, 3, 5, 4]))
    print(solutionEff(5, [3]))
    print(solutionEff(1, [1]))
    print(solutionEff(2, [1, 1, 1, 1]))