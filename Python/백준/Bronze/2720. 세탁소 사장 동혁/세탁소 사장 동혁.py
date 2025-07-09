"""
쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)의 개수
"""

t = int(input())
for _ in range(t):
    c = int(input())
    quarter = c // 25
    c %= 25
    dime = c // 10
    c %= 10
    nickel = c // 5
    c %= 5
    penny = c // 1
    
    print(quarter, dime, nickel, penny)