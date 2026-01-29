# This function prints * patters like:
'''
*
**
**
***
****
***
****
*****
******

and then repeate it'''
def pattern_():
       n=int(input(">>"))
       for i in range(n+1):
              for j in range(i):
                     j+=i
                     print("*"*(j-1))
              
pattern_()
