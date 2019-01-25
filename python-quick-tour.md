# **PYTHON QUICK TOUR** 
My writing will be a summary of the basic rules and syntax in python. This summary for people who have basic programming knowledge but don't have any time and want to quickly meet with python. A programming language can never be learned in a very short time. But however you can get an idea about it and also start writing small programs. That's the point. Python is an object-oriented programming language. It's much simpler than other OOP languages. (Another one of simple OOP languages is Ruby.) And Python has many library for different issues.

### **Forget Semicolons, Parantheses, Curly Brackets**
If you have had experience working with java, c, c #, and similar languages, you know that semicolons and brackets are very important and sometimes critical for the program. In Python, there is no semicolon requirement for lines of code to work. Code it with the correct syntax and say hello.
```python
print("Hello Python!")
```
### Focus to Indentations!

When we are coding with Java, C, C#  we use parantheses for create condition lines. In python, we don't need it. 
And in this languages (Java, C...) we use curly brackets when we are creating a loop, if/else statement, functions... But in python, **we will use line indents instead of curly brackets.** Line indents will be our program's hero.  _Let's explain all this with examples after this quick summary._

##### *There is no parantheses in condition statements:*
*Let's write a condition line:*
```python
if 3 > 2:
    print("3 is bigger than 2")
else:
    print("2 is bigger than 3")
#elif:
#Elif is else-if in other languages. This used for create other if conditions. 
```
*Let's see the difference from C*
```c
if (3 > 2){
    printf("3 is bigger than 2");
}
else{
    printf("2 is bigger than 2");
}
```
| Python       | C          |
| ------------- |:-------------:|
| We didn't use parantheses for condition        | look at the (3 > 2) |
|We used only ":"" and didn't use curly brackets | We have seperated all statement block with curly brackets|
|After defining the condition, we have defined the code which will run using with the line indent.|We have specified the code parts to be executed in curly brackets which belong to the condition.
---
> **Note That!**
>In other programming languages when we create a variable, we need to specify the type of this variable. And the initial value assignment must be from this type. But in python, we don't need to specify the type of variable. **Just write your variable name and put equal symbol and then write your value of any type. Even if your variable has a integer value, you can make it string. Just assign new value to variable.**
```python
x = 5 #x is an integer
x = "now x is a string"
x = 5.1 #x is float
```
---
## Python Variables
   I have touched on briefly some tips about variables in the previous part of this article. 
* In python, declaring a variable type is not necessary.
* The type of variable will be what did you assign to it. E.g. If you assign a integer, its type will be integer; if you assign a string its type will be string.
* In python, variables are case-sensitive.
   ``` python
    variable = "this is a text" #print(type(variable)) output: <class 'str'>
    variable = 3 #print(type(variable)) output: <class 'int'>
   ```
---
## Python Strings, Numbers 
* In python, there is no short, double and others. There is only integer, float and complex.
If the number is decimal its type is float; if the number is integer its type is int; if the number is complex (like 5j, 3i) its type is complex.  
    ``` python
   x = 3 #This is an int
   z = 5i #This is a complex number
   y = 3.2 #This is a float 
    ```
* In python, strings are like arrays. The elements of the string can be accessed through indexes. Also you can
    write a specified parts of string.
     ``` python
   text = "Let's see"
   print(text[1]) #Output:e
   print(text[0]) #Output:L
   print(text[2:8]) #Output:t's se
    ```
    Lets suppose we have a string which has name "mystring"
    - **For length of string: len(mystring)**
    - **For make all letters uppercase: mystring.upper()**
    - **For make all letters uppercase: mystring.lower()**

> **GETTING DATA FROM KEYBOARD: input()**
 ``` python
   data = input("Enter string from keyboard:\t")
  ```
 > We can use this data in our programs like other variables. 
---
## Python Conditions
This part is the quick look for conditional statements in python.
**Condition Operators:**

| Operator       | Mean         |
| -------------- |:-------------:|
|  ==    | Equal |
| !=     | Not equal|
| <= |Less than or equal  |
| >= | Greater than or equal |
| > | Greater than |

We said in python, there is no parenthesis in condition unlike other languages.  When we creating a condition statement
there is important thing is the line indents because line indents defines the code parts of conditional statements.
We saw "if statement" before. Let's see the nested if-else statements thus we can understand the importance of line indents.
```python
if username == True #If username is true then we will control password's correctness
    if password== True #Also if password is correct user can be sign in.
        login = True
    elif
        print("Wrong password!")
elif
print("Wrong user name")
```
> This code block is just an example. In real life, a login controller absolutely must be coded according to security rules.

We can write this conditional code part like that:
```python
if username and password == True
    login = True
elif 
print("Wrong username or password!")
```
---
## Python Loops
Remember this **Focus to Indentations!**
We said indentatations are very important in Python. When we are creating loops we use indentations and ":" in Python.
Let's see more clear with this example:
#### While Loops:
When we are creating the while loops, we should be careful about the indentations and we need put the ":" after the declaration of loop.
*In Python:*
```python
number = 0
while number < 5:
    print(number)
    number += 1
```
*In C:*
```c
int number;
number = 0;
while( number < 5 ){
    print(number);
    number += 1;
}
```
*In Java*:
```java
int number = 0;
while( number < 5 ){
    System.out.println(number);
    number++;
}
```
***Be careful about the indentations! Let's look the its importance in loops***
Let's think you wrote some loop lines in Python. If your code like that yes it will be run! Congratulations. 
```python
i = 0 
while i < 5:
    if i % 2 == 0:
        print('{} is even number'.format(i))
    i += 1
```
But...
If your code is like that it will give an error probably. Even, absolutely you'll get an error.
```python
i = 0 
while i < 5:
    if i % 2 == 0:
        print('{} is even number'.format(i))
        i += 1
```
You can try the both of them. Thus you can see the importance of indentations.

#### For Loops:
In the For Loops we can see more differences than While loops between the other programming languages.
##### *Let's look to the **range***
**range** defines in order of:
+ from which number? (it's like initial value of counter)
+ to which number?
+ increase amount

Let's look at the code:
```python
for i in range(0,10,1):
    print(i)
```
>*Output is:*
0
1
2
3
4
5
6
7
8
9

*In C:*
```c
int i;
for(i = 0;i < 10;i++){
    printf("%d\n",i);
}
```
This will give the same output. And **note that! In C, printf() method doesn't put new line character (\n)**  
##### *Let's go back to Python*
You don't have to give 3 argument to **range.** Range function has 0 for the initial value so if you put the e.g. range(5) this means from 0 to 5. So instead of the first "for loop example" you can use that:
```python
for i in range(10):
    print(i)
```
If you want start from 0 and increase one by one to x number, you should use range(x) instead of range(0,x,1). But if your increase amount different from 1 or you don't want start from 0 your function should be range(a,b,c).
If you want to write all lines in your file how can you do that with using for loop? Actually that is so simple with Python. There is no detail for file operations. It's just a for loop example. Code is so clear.
```python
for line in datafile:
    datas = datafile.readlines()
```
So you can access every element in your data set using for Loop. 

---
## Python Functions

Like old parts we should say this again *there is no curly brackets for functions*
In Python, if you want create function your syntax should be like that **def yourFunctionName():**
Let's create a simple function for print Hello World
```python
def sayHello():
    print('Hello')
```
In other languages you have to give type of your function, your return value and something like this. But in Python there is no declaration for this just put **def** and do something with your function. For example if you are coding with Java your function declaration would be like this:
```java
public static void yourFunctionName(parameterType parameterName){
DO SOMETHING
}
```
or if you are coding with C this would be like this:
```C
yourReturnType yourFunctionName(parameterType parameterName){
DO SOMETHING 
}
```
and if you don't want return anything your return type would be void. But in Python, you don't need assign any type for your parameter or your function's return type. Let's assume you send some argument to your function and you want to print that and then you will return this argument's double value. There is code for this scenario.
```python
def multiplyByTwo(number):
    print(number)
    return number*2
```
This is so simple like that.

---
###### This writing is summary for Python so we don't see details. You can see the syntax rules and simplicity of Python. And you can write your basic, small programs but for more you need practice, research and details.
***By Burcu Söylemez***
