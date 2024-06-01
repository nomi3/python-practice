N, L, R = map(int, input().split())
L_list = [i for i in range(1, L)]
R_list = [i for i in range(R+1, N+1)]
M_list = [i for i in range(R, L-1, -1)]
L_list.extend(M_list)
L_list.extend(R_list)
print(*L_list)