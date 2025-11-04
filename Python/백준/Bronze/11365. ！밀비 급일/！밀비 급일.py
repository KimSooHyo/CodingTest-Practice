import sys

while True:
    text = sys.stdin.readline().strip()
    if text == "END":
        break
    print(text[::-1])