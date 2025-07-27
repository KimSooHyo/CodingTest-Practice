def command(arr, i, j, k):
    slice_arr = arr[i-1:j]
    slice_arr.sort()
    
    return slice_arr[k-1]

def solution(array, commands):
    answer = []
    for cmd in commands:
        i,j,k = cmd
        r = command(array, i, j, k)
        answer.append(r)
    return answer