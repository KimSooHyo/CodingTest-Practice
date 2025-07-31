def solution(land):
    #각 행마다 이전 행에서의 최대 점수를 더해가며 최대 점수를 구함
    for i in range(1, len(land)):
        for j in range(4):
            #이전 행에서 현재 열의 값을 제외한 나머지 열들 중에서 가장 큰 값을 더함
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    return max(land[-1])