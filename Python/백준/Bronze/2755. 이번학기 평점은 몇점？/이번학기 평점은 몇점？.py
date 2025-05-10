grades = {
    "A+": 4.3, "A0": 4.0, "A-": 3.7,
    "B+": 3.3, "B0": 3.0, "B-": 2.7,
    "C+": 2.3, "C0": 2.0, "C-": 1.7,
    "D+": 1.3, "D0": 1.0, "D-": 0.7,
    "F": 0.0
}

n = int(input())

grade_sum =0.0
point_sum =0.0

for i in range(n):
    sub, point, grade = input().split()
    point = int(point)
    grade_sum += grades[grade]*point
    point_sum += point
    
avg = round(grade_sum / point_sum + 1e-8, 2)
print(f"{avg:.2f}")