import heapq

def to_minutes(time_str):
    h, m = map(int, time_str.split(":"))
    return h * 60 + m

def solution(book_time):
    # 시간을 분 단위로 변환
    times = [(to_minutes(s), to_minutes(e)) for s, e in book_time]
    
    # 시작 시간 기준 정렬
    times.sort(key=lambda x: x[0])
    
    # 최소 힙 (방마다 청소까지 끝나는 시간 저장)
    rooms = []
    
    for start, end in times:
        if rooms and rooms[0] <= start:  
            # 가장 빨리 끝난 방 재사용
            heapq.heappop(rooms)
        # 새로운 방 or 재사용 방을 청소 끝난 시간으로 업데이트
        heapq.heappush(rooms, end + 10)
    
    return len(rooms)
