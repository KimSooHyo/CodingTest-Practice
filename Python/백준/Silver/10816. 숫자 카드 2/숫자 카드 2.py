import sys
input = sys.stdin.readline

card_list = {}
N = int(input())
N_list = list(map(str, input().split()))

for n in N_list:
    if n in card_list:
        card_list[n] += 1
    else:
        card_list[n] = 1

M = int(input())
M_list = list(map(str, input().split()))

for m in M_list:
    if m not in card_list:
        print(0, end = ' ')
    else:
        print(card_list[m], end = ' ')