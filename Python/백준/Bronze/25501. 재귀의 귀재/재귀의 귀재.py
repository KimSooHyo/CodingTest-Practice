import sys
input = sys.stdin.readline

def recursion(s : str, l : int , r : int):
    global cnt_recursion
    cnt_recursion += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)
    
def isPalindrome(s : str):
    return recursion(s, 0, len(s)-1)

t = int(input())
for i in range(t):
    cnt_isPal = 0
    cnt_recursion = 0
    s = input().strip()
    result = isPalindrome(s)
    print(result, cnt_recursion)