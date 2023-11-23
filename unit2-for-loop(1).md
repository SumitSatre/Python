# shorthand method for "if-else statement"



```python
a = 27
b = 5
print("A") if a > b else print("B")
```

    A
    


```python
age=int(input("enter your age : "))
print("Elligible")if age>=18 else print("Not Elligible")
```

    enter your age : 33
    Elligible
    

# Nested if statements
You can have if statements inside if statements, this is called nested if statements.


```python
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
```

    Above ten,
    and also above 20!
    


```python

```

# Elif
The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition". 
it's short for else - if, to test additional conditions apart from the initial test expression.


```python
#  program to find the largest number among the three input numbers


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
 
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3
print("The largest number is",largest)



 

```

    Enter first number: 4
    Enter second number: 5
    Enter third number: 1
    The largest number is 5
    


```python

```


```python
# program to displays the corresponding day of week.

weekday = int(input("Enter weekday day number (1-7) : "))

if weekday == 1 :
    print("\n Monday");

elif weekday == 2 :
    print("\nTuesday")

elif(weekday == 3) :
    print("\nWednesday")

elif(weekday == 4) :
    print("Thursday")

elif(weekday == 5) :
    print("\nFriday")

elif(weekday == 6) :
    print("\nSaturday")

elif (weekday == 7) :
    print("\nSunday")

else :
    print("\nPlease enter weekday number between 1-7.")
```

    Enter weekday day number (1-7) : 6
    
    Saturday
    


```python

```


```python
###    write a prog to enter the marks of a student in four subjects. 
then calculate toal and aggregate, and display the grade obtain by the student . 
if student scores aggregate greater than 75%,then grade is Distiction.
if aggregate is 60>= and <75,then grade is 1st division. 
if aggregate is 50>= and <60,then grade is 2nd division.  
if aggregate is 40>= and <50,then grade is 3rd division.
else the grade is Fail.
```


```python
mark1= int(input("enter your marks"))
mark2= int(input("enter your marks"))
mark3= int(input("enter your marks"))
mark4= int(input("enter your marks"))
total= mark1+mark2+mark3+mark4
aggregate= float(total)/4
if(aggregate>=75):
    print("Distinction")
elif(aggregate>=60 and aggregate<75):
    print("1st division")
elif(aggregate>=50 and aggregate<60):
    print("2nd division")
elif(aggregate>=40 and aggregate<50):
    print("3rd division")
else:
    print("fail")
    


```

    enter your marks10
    enter your marks20
    enter your marks22
    enter your marks11
    fail
    

# Python While Loops

##With the while loop we can execute a set of statements as long as a condition is true.   



```python
#Print i as long as i is less than 10:


i = 1
while i <=10:
  print(i)
  
  i += 1    #i=i+1 
```

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    


```python
# prog to print countdown of a given number.

n= int(input("enter a number"))
while n >= 20:
       print(n,end=' ')
       n = n-1
```

    enter a number44
    44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 


```python
# prog to print the reverse of a number.

num = int(input("enter a number : "))

```


```python

```

# For loop

Python’s for keyword provides a more comprehensive mechanism to constitute a loop. 
The for loop in Python is used to iterate the statements or a part of the program several times.



```python
#  Program to print Numbers 1 to 10 using for loop :
for i in range (1,11):
    print (i *7,end=" ")

```

    7 14 21 28 35 42 49 56 63 70 

#  range function

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number. 
We can also define the start, stop and step size as range (start, stop, step size). Step size defaults to 1 if not provided.
This function does not store all the values in memory, it would be inefficient. So it remembers the start, stop, step size and generates the next number on the go.


# range() Function Examples :


```python
#   Create a sequence of numbers from 0 to 5, and print each item in the sequence:

x = range(6)
for n in x:
  print(n) 


```

    0
    1
    2
    3
    4
    5
    


```python
# Create a sequence of numbers from 10 to 20, and print each item in the sequence :

for n in range(20,30):
    print(n)
  
```

    20
    21
    22
    23
    24
    25
    26
    27
    28
    29
    


```python
#prog to display all leap years from 1900 to 2101.

for i in range(1900,2100,4):
    print(i,end="  ")
```

    1900  1904  1908  1912  1916  1920  1924  1928  1932  1936  1940  1944  1948  1952  1956  1960  1964  1968  1972  1976  1980  1984  1988  1992  1996  2000  2004  2008  2012  2016  2020  2024  2028  2032  2036  2040  2044  2048  2052  2056  2060  2064  2068  2072  2076  2080  2084  2088  2092  2096  

# Break Statement :

If break statement is inside a nested loop (loop inside another loop), break will terminate the innermost loop.
In other words, we can say that break is used to abort the current execution of the program and the control goes to the next line after the loop. 
The break is commonly used in the cases where we need to break the loop for a given condition. 



```python
#example 1:

for letter in 'Python':
    if letter == 'h':
        break
    print('Current Letter :', letter)
 

```

    Current Letter : P
    Current Letter : y
    Current Letter : t
    


```python
# #example 2:

for i in range(1,11):
    if i == 5:
        break   #to stop current iteration of the loop
    print(i,end=" ")
```

    1 2 3 4 


```python

```

# Continue Statement :

The continue statement is used to stop the current iteration of the loop and continues with the next one. 
It is mainly used for a particular condition inside the loop so that we can skip some specific code for a particular condition.



```python
#example 1:
for letter in 'Python':
    if letter == 'h':
        continue    #to stop current iteration of the loop
    print('Current Letter :', letter)
 
```

    Current Letter : P
    Current Letter : y
    Current Letter : t
    Current Letter : o
    Current Letter : n
    


```python
#example 2:
for i in range(1,11):
    if i == 5:
        continue    #to stop current iteration of the loop
    print(i,end=" ")
 
```

    1 2 3 4 6 7 8 9 10 


```python

```

# pass statement
The pass statement is used as a placeholder for future code.
When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
Empty code is not allowed in loops, function definitions, class definitions, or in if statements.


```python
#example 1:
a = 33
b = 200

if b > a:
    pass 
```


```python
#example 2 :

for letter in 'Python': 
   if letter == 'h':
      pass
      print ("This is pass block")
   print("Current Letter :", letter)

print ("Good bye!")

```

    Current Letter : P
    Current Letter : y
    Current Letter : t
    This is pass block
    Current Letter : h
    Current Letter : o
    Current Letter : n
    Good bye!
    


```python

```


```python

```


```python
# calculate factorial no by using for loop
# factorial of 5! = 5*4*3*2*1
num=int(input("enter a number"))
if(num==0):
   fact=1
fact =1 
for i in range(1,num+1):  
    fact = fact*i
print("factorial is",fact) 
#1st iteration= 1*1=1
#2nd iteration =1*2=2
#3nd iteration =2*3=6
#4nd iteration =6*4=24
#5nd iteration =24*5=120
#6nd iteration =120*6=720
```

    enter a number6
    factorial is 720
    


```python
#prog to find 'sum of cubes'of numbers from 1 to 50.
#   1+8+27+64+125+ ..........
n=int(input("enter a number"))
s=0
for i in range(1,n+1):
    a=i**3   #to find power of the no
    s=s+a
print("sum of cubes : ",s)
#1st iteration= a=1
 #              s=0+1=1
#2st iteration   a=8
 #               s= 1+8=9
#3 t iteration   a=27
     #          s= 9+27 =36
```

    enter a number3
    sum of cubes :  36
    


```python
# write a prog to generate calender of a month given the start-day and no of days in that month.
```


```python

```

# Nested  For Loop:

A nested for loop is a for loop inside a for loop.
The "inner for loop" will be executed one time for each iteration of the "outer for loop":


```python
#Example
# prog to Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "strwaberry", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
```

    red apple
    red strwaberry
    red cherry
    big apple
    big strwaberry
    big cherry
    tasty apple
    tasty strwaberry
    tasty cherry
    

# print pattern in Python

In Python, for loop is used to print the various patterns. Printing the various patterns are most common asked programming questions in the interview. The multiple for loops are used to print the patterns where the first outer loop is used to print the number of rows, and the inner loop is used to print the number of columns. Most of the patterns use the following concepts.

The outer loop to print the number of rows.
The inner loops to print the number of columns.
The variable to print whitespace according to the required place in Python.

 #example of print simple pyramid pattern  
* 
* * 
* * * 
* * * * 
* * * * *


```python
# prog to print simple pyramid pattern

for i in range(1,11):
    print()            # print new line
    for j in range(i):
        print("*",end="  ")
```

    
    *  
    *  *  
    *  *  *  
    *  *  *  *  
    *  *  *  *  *  
    *  *  *  *  *  *  
    *  *  *  *  *  *  *  
    *  *  *  *  *  *  *  *  
    *  *  *  *  *  *  *  *  *  
    *  *  *  *  *  *  *  *  *  *  


```python
# prog to print numbers in pyramid pattern
for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(j,end=" ")
```

    
    1 
    1 2 
    1 2 3 
    1 2 3 4 
    1 2 3 4 5 


```python
# example:
for i in range(1,6)
  # print(i,"-",end=' ')
    for j in range(1,6):
        print(j,end=" ")
    print()
```

    1 2 3 4 5 
    1 2 3 4 5 
    1 2 3 4 5 
    1 2 3 4 5 
    1 2 3 4 5 
    


```python
#example
count = 0
for i in range(1,5):
    print()
    for j in range(1,i+1):
        print(count,end=" ")
        count = count+1
```

    
    0 
    1 2 
    3 4 5 
    6 7 8 9 


```python
# example:
N=5
for i in range (1,N+1):
    for k in range(N,i,-1):
        print(" ",end = ' ')
    for j in range(1,i+1):
           print(j,end=" ")
    print()
```

            1 
          1 2 
        1 2 3 
      1 2 3 4 
    1 2 3 4 5 
    


```python
# example:
n=5
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end =' ')
    for j in range(1,i+1):
        print(j,end=" ")
    for l in range(i-1,0,-1):
        print(l,end=" ")
    print()
    
```

            1 
          1 2 1 
        1 2 3 2 1 
      1 2 3 4 3 2 1 
    1 2 3 4 5 4 3 2 1 
    

# Python for/while loop with else

In most of the programming languages (C/C++, Java, etc), the use of else statements has been restricted with the if conditional statements. But Python also allows us to use the else condition with for loops. 

Note: The else block just after for/while is executed only when the loop is NOT terminated by a break statement 


```python

```


```python
for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break\n")
```

    1
    2
    3
    No Break
    
    


```python
for i in range(1, 4):
    print(i)
    break
else:  # Not executed as there is a break
    print("No Break")
```

    1
    


```python
# else with while Loop :
i=0
while i<5:
    print (i)
    i=i+1
else :
    print ("while loop completely 	exhausted, since there is no break.")
print ("Out of loop")

```

    0
    1
    2
    3
    4
    while loop completely 	exhausted, since there is no break.
    Out of loop
    


```python

```


```python

```
