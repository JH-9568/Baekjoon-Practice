A, B = map(int, input().split())
C = int(input())

total_minutes = A * 60 + B + C

hour = (total_minutes // 60) % 24

minute = total_minutes % 60

print(hour, minute)