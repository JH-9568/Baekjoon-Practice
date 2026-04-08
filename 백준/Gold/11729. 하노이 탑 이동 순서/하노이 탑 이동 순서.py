n = int(input())

print(2**n - 1)

def hanoi(n, start, end, temp):
    if n == 1:
        print(start, end)
        return
    
    hanoi(n - 1, start, temp, end)
    print(start, end)
    hanoi(n - 1, temp, end, start)

hanoi(n, 1, 3, 2)