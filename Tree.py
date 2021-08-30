def print_line(n):
    for i in range(1, n+1, 2):
        space = int(((n - i) / 2)) * ' '
        star = '*' * i
        print(space + star + space)


number = int(input())
print_line(number)
