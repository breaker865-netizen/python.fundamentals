''' This is how real factorial is calculated in Maths 
0!=1
1!=1
2!=2 X 1
3!=3 X 2 X 1
4!=4 X 3 X 2 X 1
5!=5 X 4 X 3 X 2 X 1
'''
#recursive function
# function call itself until it reach base condition 
# calculate factorial
def factorial(n):
       if(n==1 or n==0):
              return 1
       else:
             return n*factorial(n-1)
n=int(input(">>"))
print(f"factorial of the number is :{factorial(n)}")