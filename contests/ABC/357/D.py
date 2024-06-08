def V_N_mod(N):
    MOD = 998244353
    N_str = str(N)
    len_N = len(N_str)

    power_10_len_N = pow(10, len_N, MOD)
    power_10_len_NN = pow(power_10_len_N, N, MOD)

    numerator = (power_10_len_NN - 1) % MOD
    denominator = (power_10_len_N - 1) % MOD

    denominator_inv = pow(denominator, -1, MOD)

    result = (N * numerator % MOD) * denominator_inv % MOD
    return result

N = int(input())
print(V_N_mod(N))