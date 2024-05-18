# Printing Numbers in a Reverse Semi-pyramid
# Pattern
# 1 

# 2 1 

# 3 2 1 

# 4 3 2 1 

# 5 4 3 2 1 

# 6 5 4 3 2 1 

# 7 6 5 4 3 2 1 

 
def pattern(n):
    row = 1
    while(row<=n):
        col = row
        while(col>=1):
            print(col, end=" ")
            col = col - 1
        row = row + 1
        print("\r")
      
n= 7        
pattern(n)
             
        
     
