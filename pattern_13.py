#               1 
#             1 2 
#           1 2 3 
#         1 2 3 4 
#       1 2 3 4 5 
#     1 2 3 4 5 6 
#   1 2 3 4 5 6 7 

n = 7

for i in range(n):
    for j in range(n-i):
        print(" ", end=" ")

    for k in range(1, i+2):
        print(k, end=" ")
    print()