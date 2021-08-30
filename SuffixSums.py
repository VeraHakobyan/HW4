A = [1, 2, 3, 4, 5]
B = []

for i in range(len(A)):
    new_elem = 0
    for j in range(i, len(A)):
        new_elem += A[j]
    B.append(new_elem)
print(B)
