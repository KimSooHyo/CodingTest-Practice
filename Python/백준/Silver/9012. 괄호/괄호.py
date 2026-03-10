n = int(input())

for _ in range(n):
    stack = []
    line = input().strip()
    for l in line:
        if not stack:
            stack.append(l)
        else:
            if l == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(l)

    if stack:
        print("NO")
    else:
        print("YES")