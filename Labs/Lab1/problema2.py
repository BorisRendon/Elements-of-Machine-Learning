cache = {}
def eq(n, m):
    if f'{n,m}' in cache:
        return cache[f'{n,m}']
    if m==n:
        return 1
    if m==0:
        return 1
    resultado = cache[f'{n,m}'] = eq(n-1, m) + eq(n-1, m-1)
    return resultado
print(eq(50, 35))
print(eq(100, 85))