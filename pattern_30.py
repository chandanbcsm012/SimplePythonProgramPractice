#       A
#      A B
#     A B C
#    A B C D
#   A B C D E
#  A B C D E F
# A B C D E F G
#  A B C D E F
#   A B C D E
#    A B C D
#     A B C
#      A B
#       A

n = 7
total_rows = 2 * n - 1
for i in range(total_rows):
    count = i + 1 if i < n else 2 * n - 1 - i
    spaces = " " * (n - count)
    chars = " ".join(chr(65+j) for j in range(count))
    print(f"{spaces}{chars}")