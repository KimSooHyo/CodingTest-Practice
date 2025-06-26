## 📌 문제: 문자열 내 p와 y의 개수

### ✅ 내 풀이

```python
def solution(s):
    p_cnt = 0
    y_cnt = 0
    
    for c in s:
        if c == 'p' or c == 'P':
            p_cnt += 1
        elif c == 'y' or c == 'Y':
            y_cnt += 1
    
    return p_cnt == y_cnt
```

* 설명: 문자열을 한 글자씩 확인하면서 p/P와 y/Y의 개수를 각각 세어 비교.
* 장점: 로직이 명확하고 직관적임.
* 단점: `if` 분기문이 많아 코드가 조금 장황함.

---

### 💡 발견한 더 나은 풀이

```python
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')
```

* `s.lower()`로 전체 문자열을 소문자로 변환해서 p, y만 카운트.
* 불필요한 반복, 분기 없이 한 줄로 깔끔하게 처리.
* 내 풀이보다 간결

---

### 🎯 배운 점 요약

* **파이썬 내장 메서드(`str.lower()`, `str.count()`)를 적극 활용하자.**
* 가독성과 효율을 위해 코드를 줄이려는 습관을 들이자.

---

### 🔁 TODO

* `.lower()`와 `.count()`의 동작 방식 복습
* 비슷한 문자열 처리 문제에서 내장 메서드 우선 생각해보기

---
