A, B = map(int, input().split())
users = [1, 2, 3]
if A in users:
    users.remove(A)
if B in users:
    users.remove(B)

if len(users) == 1:
    print(users[0])
else:
    print(-1)