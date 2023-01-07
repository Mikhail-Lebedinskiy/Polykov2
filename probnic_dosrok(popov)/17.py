f = open("17.txt")
arr = []
for i in f:
    arr.append(int(i))
a = 10**10
for b in arr:
    if b % 17 == 0 and a > b:
        a = b
ans = 0
for i in range(len(arr) - 1):
    if arr[i] % a == 0 or arr[i+1] % a == 0:
        ans += 1
print(ans)
f.close()