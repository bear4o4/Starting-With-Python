print("Python")

"""Variables-DataTypes"""

num=1.5
print(num,"and type:", type(num))

num2=1.5
print(num2,"and type:", type(num2))
num3='hello'
print(num3,"and type:", type(num3))

"""Take data input from user"""

num1=int(input("Enter Number"))
print(num1,"and type",type(num1))

#Type of data
print(type(num1))

"""Type Conversion"""

num2=int(num1)
print(type(num2))

"""**IF-ELSE**"""

num1=int(input("enter value of num1"))
if num1>5:
  print("num1>5")
elif num1<=5 and num1>=3:
  print("num1 between 3 & 5")
else:
  print("num1 <3")

"""IF-ELIF-ELSE"""

opr=input("Operator +,-:") #str
num1=int(input("Enter num1: ")) #int
num2=int(input(" Enter num2: ")) #int
if opr=='+':
  print("Add: ",num1+num2)
elif opr=='-':
  print("Subtract: ",num1-num2)
elif opr=='*':
  print("Multiplication:",num1*num2)
else:
  print("invalid operator")

"""**Loop: While, For**"""

#While Loop : (Condition)

n=4
while n>0:
  print(n)
  n=n-1
print("End!!!!!!!!!!")

#For Loop (Range(start,stop,step))
sum=0
for i in range(4,0,-1):
  sum=sum+i
print(sum)

#Nested Loop # To print/calculate table of 2 and 3
for i in range(2,4,1):
  #inner loop #it iterates on num (for table of 2 and 3)
  print("Table of: ", i)
  for j in range(1,11,1): # calculate table of each num defined by outer loop
    print(i,"x",j,"=",i*j,"\t")

"""**Strings Operation**

"""

str1='Python'
str2='Programming'
str3='Lecture'
str4= str1+" "+str2+" "+str3
print(str4)

str1="hello"
print(len(str1))
str2='k'+str1[1:5]
print( str2)



s = "abcdefgh"
print("s[0:len(s)-2:1]",s[0:len(s)-2:1])
print("s[::-1]",s[::-1])

print("s[4:1:-1]",s[4:1:-1])

s='hello'
#s[0] = 'y'
s = 'y'+s[1:len(s)]

sum=0
for i in range(5,11,2):
  if sum==7:
    sum=sum+i
    print("iin if part")
    break
  sum=i #sum+1
  print(sum)

"""## **Control Statements**"""

######### Break ############
sum=0
for i in range (0,10,1):
    sum=sum+i
    if sum == 6:  # Break the loop when the number is 5
        print("Number 6 found! Exiting the loop.")
        break
    print("Number is not 6.",i)

print("Loop has ended.")

######### Continue ############
sum=0
for i in range (0,10,1):
    sum=sum+i
    if sum == 6:
        print("Number 6 found! Skip this iteration in the loop.")
        continue
    print("Number is not 6.",i)

print("Loop has ended.")

######### pass ############
sum=0
for i in range (0,10,1):
    if i%2 == 0:
        pass
    else:
      print("Number is not even.",i)

print("Loop has ended.")

"""### **Define Function**"""

#Define Function
def f(x):
  print(x*2)

#Call Function
f(5)

def f( x ):
  x = x + 1
  print('in f(x): x =', x)
  return x

x = 3
z = f( x )
print(x,z)

#Define Function Number Even or ODD
def isEven(num):
  if num%2==0:
    return 1
  return 0

ans=isEven(5)
if ans==1:
  print("number is Even")
else:
  print("number is Odd")

def f(y):
  x = 1
  x += 1
  print(x)


x = 5
f(x)
print(x)

def g(y):
  print(x,x-1)
x = 5
g(x)
print(x)

def h(y):
  y += 1


x = 5
h(x)
print(x)



"""## **LIST**"""

L1=[1,2,3]
L1[2]='hello'

L = [2, 'a', 4, "ab"]
print(len(L))
print(L[0])
print(L[2]+1)
print(L[3])

i=2
print(L[i-1] )
print(L[4])

"""# **Update List**"""

L=[2, 1, 3]
L[1] = 5

#Iterate our list
sum1=0
for i in L:
  sum1=sum1+i
  print("sum:",sum1)

#Add elements
L1=[1,2,3]
L1.append(4)
print("Updated L1:",L1)

#Extend List
L1=[2,1,3]
L2=[4,5,6]
L3=L1 + L2
print("L3:",L3)
print("Updated L1:",L1.extend([0,3,4]))

#Remove List
L = [2,1,3,6,3,7,0] # do below in order
L.remove(2)
print(L )
L.remove(3)
print(L)
del(L[1])
print(L)
print(L.pop())

