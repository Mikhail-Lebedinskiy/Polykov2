n = int(input())
a = int(input())
b = int(input())

a, b = min(a, b), max(a, b)

if a + b == n + 2 and a >= 3:
    print("YES")
elif a + b == n + 3 and a >= 3:
    print("YES")
elif a + b == n + 4 and a >= 3:
    print("YES")
else:
    print("NO")
