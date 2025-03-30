def cntSubarraysWithXor(arr, k):
  d = {0: 1}
  temp = 0
  cnt = 0
  for it in arr:
    temp ^= it
    if temp^k in d:
      cnt += d[temp^k]
    if temp in d:
      d[temp] += 1
    else:
      d[temp] = 1
  return cnt

testCases = [
  ([4, 2, 2, 6, 4], 6),
  ([5, 6, 7, 8, 9], 5)
]
for arr, k in testCases:
  print(cntSubarraysWithXor(arr, k))
