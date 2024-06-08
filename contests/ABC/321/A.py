A = input()

# Aを1文字ずつintにしてリストに格納
A = [int(a) for a in A]

# 隣の要素を比較して後の要素が前の要素以上ならNoを出力
for i in range(len(A)-1):
    if A[i] <= A[i+1]:
        print("No")
        exit()

print("Yes")
