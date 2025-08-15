import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = sorted(map(int, input().split()))

sequence = []

def backtrack(start):
    if len(sequence) == M:
        print(*sequence)
        return
    for i in range(start, N):
        sequence.append(nums[i])
        backtrack(i)
        sequence.pop()

backtrack(0)