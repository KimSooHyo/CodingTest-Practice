def count_zero(s):
    zero_cnt = s.count('0')
    trans = bin(len(s) - zero_cnt)[2:]
    print(trans)
    return str(trans), zero_cnt

def solution(s):
    answer = []
    times = 0
    total_zero = 0
    while s != '1':
        times += 1
        s, zero_cnt = count_zero(s)
        total_zero += zero_cnt
    return [times, total_zero]