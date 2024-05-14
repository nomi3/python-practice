N = int(input())
A = list(map(int, input().split()))
Q = int(input())
# inputからQ行のBを取得
B = [int(input()) for _ in range(Q)]

# bisect_leftを自作する
def bisect_left(a:list[int], x:int)->int:
  left, right = 0, len(a)
  while left < right:
    mid = (left + right) // 2
    if a[mid] < x:
      left = mid + 1
    else:
      right = mid
  return left

# Aをソート
A.sort()
# Bの各要素に対して、Aの要素との差分の絶対値の最小値を求める
for b in B:
  # bisect_left: Aの中でbを挿入できる位置を返す
  idx = bisect_left(A, b)
  # idxが0の場合はA[0]が最小値
  if idx == 0:
    print(abs(A[0] - b))
  # idxがNの場合はA[N-1]が最小値
  elif idx == N:
    print(abs(A[N-1] - b))
  # それ以外の場合は、A[idx-1]とA[idx]のどちらがbに近いかを比較
  else:
    print(min(abs(A[idx-1] - b), abs(A[idx] - b)))

