N, B = map(int, input().split())
arr = []
dic = {0:1,1:0}
for _ in range(N):
    arr.append(int(input()))

def press(arr):
    copy_arr  = arr[:]
    for i in range(N):
        if copy_arr[(i-1)%N]==1:
            arr[i] = dic[arr[i]]
    return arr

for _ in range(B):
    arr = press(arr)
for x in arr:
    print(x)