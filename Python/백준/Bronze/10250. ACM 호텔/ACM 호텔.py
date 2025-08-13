t = int(input())

for _ in range(t):
    h,w,n = map(int, input().split())
    floor = n%h
    ho = (n//h)+1
    if floor == 0:
        floor = h
        ho = n // h

    print(f"{floor}{ho:02d}")