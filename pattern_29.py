# A B C D E F G
#  A B C D E F
#   A B C D E
#    A B C D
#     A B C
#      A B
#       A
#      A B
#     A B C
#    A B C D
#   A B C D E
#  A B C D E F
# A B C D E F G

n = 7
for i in range(2 * n - 1):
    count = n - i if i < n else i - n + 2
    spaces = " " * (n - count)
    chars = " ".join(chr(65 + j) for j in range(count))
    print(f"{spaces}{chars}")