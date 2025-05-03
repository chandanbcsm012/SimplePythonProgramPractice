# * * * * * * * 
#  * * * * * * 
#   * * * * * 
#    * * * * 
#     * * * 
#      * * 
#       * 
#      * * 
#     * * * 
#    * * * * 
#   * * * * * 
#  * * * * * * 
# * * * * * * * 

n = 7
for i in range(2 * n - 1):
    count = n - i if i < n else i - n + 2
    spaces = " " * (n - count)
    print(f"{spaces}{'* ' * count}".rstrip())