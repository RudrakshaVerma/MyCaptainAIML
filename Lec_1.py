"""x=2899635.265213
y=446843521.82
z= x+y
print ("THE SUM OF X AND Y IS: ",z)


#string methods
#concetenate two strings
strx="Hello! How are you?"
stry=" How are you doing?"
strz=strx+stry
print(strz)

strv=strx.capitalize()
print("Converting to upper case: ", strv)
print(strx.index('H'))

print('Replace the substring', strx.replace('hello','Hi',1))"""


"""efining a list
x=[1,27,53,179,175]
#print(x)
y=list(range(1,110,13*2))
y.append(1)
#y.append(y*2)
#y.pop()
#y.remove(x)
#z=x.__add__(y*2)
#y.reverse()
#x.extend(y)
mul=[2*x for x in (y)]
print(y)
#print(y.count(1))
print(x)
print(mul)
#z.remove(x)
#print(z)

t2=(111,34,23,44)
t1=(3,4,8)
t4=(36,53)
t3=t1.__add__(t2).__add__(t4)
print(t3)

from collections import namedtuple
Employee=namedtuple('Employee',['EmpNo','Age','Department'])
E1=Employee("Rudy","26","Kaand karna")
E2=Employee("Jaadu","25","Sustana")
print(getattr(E1,'Age'))
print(getattr(E2,'Department'))

s1=(1,2,3,4,5,6)
s2=(33,44,55)
s=set(s1)
s3=(s2*2 for s3 in (s1))
s.add(s3)
print(s)

a=3
b=5
print("a is greatest") if a>b else print("a is less than b") if a<b else print("a is equal")


i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 1
while i < 6:
    i += 1
  if i == 3:

    continue

    print(i)
"""
