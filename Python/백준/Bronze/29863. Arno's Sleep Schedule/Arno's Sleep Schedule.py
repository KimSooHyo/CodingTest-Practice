sleep = int(input())
wakeup = int(input())
if sleep >= 20:
    print(24-sleep + wakeup)
else:
    print(wakeup-sleep)