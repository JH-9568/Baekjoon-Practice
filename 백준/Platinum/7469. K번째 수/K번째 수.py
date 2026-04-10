import sys
from bisect import bisect_right

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

tree = [[] for _ in range(4 * n)]

def build(node, start, end):
    if start == end:
        tree[node] = [arr[start]]
        return
    mid = (start + end) // 2
    build(node * 2, start, mid)
    build(node * 2 + 1, mid + 1, end)
    left = tree[node * 2]
    right = tree[node * 2 + 1]
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])
    tree[node] = merged

def query(node, start, end, l, r, x):
    if r < start or end < l:
        return 0
    if l <= start and end <= r:
        return bisect_right(tree[node], x)
    mid = (start + end) // 2
    return query(node * 2, start, mid, l, r, x) + query(node * 2 + 1, mid + 1, end, l, r, x)

build(1, 0, n - 1)
vals = sorted(arr)
out = []

for _ in range(m):
    i, j, k = map(int, input().split())
    l, r = i - 1, j - 1
    lo, hi = 0, len(vals) - 1
    ans = vals[0]
    while lo <= hi:
        mid = (lo + hi) // 2
        cnt = query(1, 0, n - 1, l, r, vals[mid])
        if cnt >= k:
            ans = vals[mid]
            hi = mid - 1
        else:
            lo = mid + 1
    out.append(str(ans))

print('\n'.join(out))