from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(signals):
    # 전체 반복 주기 구하기
    total_cycle = 1
    
    for G, Y, R in signals:
        cycle = G + Y + R
        total_cycle = lcm(total_cycle, cycle)
    
    # 1초부터 전체 반복 주기까지 확인
    for t in range(1, total_cycle + 1):
        all_yellow = True
        
        for G, Y, R in signals:
            cycle = G + Y + R
            
            # 현재 신호등의 주기 내 위치
            pos = (t - 1) % cycle + 1
            
            # 노란불이 아니면 실패
            if not (G < pos <= G + Y):
                all_yellow = False
                break
        
        if all_yellow:
            return t
    
    return -1