for _ in range(int(input())):
  n = int(input())
  k = (n - 1) // 3 + 2
  if (n - k - k + 1) > 0:
    print(k - 1, k, n - k - k + 1)
  else:
    print(k - 2, k, n - k - k + 2)