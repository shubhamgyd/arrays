def count(arr, m):
  low = 0
  high = len(arr)-1
  while low <= high:
    mid = low + (high-low)//2
    if arr[mid] <= m:
      low = mid + 1
    else:
      high = mid - 1
  
  return low

def check(mat, mid):
  cnt = 0
  for it in mat:
    cnt += count(it, mid)
  return cnt

def matrixMedian(mat):
  n = len(mat)
  m = len(mat[0])
  req = (n*m)//2
  # print(req)
  low = 1
  high = 10
  while low <= high:
    mid = (low + high)//2
    cnt = check(mat, mid)
    print(mid)
    if cnt <= req:
      low = mid + 1
    else:
      high = mid - 1
  return low

if __name__=="__main__":
  mat = [
    [1, 4, 9],
    [2, 6, 7],
    [3, 8, 9]
    ]
  print(matrixMedian(mat))