def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def V_N_mod(N):
    MOD = 998244353
    N_str = str(N)
    len_N = len(N_str)

    power_10_len_N = pow(10, len_N, MOD)
    power_10_len_NN = pow(power_10_len_N, N, MOD)

    numerator = (power_10_len_NN - 1) % MOD
    denominator = (power_10_len_N - 1) % MOD

    denominator_inv = modinv(denominator, MOD)

    result = (N * numerator % MOD) * denominator_inv % MOD
    return result

N = int(input())
print(V_N_mod(N))