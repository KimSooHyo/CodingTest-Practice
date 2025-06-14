def solution(s):
    answer = 0
    n = len(s)
    
    for i in range(n):
        stack = []
        for j in range(n):
            # 괄호 문자열을 회전시키면서 참조
            c = s[(i+j) % n]
            if c == '(' or c=='{' or c == '[': #열린 괄호는 푸시
                stack.append(c)
            else:
                if not stack: #스택이 비어있는 경우
                    break
                
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c== '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    break
        else: #for문이 break에 의해 끝나지 않고 끝까지 수행된 경우
            if not stack:
                answer += 1
    return answer