# 1 2 3 4 5 6 7
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7

n = 7
total_rows = 2 * n - 1

for i in range(total_rows):
    count = n-i if i < n else i-n+2
    print(*range(1, count+1))
