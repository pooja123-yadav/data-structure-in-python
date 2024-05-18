# 16 

# 16 14 

# 16 14 12 

# 16 14 12 10 

# 16 14 12 10 8 

# 16 14 12 10 8 6 

# 16 14 12 10 8 6 4 

# 16 14 12 10 8 6 4 2 
# 8,8-8,-1
def pattern(n):
    for i in range(n,0,-1):
        for j in range(n,i-1,-1):
            print(j*2, end=" ")
        print("\r")
