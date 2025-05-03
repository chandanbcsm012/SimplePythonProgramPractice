# * * * * * * * 
#   * * * * * * 
#     * * * * * 
#       * * * * 
#         * * * 
#           * * 
#             * 
#           * * 
#         * * * 
#       * * * * 
#     * * * * * 
#   * * * * * * 
# * * * * * * * 

n= 7

total_rows = 2 * n -1

for i in range(total_rows):
    count = n-i if i < n  else i - n+2
    spaces = "  "* (n - count)
    print(spaces + "* "* count)
