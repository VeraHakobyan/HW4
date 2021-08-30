def get_number_of_divisors(n):
    number_of_divisors = 0
    for i in range(1, n+1):
        if n % i == 0:
            number_of_divisors += 1
    return number_of_divisors


a = int(input())
b = int(input())
max_divisor_rich = a

for number in range(a, b):
    if get_number_of_divisors(number) > get_number_of_divisors(max_divisor_rich):
        max_divisor_rich = number

print(max_divisor_rich)
