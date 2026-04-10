n = int(input())
arr = [] 

for _ in range(n):
    arr.append(int(input()))
    
for i in range(n-1):
    for j in range(i + 1, n):
        if arr[j] < arr[i]:
            arr[i], arr[j] = arr[j], arr[i]
            
for num in arr:
    print(num)