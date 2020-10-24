def solution(N):

    binary = bin(N)[2:]
    gap=0
    boundary=0
    gaps = []
    for i in binary:
        if i == '0':
            gap+=1
        else:
            boundary+=1
            gaps.append(gap)
            gap = 0
    if boundary > 1:
        gaps = sorted(gaps)
        return gaps[-1]
    else:
        return 0

if __name__ == "__main__":
    print(solution(9))
    print(solution(529))
    print(solution(1041))
    print(solution(32))
    print(solution(483647))
    print(solution(1073741825))