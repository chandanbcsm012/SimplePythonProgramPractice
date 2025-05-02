#               * 
#             * * 
#           * * * 
#         * * * * 
#       * * * * * 
#     * * * * * * 
#   * * * * * * * 

n = 7

for i in range(n):
    for j in range(n-i):
        print(" ", end=" ")

    for k in range(1, i+2):
        print("*", end=" ")
    print()