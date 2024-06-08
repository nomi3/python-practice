S = input()
upper = 0
lower = 0
for s in S:
    if s.isupper():
        upper += 1
    else:
        lower += 1
if upper > lower:
    print(S.upper())
else:
    print(S.lower())