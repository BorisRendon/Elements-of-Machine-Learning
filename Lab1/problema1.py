def triangle(n):
    for i in range(n,0,-1):
        for j in range(n-i):
            print(" " , end='\n')
        for j in range(2*i-1):
            print("*",end='\n')

print(triangle(3))
print('')
print(triangle(5))