#       1
#      1 2
#     1 2 3
#    1 2 3 4
#   1 2 3 4 5
#  1 2 3 4 5 6
# 1 2 3 4 5 6 7
#  1 2 3 4 5 6
#   1 2 3 4 5
#    1 2 3 4
#     1 2 3
#      1 2
#       1

n = 7
total_rows = 2 * n - 1
for i in range(total_rows):
    count = i+1 if i < n else total_rows - i
    spaces = " " * (n - count)
    print(spaces, end="")
    print(*range(1, count+1))