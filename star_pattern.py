'''
Docstring for star_pattern
Triangel patters using stars * 
Using 6 Rows
'''
def star_triange(row):
              for i in range(row):
                     for j in range(row-i-1):
                            print(" ",end="")
                     for j in range(2*i+1):
                            print("*",end="")
                     print()
star_triange(500)