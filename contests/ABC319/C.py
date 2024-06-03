from itertools import permutations

# 入力をリストに変換する関数
def input_to_list():
    data = []
    for _ in range(3):
        data += list(map(int, input().split()))
    return data

# がっかり条件を判定する関数
def is_disappointed(data, perm, judge):
    for a, b, c in judge:
        if (data[a] == data[b] and perm[a] < perm[c] and perm[b] < perm[c]) or \
           (data[a] == data[c] and perm[a] < perm[b] and perm[c] < perm[b]) or \
           (data[b] == data[c] and perm[b] < perm[a] and perm[c] < perm[a]):
            return True
    return False

# 主な処理を行う関数
def main():
    data = input_to_list()
    judge = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    open_positions = list(range(9))

    total = 0
    cnt = 0

    for perm in permutations(open_positions):
        total += 1
        if not is_disappointed(data, perm, judge):
            cnt += 1

    print(cnt / total)

if __name__ == "__main__":
    main()
