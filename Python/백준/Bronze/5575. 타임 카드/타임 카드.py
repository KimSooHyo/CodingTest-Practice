for _ in range(3):
    on_h, on_m, on_s, off_h, off_m, off_s = map(int, input().split())
    on_time = on_s + (on_m*60) + (on_h*60*60)
    off_time = off_s + (off_m*60) + (off_h*60*60)
    total_s = off_time - on_time
    ans_h = total_s // (60*60)
    total_s %= 60*60
    ans_m = total_s // 60
    total_s %= 60
    ans_s = total_s
    print(ans_h, ans_m, ans_s)