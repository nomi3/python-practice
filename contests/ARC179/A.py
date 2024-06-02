def can_be_good_sequence(K, A):
    if K > 0:
        A.sort()
        return True, A
    else:
        if sum(A) < K:
            return False, []
        else:
            A.sort(reverse=True)
            return True, A

N, K = map(int, input().split())
A = list(map(int, input().split()))

is_possible, result = can_be_good_sequence(K, A)
if is_possible:
    print("Yes")
    print(" ".join(map(str, result)))
else:
    print("No")
