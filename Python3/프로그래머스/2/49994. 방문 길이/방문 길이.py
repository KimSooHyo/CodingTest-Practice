def is_valid(nx, ny):
    return 0 <= nx <= 10 and 0 <= ny <= 10

def update_location(x,y, dir):
    if dir == 'U':
        y += 1
    elif dir == 'D':
        y -= 1
    elif dir == 'L':
        x -= 1
    elif dir == 'R':
        x += 1
    return x, y

def solution(dirs):
    x, y = 5, 5
    ans = set()
    for dir in dirs:
        nx, ny = update_location(x, y, dir)
        if not is_valid(nx, ny):
            continue
        #한 경로의 두 가지 방향을 모두 추가
        ans.add((x,y,nx,ny))
        ans.add((nx,ny,x,y))
        
        x, y = nx, ny
    return len(ans)/2