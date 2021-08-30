N = int(input())
k = int(input())
a = []
for _ in range(N):
    a.append(int(input()))

for _ in range(k):
    last_to_first = a[-1]
    for i in range(N-1, 0, -1):
        a[i] = a[i-1]
    a[0] = last_to_first
print(a)
