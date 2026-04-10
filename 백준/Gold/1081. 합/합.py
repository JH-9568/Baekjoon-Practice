import sys

def get_digit_sum(n):
    if n < 0: return 0
    
    counts = [0] * 10
    start = 1
    cur_start = 0
    
    def add_digits(num, multiplier):
        while num > 0:
            counts[num % 10] += multiplier
            num //= 10

    while cur_start <= n:
        while n % 10 != 9 and cur_start <= n:
            add_digits(n, start)
            n -= 1
        
        if n < cur_start:
            break
            
        while cur_start % 10 != 0 and cur_start <= n:
            add_digits(cur_start, start)
            cur_start += 1
            
        cnt = (n // 10 - cur_start // 10 + 1)
        for i in range(10):
            counts[i] += cnt * start
            
        cur_start //= 10
        n //= 10
        start *= 10
        
    total = 0
    for i in range(10):
        total += i * counts[i]
    return total

l, u = map(int, sys.stdin.readline().split())
print(get_digit_sum(u) - get_digit_sum(l - 1))