import sys

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    results = []
    
    for _ in range(3):  # 총 3개의 테스트 셋
        N = int(data[index])  # 정수의 개수
        index += 1
        
        total_sum = 0
        
        for _ in range(N):
            total_sum += int(data[index])
            index += 1
            
        if total_sum > 0:
            results.append("+")
        elif total_sum < 0:
            results.append("-")
        else:
            results.append("0")
    
    # 결과 출력
    print("\n".join(results))

if __name__ == "__main__":
    main()
