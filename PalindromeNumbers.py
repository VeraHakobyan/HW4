def palindrome(n):
    nstr = str(n)
    reverse = nstr[-1::-1]
    if nstr == reverse:
        return True


a = int(input())
b = int(input())

for i in range(a, b+1):
    if palindrome(i):
        print(i)
