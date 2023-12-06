N, M, K = map(int, input().split()) # NxN M플레이어수 K라운드
arr = [list(map(int, input().split()))for _ in range(N)]
gun = {}
for i in range(N):
    for j in range(N):
        if arr[i][j]>0:
            gun[(i,j)] = [arr[i][j]]

dir = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}
change = {0:2,2:0,1:3,3:1}
player = {}
score =[0]*(M+1)
pos = {}
for i in range(1,M+1):
    x,y,d,s= map(int, input().split())
    player[i] = [x-1,y-1,d,s,0]
    pos[(x-1,y-1)] = i

for _ in range(K):
    for i in range(1,M+1):
        ci,cj,cd,cs,cg = player[i]
        ni,nj = ci+dir[cd][0], cj+dir[cd][1]
        if not (0<=ni<N and 0<=nj<N): #격자 밖이라 방향 전환.
            cd = change[cd]
            ni,nj = ci+dir[cd][0], cj+dir[cd][1]

        if not pos.get((ni,nj)): #해당 위치에 다른 사람이 없다.
            ng = cg
            if gun.get((ni,nj)): #해당 위치에 총이 있는지 확인.
                gun[(ni,nj)].sort() #정렬
                if gun[(ni,nj)][-1]>cg: #가장 쎈 총이 내 현재 총보다 쎄다
                    ng = gun[(ni,nj)].pop() # 바꿔치기
                    if cg>0: #내가 총이 있다면
                        gun[(ni,nj)].append(cg) #바꾼 총 바닦에 놓기
                    if len(gun[(ni,nj)])==0: #바닥에 총이 없다.
                        del gun[(ni,nj)] #삭제
            del pos[(ci,cj)] #기존 위치 삭제
            pos[(ni,nj)] = i #새로운 위치 등록
            player[i] = [ni,nj,cd,cs,ng] #플레이어 정보 갱신

        else: # 다른 사람이 있다.
            del pos[(ci,cj)]
            j = pos[(ni,nj)] #상대방 번호
            ni,nj,nd,ns,ng = player[j]
            if cs+cg>ns+ng:
                w,wi,wj,wd,ws,wg = i,ni,nj,cd,cs,cg
                l,li,lj,ld,ls,lg = j,ni,nj,nd,ns,ng
            elif cs+cg<ns+ng:
                w, wi, wj, wd, ws, wg =j,ni,nj,nd,ns,ng
                l, li, lj, ld, ls, lg = i,ni,nj,cd,cs,cg
            else:
                if cs>ns:
                    w, wi, wj, wd, ws, wg = i, ni, nj, cd, cs, cg
                    l, li, lj, ld, ls, lg = j, ni, nj, nd, ns, ng
                else:
                    w, wi, wj, wd, ws, wg = j, ni, nj, nd, ns, ng
                    l, li, lj, ld, ls, lg = i, ni, nj, cd, cs, cg

            score[w] += ws+wg-ls-lg #점수 갱신
            if lg>0: #진사람 총 내려 놓기
                if gun.get((ni,nj)):
                    gun[(ni,nj)].append(lg)
                else:
                    gun[(ni,nj)] = [lg]
                lg = 0

            pos[(ni,nj)] = w
            for _ in range(4):
                lni,lnj = ni+dir[ld][0], nj+dir[ld][1]
                if 0<=lni<N and 0<=lnj<N and not pos.get((lni,lnj)):
                    pos[(lni,lnj)] = l
                    if gun.get((lni, lnj)):
                        gun[(lni, lnj)].sort()
                        lg = gun[(lni,lnj)].pop()
                        if len(gun[(lni,lnj)])==0:
                            del gun[(lni,lnj)]
                    player[l] = [lni,lnj,ld,ls,lg]
                    break
                else:
                    ld = (ld+1)%4

            nwg = wg
            if gun.get((ni,nj)):
                gun[(ni,nj)].sort()
                if gun[(ni,nj)][-1]>wg:
                    nwg = gun[(ni,nj)].pop()
                    if wg>0:
                        gun[(ni,nj)].append(wg)
                if len(gun[(ni,nj)])==0:
                    del gun[(ni,nj)]
            player[w] = [ni,nj,wd,ws,nwg]

print(*score[1:])