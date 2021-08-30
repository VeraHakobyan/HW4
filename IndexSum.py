N = int(input())
A = []

for _ in range(N):
    A.append(float(input()))

M = int(input())
IND = []

for _ in range(M):
    IND.append(int(input()))

index_sum = 0

for el in IND:
    index_sum += A[el]

print(index_sum)
