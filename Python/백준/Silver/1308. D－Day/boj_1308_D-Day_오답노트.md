# 📘 오답노트: 백준 1308번 - D-Day

## ❌ 오답 이유 요약

- 문제를 풀기 위해 `datetime` 모듈을 사용했으나,
- `1000년 뒤의 날짜`를 `datetime.date(y1 + 1000, m1, d1)`로 계산하려다
- **연도 범위 초과로 인한 런타임 에러 발생**

---

## ✅ 핵심 개념 정리

### 1. `datetime` 모듈의 역할
- 날짜 간의 차이 계산이나 날짜 형식 처리에 유용함
- `datetime.date(연, 월, 일)` 형식으로 날짜 객체 생성 가능
- 날짜 객체끼리 뺄 수 있고 `.days`로 일 수를 구할 수 있음

### 2. `datetime.date()`의 사용 제한
- Python의 `datetime` 모듈이 지원하는 날짜 범위는 다음과 같음:
0001-01-01 ~ 9999-12-31

python
Copy code
- 따라서 `y1 + 1000`이 10000 이상이면 `ValueError` 발생

---

## 💡 해결 방법 요약

- `1000년 이상 지난 날짜인지` 확인할 때는 **직접 연, 월, 일을 비교**해야 안전함
