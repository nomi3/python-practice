H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
row_sum = []
for i in range(H):
	row_sum.append(sum(A[i]))
col_sum = []
for i in range(W):
	col_sum.append(sum(A[j][i] for j in range(H)))

for i in range(H):
	for j in range(W):
		print(row_sum[i] + col_sum[j] - A[i][j], end=" ")
	print()