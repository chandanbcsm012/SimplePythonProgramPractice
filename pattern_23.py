# A  B  C  D  E  F  G 
# A  B  C  D  E  F 
# A  B  C  D  E 
# A  B  C  D 
# A  B  C 
# A  B 
# A 
# A  B 
# A  B  C 
# A  B  C  D 
# A  B  C  D  E 
# A  B  C  D  E  F 
# A  B  C  D  E  F  G

n = 7
total_rows = 2 * n -1

for i in range(total_rows):
    count = n -i if i < n  else i - n +2
    print(*[chr(65+j)+ " " for j in range(count)])