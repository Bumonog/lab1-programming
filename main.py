n = 5

# rectangle
print("Rectangle:")
for i in range(n):
    print("*" * n)
    
# triangle
print("\nTriangle:")
for i in range(1, n+1):
    print("*" * i)
    
# Christmas tree
print("\nChristmas tree:")
for i in range(1, n+1):
    print( " " * (n - i) + "*" * (2*i-1) )
    
# romb
print("\nRomb:")
for i in range(1, n+1):
    print( ' '*(n-i) + "*"*(2*i-1) )
for i in range(n-1, 0, -1):
    print(' '*(n-i) + "*"*(2*i-1))