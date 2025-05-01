# A B C D E F G 
#  A B C D E F 
#   A B C D E 
#    A B C D 
#     A B C 
#      A B 
#       A 

n = 7

for i in range(n):
    for j in range(i):
        print(" ", end="")
    for k in range(n-i):
        print(chr(65+k), end=" ")
    print()