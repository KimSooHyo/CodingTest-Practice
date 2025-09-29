

# 📝 오답 노트: 파괴되지 않은 건물 문제 (2022 KAKAO BLIND)

## 📌 문제 요약

* **N x M** 크기의 맵에 내구도를 가진 건물이 존재한다.
* `skill` 리스트에 따라 특정 직사각형 영역의 건물들이 공격(내구도 감소) 또는 회복(내구도 증가)을 받는다.
* 모든 스킬이 끝난 뒤 **내구도가 1 이상인 건물의 개수**를 구하는 문제이다.

---

## 🚫 처음 풀이 (시간 초과 발생)

```python
def solution(board, skill):
    answer = 0
    
    for s in skill:
        t, r1, c1, r2, c2, degree = s
        n = degree if t == 2 else -degree
        
        for y in range(r1, r2+1):
            for x in range(c1, c2+1):
                board[y][x] += n
    
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] > 0:
                answer += 1
    return answer
```

### ❌ 문제점

* 각 스킬마다 `(r2-r1+1) * (c2-c1+1)` 영역을 **직접 순회**하며 내구도를 갱신.
* 최악의 경우

  * `N = M = 1000`
  * `skill = 250,000`
  * 연산 횟수는 `250,000 * 1,000 * 1,000 = 2.5 * 10^11` → **시간 초과** 🚨

즉, 단순 구현으로는 절대 풀 수 없는 문제였다.

---

## 💡 접근법: 누적합 (Prefix Sum, Imos 방법)

### 📖 누적합이란?

* 배열에 **구간 단위의 변화량만 기록**하고,
* 마지막에 한 번의 **누적 계산**으로 전체 변화를 반영하는 기법.
* 예: 1차원 배열에서 `[l, r] 구간에 +k`를 하고 싶다면

  * `arr[l] += k`, `arr[r+1] -= k` 로 기록
  * 이후 `prefix sum`을 돌리면 각 위치에 최종 변화량이 반영됨.

이 문제는 2차원 배열이므로, **2차원 누적합**을 적용한다.

---

## ✅ 최종 풀이

```python
def solution(board, skill):
    answer = 0
    N, M = len(board), len(board[0])
    
    # 변화량 기록 배열 (여유 공간 포함)
    changes = [[0] * (M+1) for _ in range(N+1)]
    
    # 변화량 기록
    for t, r1, c1, r2, c2, degree in skill:
        d = degree if t == 2 else -degree
        changes[r1][c1] += d
        changes[r1][c2+1] -= d
        changes[r2+1][c1] -= d
        changes[r2+1][c2+1] += d
    
    # 가로 누적합
    for i in range(N):
        for j in range(M):
            changes[i][j+1] += changes[i][j]
    
    # 세로 누적합
    for j in range(M):
        for i in range(N):
            changes[i+1][j] += changes[i][j]
    
    # 최종 결과 계산
    for i in range(N):
        for j in range(M):
            if board[i][j] + changes[i][j] > 0:
                answer += 1
    
    return answer
```

---

## 🔍 복잡도 분석

* 스킬 처리: `O(K)` (K = skill 길이)
* 누적합 계산: `O(N*M)`
* 최종 결과 계산: `O(N*M)`
* 전체 시간 복잡도: `O(N*M + K)`
  → **효율성 통과** 🎉

---

## 📌 배운 점

1. **단순 구현은 시간 초과**가 쉽게 발생할 수 있다.

   * 문제의 입력 크기(`N, M, skill`)를 보고, 단순한 3중 반복문이 가능한지 항상 체크해야 한다.

2. **누적합**은 구간 업데이트 문제에서 강력하다.

   * 변화량을 기록하고, 마지막에 한 번의 누적 연산으로 전체에 반영하는 방식.
   * 1차원 → 2차원으로 확장 가능.

3. **알고리즘 선택의 중요성**

   * 이 문제는 단순 구현이 아니라 **누적합 알고리즘을 아는지**를 묻는 문제였다.

---

## ✨ 정리

* 처음 풀이는 **직접 모든 구간을 순회 → 시간 초과**
* 효율적으로 풀기 위해 **2차원 누적합(구간 업데이트)** 기법 사용
* **O(N*M + K)** 로 최적화 성공
