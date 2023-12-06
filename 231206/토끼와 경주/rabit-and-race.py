import heapq
Q = int(input()) # 명령어 수
query, N,M, P, *lst = list(map(int, input().split()))
rabbit = []
heapq.heapify(rabbit)
dir = {0:(1,0),1:(-1,0),2:(0,1),3:(0,-1)}
change = {0:1,1:0,2:3,3:2}
d_dic = {}
#우선순위 -> 현재까지 점프 횟수, 서있는 행번호+열번호, 행번호, 열번호, 고유번호
for i in range(0,len(lst),2):
    heapq.heappush(rabbit,(0,0,0,0,lst[i]))
    d_dic[lst[i]] = [lst[i+1],0,0,0] #이동 거리 점수 저장 행 열

#NxM 격자, P 토끼 lst > pid, di 로 이루어짐.

def move(i,j,id):
    move_lst = []
    for cd in (0,1): #상 하
        s = d_dic[id][0] #이동거리
        ci,cj= i,j
        s %= (2 * N - 2)
        for _ in range(3):
            ni,nj = ci+s*dir[cd][0], cj+s*dir[cd][1]
            if 0<=ni<N and 0<=nj<M:
                move_lst.append((ni,nj))
                break
            else:
                if cd==0:
                    s -= N-1-ci
                    ci = N-1
                    cd = change[cd]
                elif cd==1:
                    s -= ci
                    ci = 0
                    cd =change[cd]

    for cd in (2,3): #좌우
        s = d_dic[id][0]  # 이동거리
        ci, cj = i, j
        s %= (2 * M - 2)
        for _ in range(3):
            ni, nj = ci + s * dir[cd][0], cj + s * dir[cd][1]
            if 0 <= ni < N and 0 <= nj < M:
                move_lst.append((ni, nj))
                break
            else:
                if cd == 2:
                    s -= M - 1 - cj
                    cj = M - 1
                    cd = change[cd]
                elif cd == 3:
                    s -= cj
                    cj = 0
                    cd = change[cd]

    add_mij, mi,mj = -1,-1,-1
    for si,sj in move_lst:
        if add_mij<si+sj:
            add_mij,mi,mj = si+sj,si,sj
        elif add_mij==si+sj:
            if mi<si:
                mi,mj = si, sj
            elif mi==si:
                if mj<sj:
                    mj = sj
    return mi,mj

for _ in range(Q-1):
    query, *lst2 = list(map(int, input().split()))
    if query==200: # 경주
        K,S = lst2
        jump_rabbit = set()
        for _ in range(K):
            cur_jump, add_ij, i,j, id = heapq.heappop(rabbit)
            ni,nj = move(i,j,id)
            for key in d_dic.keys():
                if key!=id:
                    d_dic[key][1]+=ni+nj+2
            d_dic[id][2],d_dic[id][3] = ni,nj
            heapq.heappush(rabbit, (cur_jump+1, ni+nj,ni,nj,id))
            jump_rabbit.add(id)
        mx_ij,mi, mj, mx_id = -1,-1,-1,0
        for id in jump_rabbit:
            ci,cj = d_dic[id][2],d_dic[id][3]
            if mx_ij<ci+cj:
                mx_ij,mi,mj,mx_id = ci+cj,ci,cj,id
            elif mx_ij==ci+cj:
                if mi<ci:
                    mi,mj,mx_id = ci,cj,id
                elif mi==ci:
                    if mj<cj:
                        mj,mx_id = cj,id
                    elif mj==cj:
                        if mx_id<id:
                            mx_id = id
        d_dic[mx_id][1]+=S

    elif query==300: #이동거리 변경
        pid_t, L = lst2
        d_dic[pid_t][0]*=L

    else: #최고 토끼 선정 마지막에만 있음.
        ans = 0
        for value in d_dic.values():
            ans = max(ans, value[1])

        print(ans)