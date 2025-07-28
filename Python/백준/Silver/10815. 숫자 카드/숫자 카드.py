import sys
input = sys.stdin.readline

N = int(input())
card_list = list(map(int, input().split()))
card_list = set(card_list)
M = int(input())
M_list = list(map(int, input().split()))

for c in M_list:
    if c in card_list:
        print(1, end=' ')
    else:
        print(0, end=' ')