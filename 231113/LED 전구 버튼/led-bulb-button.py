N, B = map(int, input().split())
arr = []
dic = {0:1,1:0}
S =  set()
for _ in range(N):
    arr.append(int(input()))
origin = arr[:]

def press(arr):
    copy_arr  = arr[:]
    for i in range(N):
        if copy_arr[(i-1)%N]==1:
            arr[i] = dic[arr[i]]
    return arr

S.add(tuple(arr))
for _ in range(B):
    arr = press(arr)
    if tuple(arr) in S:
        break
    else:
        S.add(tuple(arr))

arr = origin
if tuple([0]*N) not in S:
    for idx in range(B%len(S)):
        arr = press(arr)

    for x in arr:
        print(x)
else:
    for _ in range(len(arr)):
        print(0)