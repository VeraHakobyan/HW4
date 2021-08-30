def is_prime(n):
    prime = True
    for number in range(2, n):
        if n % number == 0:
            prime = False
            break
    return prime


even_number = int(input())

for i in range(2, even_number):
    if is_prime(i) and is_prime(even_number-i):
        print(i, even_number - i)
        break
