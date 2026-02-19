# Main objective is to find output without running code
string="Scan#List!"
new_str=""
c=len(string)
for i in range(c):
       if string[i].isalpha()==False:
              new_str+="*"
       elif string[i].isupper()==True:
              new_str+=chr(ord(string[i])+1)
       else:
              new_str+=string[i+1]
print(f"New string {new_str}")