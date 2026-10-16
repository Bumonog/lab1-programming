import math

print(f"{'X':>8} {'sin(x)':>10}")
print('-' * 28)

for i in range(1,11):
    x = i * math.pi/10
    y = math.sin(x)
    print(f"{x:8.4} {y:10}")