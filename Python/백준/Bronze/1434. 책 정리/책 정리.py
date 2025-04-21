
n,m = map(int, input().split())
box = [0] * n
book = [0] * m

idx = 0

boxes = list(map(int, input().split()))
books = list(map(int, input().split()))

for book in books:
    if boxes[idx] >= book:
        boxes[idx] -= book
    else:
        idx += 1
        boxes[idx] -= book
        
waste = sum(boxes)
print(waste)