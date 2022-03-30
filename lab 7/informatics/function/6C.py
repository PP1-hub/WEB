def xor(a, b):
    res = a ^ b
    return res
x, y = map(int, input().split())
print(xor(x, y))