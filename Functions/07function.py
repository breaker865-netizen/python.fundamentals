def set_operations(set_a, set_b):
    union = set_a | set_b  # Union: All unique elements from both sets
    intersection = set_a & set_b  # Intersection: Only elements present in both sets
    complement = set_a - set_b  # Relative Complement: Elements in A but NOT in B

    return {
        "union": union,
        "intersection": intersection,
        "complement_a_minus_b": complement
    }

#A = {1, 2, 3, 4, 5}
#B = {4, 5, 6, 7, 8}
A=[]
B=[]
n=int(input("Enter the number of element :"))
for i in range(n):
       i=int(input("Enter element:"))
       A.append(i)
print(f"First set:{A}")
s=int(input("Enter the number of element :"))
for t in range(s):
      t=int(input("Enter element:"))
      B.append(t)
print(f"Second set:{B}")
set_a=set(A)
set_b=set(B)

results = set_operations(set_a,set_b)

print(f"Union: {results['union']}")             
print(f"Intersection: {results['intersection']}")   
print(f"Complement (A-B): {results['complement_a_minus_b']}") 