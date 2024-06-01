def solve(N, M):
    MOD = 998244353
    total_sum = 0
    bit_length = max(N.bit_length(), M.bit_length())

    for bit in range(bit_length):
        bit_mask = 1 << bit
        if M & bit_mask:
            full_cycles = (N + 1) // (2 * bit_mask)
            remaining = (N + 1) % (2 * bit_mask)

            total_sum += full_cycles * bit_mask
            total_sum += max(0, remaining - bit_mask)

    result = total_sum % MOD
    return result

N, M = map(int, input().split())

print(solve(N, M))
