st=input("Enter a string:")
s2=""
lis=['A','E','I','O','U']
for i in range(len(st)):
       if st[i] in lis:
              s2+=""
       else:
              s2+=st[i]
print("------NEW STRING WITHOUT CAPITAL VOWELS-------")
print()
print(s2)

              