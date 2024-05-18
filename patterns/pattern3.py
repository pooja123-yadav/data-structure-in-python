# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15 

def pattern1(n):
  row = 1
  num = 1
  while(row<=n):
    col = 1
    while(col<=row):
      print(num, end=" ")
      col = col + 1
      num = num +1
    
    row = row +1
    print("\r")

pattern1(n=5)

#            1 
#          2 3 
#        4 5 6 
#      7 8 9 10 
# 11 12 13 14 15 

def pattern2(n):
  row = 1
  num = 1
  while(row<=n):
    for i  in range(0,n-row):
        print(f" ",end=" ")
    col = 1
    while(col<=row):
      print(f"{num} ", end=" ")
      col = col + 1
      num = num +1
    
    row = row +1
    print("\r")

pattern2(n=5)
