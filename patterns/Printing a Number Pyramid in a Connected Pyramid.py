# 1234567

#  234567

#   34567

#   4567

#     567

#      67

#       7

def pattern(n):
    row = 1
    while(row<=n):
        col = row
        for i in range(0,row-1):
            print(' ', end=" ")
            
        while(col<=n):
            print(col, end=" ")
            col = col + 1
        row = row + 1
        print("\r")

n= 7
pattern(n)
             
        
     
