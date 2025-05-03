#        * 
#       * * 
#      * * * 
#     * * * * 
#    * * * * * 
#   * * * * * * 
#  * * * * * * * 
#   * * * * * * 
#    * * * * * 
#     * * * * 
#      * * * 
#       * * 
#        * 


n = 7
for i in range(2 * n - 1):
    count = i + 1 if i < n else 2 * n - 1 - i
    spaces = ' ' * (n - count)
    stars = '* ' * count
    print(f"{spaces}{stars.rstrip()}")
