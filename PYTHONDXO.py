#!/usr/bin/env python
# coding: utf-8

# # INDENTATION PROGRAM

# In[2]:


if 6>2:
    print("six is greater than two!")


# # KEYWORDS

# In[4]:


for x in range(1,9):
    print(x)
    if x <6:
        continue
    else:
        break
            


# null
# NULL
# Null
# 

# # VALID IDENTIFIERS

# In[ ]:


_RAM
RAM
RAM01


# # INVALID IDENTIFIERS

# In[ ]:


9RAM
RAM TIWARI
RAM#567


# # IDENTIFIERS PROGRAM

# In[7]:


#_myfile,dropxout is a identifier.
_myfile="hello"
dropxout="world"
print(_myfile)
print(dropxout)


# # STRING LITERALS

# In[5]:


A='Dropxout'
B="is"
C=''' a
     learning
            platform'''
print(A)
print(B)
print(C)


# # CHARACTER LITERALS

# In[6]:


A='D'
B ="A"
print(A)
print(B)


# # NUMERIC LITERALS

# In[10]:


A=5 #int
B=34.9 #float
c=3 +7j #complex
print(A)
print(B)
print(C)


# # BOOLEAN LITERALS

# In[11]:


A=(1==True)
B=(1==False)
C=True+4
D=False+7
print(A,B,C,D)


# # SPECIAL LITERALS

# In[18]:


A=None
print(A)


# # LITERALS COLLECTIONS

# # LIST

# In[19]:


Rollno=[1,2,3]
Sname=["Aman","Rohan","Ram"]
print(Rollno)
print(Sname)


# # Tuples

# In[22]:


Fruits=("Apple","Banana","Cherry")
print(Fruits)


# # Dictionary

# In[23]:


Student={"name":"Aman","rollno":"1","class":"5th"}
print(Student)


# # SET

# In[24]:


Fruits={"APPLE","BANANA","CHERRY"}
print(Fruits)


# # OPERATORS

# In[27]:


#Arithmetic operators=
A=5
B=8
print("sum:",a+b)
print("substraction:",a-b)
print("division:",a/b)
print("modulo:",a%b)
print("floor division:",a//b)
print("power:",a**b)


# In[30]:


#Assignment operator
a=9
b=5
a+=b #a=a+b
print(a)


# In[31]:


a=6
b=5
a/=b #a=a/b
print(a)


# In[32]:


#comparison operator
a=8
b=5
print("a==b",a==b) #equal to operator
print("a!=b",a!=b) #not equal to
print("a>b",a>b)   #greater than
print("a<b",a<b)   #less than
print("a>=b",a>=b)  #greater thab or equal to
print("a<=b",a<=b)  #less than or equal to


# In[35]:


#logical operator
print(True and True)
print(True and False)
print(True or False)
print(not True)


# In[1]:


#identity operator
A=["Apple","Cherry"]
B=["Apple","Cherry"]
C=A
print(A is C)
print(A==B)
print(B is C)


# In[6]:


#membership operator
A=["Apple","Cherry"]
print("Apple" in A)


# In[7]:


A=["apple","cherry"]
print("banana" not in A)


# # SIMPLE INPUT AND OUTPUT

# In[8]:


name=input("enter student name:")
print("Tiwari"+name)
print(type(name))


# # DATA TYPES

# In[9]:


#string
A="Dropxout"
print(A)
print(type(A))
#INT
A=5
print(A)
print(type(A))
#FLOAT
A=5.4
print(A)
print(type(A))
#complex
A=5 + 9j
print(A)
print(type(A))


# In[10]:


#list
x=["apple","cherry"]
print(x)
print(type(x))
#tuples
x=("apple","cherry")
print(x)
print(type(x))
#dictionary
Y={"name":"AMAN","rollno":2}
print(Y)
print(type(Y))
#set
Y={"apple","banana"}
print(Y)
print(type(Y))
#frozenset
y=frozenset({"apple","cherry"})
print(y)
print(type(y))


# In[11]:


X=True
print(X)
print(type(X))


# # MUTUABLE

# In[14]:


#APPEND
Rollno=[1,2,3]
Rollno.append(4)
print(Rollno)
#insert
Rollno.insert(1,6)
print(Rollno)
#remove
Rollno.remove(3)
print(Rollno)


# # IMMUTUABLE

# In[15]:


A=(0,1,2,3,4)
A[0]=4
print(A)


# # Variables and Assignment

# In[16]:


NAME="AMIT" # NAME i.e VARIABLES 
CLASS="5TH"# = i.e assignment operator
print(NAME)
print(CLASS)


# # Variable NAME

# In[21]:


#VALID VARIABLE NAME
_file=4
X_="DROPXOUT"
print(_file)
print(X_)


# In[18]:


#INVALID VARIABLE NAME
5G="KUMKUM"
RAM9 0="RAJ"
get_ipython().run_line_magic('TANU', '=5')
print(5G)
print(RAM9 0)
print(%TANU)


# # Python Variables - Assign Multiple Values

# In[19]:


A,B,C=10,20,30
print(A)
print(B)
print(C)


# # Assigning same Values to Multiple Variables

# In[20]:


A=B=C=10
print(A)
print(B)
print(C)


# # OUTPUT VARIABLES

# In[26]:


X="python"
Y="is a"
Z="programming-language"
print(X)
print(Y)
print(Z)


# # GLOBAL VARIABLE

# In[27]:


def fun():
    print("inside function",name)
#GLOBAL SCOPE
name="DROPXOUT"
fun()
print("outside function",name)


# # local variable

# In[28]:


def fun():
    name="Dropxout"
    print(name)
fun()


# # IF/ELSE CONDITION

# In[32]:


X=30
if(X < 25):
    print("X is smaller than 25")
    print("if block")
else:
    print("X is greater than 25")
    print("else block")


# # FOR LOOP

# In[2]:


fruits=["apple","cherry","banana"]
for x in fruits:
    print(x)


# # RANGE()

# In[3]:


list(range(5))


# In[4]:


list(range(10))


# In[5]:


list(range(2))


# # BREAK STATEMENT

# In[8]:


fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x=="banana":
        break


# # continue statement

# In[10]:


fruits=["apple","banana","cherry"]
for x in fruits:
    if x=="banana":
        continue
    print(x)


# # else clause

# In[11]:


a=8
b=7
if b>a:
    print("b is greater than:a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater than b")


# In[14]:


x=5
try:
    x>10
except:
    print("something went wrong")
else:
    print("the 'try' code was executed without raising any errors")


# # pass statement

# In[20]:


#USE PASS KEYWORD IN A FUNCTIONS
def fun():
    pass


# In[21]:


#class
class dog:
    pass


# In[22]:


#if
a=50
b=62
if b>a:
    pass


# # COMMENTS

# In[ ]:


#single line comments
'''python is 
a programming
language'''


# In[29]:


def fun()


# # FUNCTION

# In[31]:


def fun():
    print("hello")
fun()


# # Argunments 

# In[33]:


def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def greet(func):
    greeting=func("hiii")
    print(greeting)
greet(shout)
greet(whisper)


# # ASSERT

# In[36]:


x="hey"
assert x=="hey"
assert x=="by"


# # recursion

# In[38]:


def fac(x):
    if x==1:
        return 1
    else:
        return(x*fac(x-1))
num=6
print("the factorial of",num,"is",fac(num))


# # lambda function

# In[40]:


x=lambda a:a+10
print(x(5))


# In[42]:


#modify
fruits=["apple","cherry"]
fruits[0]="orange"
print(fruits)


# In[43]:


#len
x=len(fruits)
print(x)


# In[45]:


fruit=["apple","cherry","banana"]
x=fruit[2]
print(x)


# # class and objects

# In[46]:


class Employee:
    employee_id=0
employee1=Employee()
employee2=Employee()
employee1.employeeid=1001
print(f"Employee ID:{employee1.employeeid}")
employee2.employeeid=1002
print(f"EMPLOYEE id:{ employee2.employeeid}")


# # date time

# In[48]:


import datetime
x=datetime.datetime.now()
print(x)


# In[49]:


x=min(5,8,9)
y=max(5,8,9)
print(x)
print(y)


# In[51]:


import math
x=math.sqrt(64)
print(x)


# # inheritance in python 

# In[59]:


class Person(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def isEmployee(self):
        return False
class Employee(Person):
    def isEmployee(self):
        return True
emp=Person("ram")
print(emp.getName(),emp.isEmployee())
emp=Employee("rajan")
print(emp.getName(),emp.isEmployee())


# # Encapsulation in python

# In[68]:


class Employee:
    def __init__(self,name,salary,project):
        self.name=name
        self.salary=salary
        self.project=project
    def show(self):
        print("name:",self.name,"salary:",self.salary)
    def work(self):
        print(self.name,"is working on ",self.project)
emp=Employee("Aman",10000,"xyz") 
emp.show()
emp.work()


# # polymorphism 

# In[71]:


class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"im a cat.my name is {self.name}.i am {self.age}years old.")
    def make_sound(self):
        print("meow")
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"im a dog.my name is {self.name},i am {self.age}years old.")
    def make_sound(self):    
        print("bark")
cat1=Cat("chinky",1)
dog1=Dog("tommy",3)

for animal in (cat1,dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()

        
        


# # dir()

# In[75]:


print(dir())
import random
import math
print(dir())


# # numpy

# In[76]:


import numpy as np
arr=np.array((1,2,3,4,5))
print(arr)


# # get the value

# In[84]:


import numpy as np
arr=np.array([1,2,3,4])
print(arr[2])


# # numpy data type

# In[85]:


import numpy as np
x=np.array([1,2,3])
print(x.dtype)


# #  Numpy Copy 

# In[86]:


import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.copy()
arr[0]=6
print(arr)
print(x)


# # View

# In[87]:


import numpy as np
arr=np.array([1,2,3,4])
x=arr.view()
arr[0]=6
print(arr)
print(x)


# # Shape of an array

# In[88]:


import numpy as np
arr=np.array([[1,2,3],[1,2,3]])
print(arr.shape)


# # ITERATE

# In[91]:


import numpy as np
arr=np.array([1,2,3])
for x in arr:
    print(x)


# # NUMPY join ARRAY

# In[92]:


import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2))
print(arr)


# # PANDAS

# In[6]:


import pandas
mydataset={
    "fruits":["orange","apple","cherry"],
"passings":[5,6,8]
}
myvar=pandas.DataFrame(mydataset)
print(myvar)


# # series

# In[7]:


import pandas as pd
x=[5,4,7]
myvar=pd.Series(x)
print(myvar)


# # label

# In[10]:


import pandas as pd
x=[5,8,9]
myvar=pd.Series(x,index=["orange","apple","cherry"])
print(myvar)


# # dataframe

# In[11]:


import pandas as pd
data={
    "rollno":[20,21,22],
    "rank":[1,2,3]
}
df=pd.DataFrame(data)
print(df)


# # Pandas project

# In[13]:


import pandas as pd
df=pd.read_csv("Downloads\data.csv")
print(df.to_string())


# # Return a  new data frame with no empty cell

# In[14]:


import pandas as pd
df=pd.read_csv("Downloads\data.csv")
new_df=df.dropna()
print(new_df.to_string())


# In[16]:


import pandas as pd
df=pd.read_csv("Downloads\data.csv")
df.fillna(145,inplace=True)


# In[17]:


print(df.duplicated())


# In[18]:


df.corr()


# # plotting

# In[19]:


import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Downloads\data.csv")
df.plot()
plt.show()


# # MATPLOTLIB

# In[20]:


import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,6])
y=np.array([0,250])
plt.plot(x,y)
plt.show()


# In[31]:


CITIES=["MUMBAI","PUNE","BANGLORE"]
POPULATION=[50000,56000,85000]
plt.bar(CITIES,POPULATION)
plt.xlabel("cities")
plt.ylabel("population")
plt.show()


# In[32]:


plt.bar(CITIES,POPULATION,width=1/2)


# In[33]:


plt.bar(CITIES,POPULATION,color="red")


# In[34]:


plt.bar(CITIES,POPULATION,color=["red","blue","green"])


# # subplot

# In[38]:


import matplotlib.pyplot as plt
import numpy as np
#plot1
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x,y)

#plot2
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.subplot(1,2,2)
plt.plot(x,y)
plt.show()


# # pie chart

# In[39]:


import matplotlib.pyplot as plt
import numpy as np
y=np.array([10,5,2,33])
plt.pie(y)
plt.show()


# In[40]:


import matplotlib.pyplot as plt
import numpy as np
x=np.array([5,4,7,8,9,5,2,1,6])
y=np.array([45,55,22,44,77,66,99,55,77])
plt.scatter(x,y)
plt.show()


# In[ ]:




