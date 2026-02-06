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
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
while True:
    try:
        n = int(input(">> "))
        print(f"factorial of the number is: {factorial(n)}")
        break
    except ValueError as e:
        print("Invalid input:", e)
