f = open("17-4.txt")
arr = []
brr = []
srar = 0
for line in f:
    arr.append(line[:-1])
srar = sum([int(i) for i in arr]) / len(arr)
for i in range(len(arr) - 2):
    if int(arr[i]) < srar or int(arr[i+1]) < srar or int(arr[i+2]) < srar:
        if "9" in arr[i] and "9" in arr[i+1] and "9" in arr[i+2]:
            brr.append(int(arr[i]) + int(arr[i+1]) + int(arr[i+2]))
print(len(brr), max(brr))
f.close()




