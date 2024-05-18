# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

def pattern1(n):
  row = 1
  while(row<=n):
    col = 1
    while(col<=row):
      print(col, end=" ")
      col = col + 1
    
    row = row +1
    print("\r")

pattern1(n=5)
