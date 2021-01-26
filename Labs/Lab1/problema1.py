def triangle(n):
    for i in range(n,0,-1):
        for j in range(0,n-i):
            print(end = ' ')
        
        for j in range (0,i):
            print('*', end=' ')
        print()


print(triangle(4))
print(triangle(5))
print(triangle(6))