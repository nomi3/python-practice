N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [0] * N
for i in range(N):
  X[i] = list(map(int, input().split()))

Y = [list(i) for i in zip(*X)]

for i in range(M):
  if sum(Y[i]) < A[i]:
    print("No")
    exit()
print("Yes")