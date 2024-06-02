def bingo(N, T, A):
    # 2次元のビンゴカードを作成し、ビンゴ達成チェック用のリストを初期化
    row_check = [0] * N
    col_check = [0] * N
    diag1_check = 0
    diag2_check = 0
    marked_positions = set()

    # 数字が宣言された順にチェック
    for turn in range(T):
        num = A[turn]
        i = (num - 1) // N
        j = (num - 1) % N

        # マスをマーク
        marked_positions.add((i, j))
        row_check[i] += 1
        col_check[j] += 1

        if i == j:
            diag1_check += 1
        if i + j == N - 1:
            diag2_check += 1

        # ビンゴ達成チェック
        if row_check[i] == N or col_check[j] == N or diag1_check == N or diag2_check == N:
            return turn + 1

    return -1

# 入力例を処理
N, T = map(int, input().split())
A = list(map(int, input().split()))

# 結果を出力
result = bingo(N, T, A)
print(result)
