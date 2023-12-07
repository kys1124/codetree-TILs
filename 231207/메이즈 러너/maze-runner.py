N,M,K = map(int, input().split()) #NxN 0빈칸 1~9내구도 M명 참가자
arr = [list(map(int, input().split())) for _ in range(N)]
player ={}
pos = {}
for i in range(1,M+1):
    r,c = map(lambda x:int(x)-1, input().split())
    player[i] = (r,c)
    pos[(r,c)] = [i]

ei,ej = map(lambda x:int(x)-1, input().split())

ans = 0
def find_square():
    for l in range(2, N):
        for si in range(N - l + 1):
            for sj in range(N - l + 1):
                flag1, flag2 = False, False
                for i in range(l):
                    for j in range(l):
                        ci, cj = si + i, sj + j
                        if (ei, ej) == (ci,cj):
                            flag1 = True
                        if pos.get((ci, cj)):
                            flag2 = True
                if flag1 and flag2:
                    return si,sj,l

for _ in range(K):
    new_pos = {}
    for i in range(1,M+1):
        if player.get(i):
            ci,cj =player[i]
            dist = abs(ci-ei)+abs(cj-ej)
            mi,mj = ci,cj
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj =ci+di,cj+dj
                if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0:
                    nxt_dist = abs(ni-ei)+abs(nj-ej)
                    if dist>nxt_dist:
                        dist = nxt_dist
                        mi,mj = ni,nj

            if (ci,cj)!=(mi,mj):
                ans+=1

            if (mi,mj)==(ei,ej):
                del player[i]
                continue
            else:
                if new_pos.get((mi,mj)):
                    new_pos[(mi,mj)].append(i)
                else:
                    new_pos[(mi,mj)] = [i]
                player[i] = (mi,mj)

    pos = new_pos

    if not player:
        break

    ci,cj,cl = find_square()
    new_arr = [arr[i][:] for i in range(N)]
    for i in range(cl):
        for j in range(cl):
            new_arr[ci+i][cj+j] = arr[ci+(cl-1-j)][cj+i]
            if new_arr[ci+i][cj+j]>0:
                new_arr[ci+i][cj+j]-=1

    arr = new_arr

    new_pos = {}
    for key,value in pos.items():
        si,sj = key
        if ci<=si<=ci+cl-1 and cj<=sj<=cj+cl-1: #같이 회전.
            ni,nj = ci+ (sj-cj) ,cj+cl-1-(si-ci)

            for v in value:
                player[v] = (ni,nj)
            new_pos[(ni,nj)] = value
        else:
            new_pos[key] = value
    pos = new_pos
    ei,ej = ci+(ej-cj), cj+cl-1-(ei-ci)

print(ans)
print(ei+1,ej+1)