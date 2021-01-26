def diamond(n):
    for i in range(1, n, 2):
        print(" "*(n//2-i//2), "*"*i)
    for i in range(n, 0, -2):
        print(" "*(n//2-i//2), "*"*i)

diamond(7)
print()
diamond(9)
print()
diamond(11)