# 1 2 3 4 5 6 7 
#  1 2 3 4 5 6 
#   1 2 3 4 5 
#    1 2 3 4 
#     1 2 3 
#      1 2 
#       1 


n=7
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for k in range(1, (n+1)-i):
        print(k, end=" ")
    print()