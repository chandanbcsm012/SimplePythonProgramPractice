#               A 
#             A B 
#           A B C 
#         A B C D 
#       A B C D E 
#     A B C D E F 
#   A B C D E F G 

n = 7

for i in range(n):
    for j in range(n-i):
        print(" ", end=" ")
    for k in range(i+1):
        print(chr(65+k), end=" ")
    print()