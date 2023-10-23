import math

'''
a = [1 , 2 , 3 , 5, 6 , 7 , 8 , 9]
z = (len(set(a)))
b = [3 , 4 , 5 , 5 , 7 , 8 , 3]
c = (len(set(b)))
print(z + c)
v = (z & c)
v.sort()
print(v)
'''
'''
a = [1 , 2 , 3 , 5, 6 , 7 , 8 , 9]
b = [3 , 4 , 5 , 5 , 7 , 8 , 3]
z = set(a)
c = set(b)
print(z & c)
'''
'''

a = "1 2 3 4 5 6 7 8 6 4 5 7"
a = a.split()
x=[]
for v in a:
  v=int(v)
  x.append(v)
print(x)
c = set()
for b in x:
  if b in c:
    print('Yes')
  else:
    print('No')
    c.add(b)
    
'''
