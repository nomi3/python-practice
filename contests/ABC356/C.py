def count_valid_combinations(N, M, K, tests):
    required_keys = []
    for C, keys_used, result in tests:
        keys_mask = sum(1 << (key - 1) for key in keys_used)
        required_keys.append((keys_mask, result))

    def is_valid_combination(bits):
        for keys_mask, result in required_keys:
            correct_keys_count = bin(bits & keys_mask).count('1')
            if result == 'o' and correct_keys_count < K:
                return False
            if result == 'x' and correct_keys_count >= K:
                return False
        return True

    valid_combinations_count = 0
    for bits in range(1 << N):
        if is_valid_combination(bits):
            valid_combinations_count += 1

    return valid_combinations_count

N, M, K = map(int, input().split())
tests = []
for _ in range(M):
    test = list(input().split())
    C = int(test[0])
    keys_used = list(map(int, test[1:C+1]))
    result = test[C+1]
    tests.append((C, keys_used, result))

print(count_valid_combinations(N, M, K, tests))