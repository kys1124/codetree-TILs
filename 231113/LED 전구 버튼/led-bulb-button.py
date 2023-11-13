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

S = []
idx  = 0
for _ in range(B):
    arr = press(arr)
    if tuple(arr) in S:
        idx = S.index(tuple(arr))
        S  = S[idx:]
        arr = S[(B-idx)%(len(S))-1]
        break
    else:
        S.append(tuple(arr))

for x in arr:
    print(x)