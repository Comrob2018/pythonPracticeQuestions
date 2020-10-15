#Unless stated otherwise:
#	Input data being supplied to the question should be a console input.

#----------------------------------------#
#Question 1

	Write a program which will find all such numbers which are divisible by 7 
	but are not a multiple of 5, between 2000 and 3200 (both included).
	The numbers obtained should be printed in a comma-separated sequence on a
	single line.

	
#----------------------------------------#
#Question 2
		
	Write a program which can compute the factorial of a given numbers. The 
	results should be printed in a comma-separated sequence on a single line.
		
	#Example:
		Suppose the following input is supplied to the program:
			
			8

		Then, the output should be:
			
			40320

#----------------------------------------#
#Question 3
		
	With a given integer n, write a program to generate a dictionary that
	contains (i, i*i) such that is an integral number between 1 and n (both included).
	Then the program should print the dictionary.
		
	#Example
		Suppose the following input is supplied to the program:
		
			8
		
		Then, the output should be:
		
			{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

	
#----------------------------------------#
#Question 4
	
	Write a program which accepts a sequence of comma-separated numbers from console and generate
	a list and a tuple which contains every number.
		
	#Example:
		Suppose the following input is supplied to the program:
		
			34,67,55,33,12,98
			
		Then, the output should be:
		
			['34', '67', '55', '33', '12', '98']
			('34', '67', '55', '33', '12', '98')

#----------------------------------------#
#Question 5
		
	Define a class which has at least two methods.
	getString: to get a string from console input
	printString: to print the string in upper case.
	Also please include simple test function to test the class methods.

	#Hints:
		Use __init__ method to construct some parameters.

#----------------------------------------#
#Question 6
		
	Write a program that calculates and prints the value according to the given formula:
		Q = Square root of [(2 * C * D)/H]
		
	Following are the fixed values of C and H:
		
		C is 50. H is 30.
		D is the variable whose values should be input to your program
		in a comma-separated sequence.

	#Example:
		Let us assume the following comma separated input sequence is given to the program:
				
			100, 150, 180

		The output of the program should be:

			18, 22, 24

	#Hints:
		If the output received is in decimal form, it should be rounded off to its 
		nearest value (for example, if the output received is 26.0, it should be 
		printed as 26). 

	#Note:	
		Input data should be in a comma-separated form.


#----------------------------------------#
#Question 7
		
	Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
	The element value in the i-th row and j-th column of the array should be i*j.
	

	#Example:
		Suppose the following inputs are given to the program:
				
			3,5

		Then, the output of the program should be:

			[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

	#Note:
		Input data should be in a comma-separated form.

#----------------------------------------#
#Question 8
	
	Write a program that accepts a comma separated sequence of words as input and
	prints the words in a comma-separated sequence after sorting them alphabetically.

	#Example:
		Suppose the following input is supplied to the program:
			
			without,hello,bag,world
			
		Then the output should be:
			
			bag,hello,without,world

	#Note:
		Input data should be in a comma-separated form.

#----------------------------------------#
#Question 9
	
	Write a program that accepts sequence of lines as input and prints the lines after
	making all characters in the sentence capitalized.
		
	#Example:
		Suppose the following input is supplied to the program:

			Hello world
			Practice makes perfect

		Then, the output should be:
			
			HELLO WORLD
			PRACTICE MAKES PERFECT

#----------------------------------------#
#Question 10

	Write a program that accepts a sequence of whitespace separated words as input and prints
	the words after removing all duplicate words and sorting them alphanumerically.
		
	#Example:	
		Suppose the following input is supplied to the program:
				
			hello world and practice makes perfect and hello world again

		Then, the output should be:
				
			again and hello makes perfect practice world

	#Hints:
		Use set container to remove duplicated data automatically and then use sorted() to sort the data.

#----------------------------------------#
#Question 11
		
	Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
	and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are 
	to be printed in a comma separated sequence.

	#Example:
		Suppose the following input is supplied to the program:
		
			0100,0011,1010,1001

		Then the output should be:
			
			1010
	#Note:
		Input data should be in a comma-separated form.

#----------------------------------------#
#Question 12

	Write a program, which will find all such numbers between 1000 and 3000 (both included) such that
	each digit of the number is an even number. The numbers obtained should be printed in a 
	comma-separated sequence on a single line.

#----------------------------------------#
#Question 13
	
	Write a program that accepts a sentence and calculate the number of letters and digits.
	
	#Example:	
		Suppose the following input is supplied to the program:
			
			hello world! 123
			
		Then, the output should be:
		
			LETTERS 10
			DIGITS 3

#----------------------------------------#
#Question 14

	Write a program that accepts a sentence and calculate the number of upper case letters and
	lower case letters.
		
	#Example:
		Suppose the following input is supplied to the program:
			
			Hello world!
			
		Then, the output should be:
			
			UPPER CASE 1
			LOWER CASE 9

#----------------------------------------#
#Question 15

	Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

	#Example
		Suppose the following input is supplied to the program:
		
			9

		Then, the output should be:
			
			11106
		(9+99+999+9999)=11106

#----------------------------------------#
Question 16
	
	Use a list comprehension to square each odd number in a list. The list is input by a 
	sequence of comma-separated numbers.

	#Example	
		Suppose the following input is supplied to the program:

			1,2,3,4,5,6,7,8,9
		
		Then, the output should be:

			1,3,5,7,9

	
#----------------------------------------#
#Question 17

	Write a program that computes the net amount of a bank account based a transaction log from console input.
	D means deposit and W means withdrawal. The transaction log format is shown as following:

		D 100
		W 200

	#Example:		
		Suppose the following input is supplied to the program:

			D 300
			D 300
			W 200
			D 100

		Then, the output should be:
			
			500

#----------------------------------------#
#Question 18

	A website requires the users to input username and password to register. 
	Write a program to check the validity of password input by users.
	Following are the criteria for checking the password:
	
		1. At least 1 lowercase letter [a-z]
		2. At least 1 number [0-9]
		3. At least 1 Uppercase letter [A-Z]
		4. At least 1 character from [$#@]
		5. Minimum length of password: 6
		6. Maximum length of password: 12

	Your program should accept a sequence of comma separated passwords and will check them
	according to the above criteria. Passwords that match the criteria are to be printed, 
	each separated by a comma.

	#Example:
		If the following passwords are given as input to the program:
			
			ABd1234@1,a F1#,2w3E*,2We3345

		Then, the output of the program should be:

			ABd1234@1

	#Note:
		Input data should be in comma-separated form.

#----------------------------------------#
#Question 19

	You are required to write a program to sort the (name, age, height) tuples by ascending 
	order where name is string, age and height are numbers. The tuples are input by console.
	The sort criteria is:
		
		1: Sort based on name.
		2: Then sort based on age.
		3: Then sort by score.

	The priority is name > age > score.

	#Example:
		If the following tuples are given as input to the program:

			(Tom, 19, 80)
			John, 20, 90
			Joni, 17, 91
			Judy, 17, 93
			Jason, 21, 85
							
		Then, the output of the program should be:

			[('Judy', '17', '93'), ('Joni', '17', '91'), ('John', '20', '90'), 
			('Jason', '21', '85'), ('Tom', '19', '80')]

	#Note:					      
		Input data should be in comma-separated form.
					      
#----------------------------------------#
#Question 20
					      
	Define a class with a generator which can iterate the numbers, which are divisible 
	by 7, between a given range 0 and n.

	#Hints:
		Consider using yield

#----------------------------------------#
#Question 21
					      
	Write a program for a robot. The robot moves in a plane starting at the center (0,0). 
	The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of 
	robot movement is shown as the following:

		UP 5
		DOWN 3
		LEFT 3
		RIGHT 2

	The numbers after the direction are steps. Please write a program to compute the 
	distance from current position after a sequence of movement and original point. 
	If the distance is a float, then just print the nearest integer.
					      
	#Example:
		If the following tuples are given as input to the program:
							
			(UP, 5)
			DOWN 3
			LEFT 3
			RIGHT 2
							
		Then, the output of the program should be:
							
			2 

#----------------------------------------#
# Question 22
	
	Write a program to compute the frequency of the words from the input. 
	The output should output after sorting the key alphanumerically. 

	#Example:
		Suppose the following input is supplied to the program:
	
			New to Python or choosing between Python 2 and 
			Python 3? Read Python 2 or Python 3.

		Then, the output should be:

			2:2
			3.:1
			3?:1
			New:1
			Python:5
			Read:1
			and:1
			between:1
			choosing:1
			or:2
			to:1

#----------------------------------------#
#Question 23

    Write a method which can calculate square value of number

#----------------------------------------#
#Question 24

    write a program to print some Python built-in functions documents, such as abs(), int(), 
    input(). And add document for your own function.
    
    #Hints:
	The built-in document method is __doc__

#----------------------------------------#
#Question 25

    	Define a class, which have a class parameter and have the same instance parameter.

	#Hint:
		Define a instance parameter, need add it in __init__ method
		You can init a object with construct parameter or set the value later

#----------------------------------------#
#Question 26

	Define a function which can compute the sum of two numbers.

#----------------------------------------#
#Question 27

	Define a function that can convert a integer into a string and print it in console.

#----------------------------------------#
#Question 28

	Define a function that can receive two integer numbers in string form and compute 
	their sum and then print it in console.

#----------------------------------------#
#Question 29

	Define a function that can accept two strings as input and concatenate them and then 
	print it in console.

#----------------------------------------#
#Question 30
	
	Define a function that can accept two strings as input and print the string with maximum 
	length in console. If two strings have the same length, then the function should print 
	all strings line by line.

#----------------------------------------#
#Question 31
	
	Define a function that can accept an integer number as input and print the "It is an even number"
	if the number is even, otherwise print "It is an odd number".

#----------------------------------------#
#Question 32	
	
	Define a function which can print a dictionary where the keys are numbers between 1 and 3 
	(both included) and the values are square of keys.

	#Hints:
		Use dict[key]=value pattern to put entry into a dictionary.
		Use ** operator to get power of a number.

#----------------------------------------#
#Question 33
	
	Define a function which can print a dictionary where the keys are numbers between 1 and 20 
	(both included) and the values are square of keys.

	#Hints:
		Use dict[key]=value pattern to put entry into a dictionary.
		Use ** operator to get power of a number.
		Use range() for loops.

#----------------------------------------#
#Question 34
	
	Define a function which can generate a dictionary where the keys are numbers between 1 and 20 
	(both included) and the values are square of keys. The function should just print the values only.

	#Hints:
		Use dict[key]=value pattern to put entry into a dictionary.
		Use ** operator to get power of a number.
		Use range() for loops.
		Use keys() to iterate keys in the dictionary. Also use item() to get key/value pairs.

#----------------------------------------#
#Question 35

	Define a function which can generate a dictionary where the keys are numbers between 1 and 20 
	(both included) and the values are square of keys. The function should just print the keys only.

	#Hints:
		Use dict[key]=value pattern to put entry into a dictionary.
		Use ** operator to get power of a number.
		Use range() for loops.
		Use keys() to iterate keys in the dictionary. Also use item() to get key/value pairs.

#----------------------------------------#
#Question 36

	Define a function which can generate and print a list where the values are square of numbers between 
	1 and 20 (both included).

#----------------------------------------#
#Question 37
	
	Define a function which can generate a list where the values are square of numbers between 1 and 20 
	(both included). Then the function needs to print the first 5 elements in the list.

	#Hints:
		Use ** operator to get power of a number.
		Use range() for loops.
		Use list.append() to add values into a list.
		Use [n1:n2] to slice a list

#----------------------------------------#
#Question 38

	Define a function which can generate a list where the values are square of numbers between 1 and 20 
	(both included). Then the function needs to print the last 5 elements in the list.

	#Hints:
		Use ** operator to get power of a number.
		Use range() for loops.
		Use list.append() to add values into a list.
		Use [n1:n2] to slice a list

#----------------------------------------#
#Question 39

	Define a function which can generate and print a tuple where the value are square of numbers between 
	1 and 20 (both included). 

	#Hints:
		Use ** operator to get power of a number.
		Use range() for loops.
		Use list.append() to add values into a list.
		Use tuple() to get a tuple from a list.

#----------------------------------------#
#Question 40

	With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and
	the last half values in one line. 

	#Hints:
		Use [n1:n2] notation to get a slice from a tuple.

#----------------------------------------#
#Question 41

	Write a program to generate and print another tuple whose values are even numbers in the given tuple 
	(1,2,3,4,5,6,7,8,9,10). 

	#Hints:
		Use "for" to iterate the tuple
		Use tuple() to generate a tuple from a list.

#----------------------------------------#
#Question 42

	Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes",
	otherwise print "No". 

	#Hints:
		Use if statement to judge condition.

#----------------------------------------#
#Question 43

	Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

	#Hints:
		Use filter() to filter some elements in a list.
		Use lambda to define anonymous functions.

#----------------------------------------#
#Question 44

	Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

	#Hints:
		Use map() to generate a list.
		Use lambda to define anonymous functions.

#----------------------------------------#
#Question 45

	Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

	#Hints:
		Use map() to generate a list.
		Use filter() to filter elements of a list.
		Use lambda to define anonymous functions.

#----------------------------------------#
#Question 46

	Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

	#Hints:
		Use filter() to filter elements of a list.
		Use lambda to define anonymous functions.

#----------------------------------------#
#Question 47

	Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

	#Hints:
		Use filter() to filter elements of a list.
		Use lambda to define anonymous functions.

#----------------------------------------#
#Question 48

	Define a class named American which has a static method called printNationality.

	#Hints:
		Use @staticmethod decorator to define class static method.

#----------------------------------------#
#Question 49

	Define a class named American and its subclass NewYorker. 

	#Hints:
		Use class Subclass(ParentClass) to define a subclass.

#----------------------------------------#
#Question 50

	Define a class named Circle which can be constructed by a radius. 
	The Circle class has a method which can compute the area. 

	#Hints:
		Use def methodName(self) to define a method.

#----------------------------------------#
#Question 51

	Define a class named Rectangle which can be constructed by a length and width. 
	The Rectangle class has a method which can compute the area. 

	#Hints:
		Use def methodName(self) to define a method.

#----------------------------------------#
#Question 52

	Define a class named Shape and its subclass Square. The Square class has an init 
	function which takes a length as argument. Both classes have a area function which
	can print the area of the shape where Shape's area is 0 by default.

	#Hints:
		To override a method in super class, we can define a method with the same name 
		in the super class.

#----------------------------------------#
#Question 53

	Please raise a RuntimeError exception.

	#Hints:
		Use raise() to raise an exception.

#----------------------------------------#
#Question 54

	Write a function to compute 5/0 and use try/except to catch the exceptions.

	#Hints:
		Use try/except to catch exceptions.

#----------------------------------------#
#Question 55

	Define a custom exception class which takes a string message as attribute.

	#Hints:
		To define a custom exception, we need to define a class inherited from Exception.

#----------------------------------------#
#Question 56

	Assuming that we have some email addresses in the "username@companyname.com" format, 
	please write program to print the user name of a given email address. Both user names 
	and company names are composed of letters only.

	#Example:
		If the following email address is given as input to the program:

			john@google.com

		Then, the output of the program should be:

			john

	#Hints:
		Use '\w' to match letters.

#----------------------------------------#
#Question 57

	Assuming that we have some email addresses in the "username@companyname.com" format, 
	please write program to print the company name of a given email address. Both user names
	and company names are composed of letters only.

	#Example:
		If the following email address is given as input to the program:

			john@google.com

		Then, the output of the program should be:

			google

	#Hints:
		Use '\w' to match letters.

#----------------------------------------#
#Question 58

	Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

	#Example:
		If the following words is given as input to the program:

			2 cats and 3 dogs.

		Then, the output of the program should be:

			['2', '3']

	#Hints:
		Use re.findall() to find all substring using regex.

#----------------------------------------#
#Question 59

        Print a unicode string "hello world".

        #Hints:
                Use u'strings' format to define unicode string.

#----------------------------------------#
#Question 60

        Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

        #Hints:
                Use unicode() function to convert.

#----------------------------------------#
#Question 61

        Write a special comment to indicate a Python source code file is in unicode.

#----------------------------------------#
#Question 62

        Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

        #Example:
                If the following n is given as input to the program:

                        5

                Then, the output of the program should be:

                        3.55

        #Hints:
                Use float() to convert an integer to a float
					      
#----------------------------------------#
#Question 63

        Write a program to compute:

                f(n)=f(n-1)+100 when n>0 and f(0)=1 with a given n input by console (n>0).

        #Example:
                If the following n is given as input to the program:

                        5

                Then, the output of the program should be:

                        500

        #Hints:
                We can define a recursive function in Python.

#----------------------------------------#
#Question 64

        The Fibonacci Sequence is computed based on the following formula:

                f(n)=0 if n=0
                f(n)=1 if n=1
                f(n)=f(n-1)+f(n-2) if n>1

        Please write a program to compute the value of f(n) with a given n input by console.

        #Example:
                If the following n is given as input to the program:

                        7

                Then, the output of the program should be:

                        13

        #Hints:
                We can define a recursive function in Python.

#----------------------------------------#
#Question 65

        The Fibonacci Sequence is computed based on the following formula:

                f(n)=0 if n=0
                f(n)=1 if n=1
                f(n)=f(n-1)+f(n-2) if n>1

        Please write a program using list comprehension to print the Fibonacci Sequence 
        in comma separated form with a given n input by console.

        #Example:
                If the following n is given as input to the program:

                        7

                Then, the output of the program should be:

                        0,1,1,2,3,5,8,13

        #Hints:
                We can define a recursive function in Python.
                Use list comprehension to generate a list from an existing list.
                Use string.join() to join a list of strings.

#----------------------------------------#
#Question 66

        Please write a program using generator to print the even numbers between 
        0 and n in comma separated form while n is input by console.

        #Example:
                If the following n is given as input to the program:

                        10

                Then, the output of the program should be:

                        0,2,4,6,8,10

        #Hints:
                Use yield to produce the next value in generator.

#----------------------------------------#
#Question 67

        Please write a program using generator to print the numbers which can be divisible by 5 and 7 
        between 0 and n in comma separated form while n is input by console.

        #Example:
                If the following n is given as input to the program:

                        100

                Then, the output of the program should be:

                        0,35,70

        #Hints:
                Use yield to produce the next value in generator.

#----------------------------------------#
#Question 68

        Please write assertion statements to verify that every number in the list [2,4,6,8] is even.

        #Hints:
                Use "assert expression" to make assertion.

#----------------------------------------#
#Question 69

        Please write a program which accepts basic mathematic expression from 
	console and print the evaluation result.

        #Example:
                If the following string is given as input to the program:

                        35+3
 
                Then, the output of the program should be:

                        38

        #Hints:
                Use eval() to evaluate an expression.

#----------------------------------------#
#Question 70

	Please write a binary search function which searches an item in a sorted list. 
	The function should return the index of element to be searched in the list.

	#Hints:
		Use if/elif to deal with conditions.

#----------------------------------------#
#Question 71

	Generate a random float with a value between 10 and 100 using Python math module.

	#Hints:
		Use random.random() to generate a random float in [0,1].


#----------------------------------------#
#Question 72

	Generate a random float with a value between 5 and 95 using Python math module.

	#Hints:
		Use random.random() to generate a random float in [0,1].

#----------------------------------------#
#Question 73

	Please write a program to output a random even number between 0 and 10 inclusive using 
	random module and list comprehension.

	#Hints:
		Use random.choice() to a random element from a list.

#----------------------------------------#
#Question 74

	Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10
	inclusive using random module and list comprehension.

	#Hints:
		Use random.choice() to a random element from a list.

#----------------------------------------#
#Question 75

	Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

	#Hints:
		Use random.sample() to generate a list of random values.

#----------------------------------------#
#Question 76

	Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

	#Hints:
		Use random.sample() to generate a list of random values.

#----------------------------------------#
#Question 77

	Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7, 
	between 1 and 1000 inclusive.

	#Hints:
		Use random.sample() to generate a list of random values.

#----------------------------------------#
#Question 78

	Please write a program to randomly print a integer number between 7 and 15 inclusive.

	#Hints:
		Use random.randrange() to a random integer in a given range.

#----------------------------------------#
#Question 79

	Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

	#Hints:
		Use zlib.compress() and zlib.decompress() to compress and decompress a string.

#----------------------------------------#
#Question 80

	Please write a program to print the running time of execution of "1+1" for 100 times.

	#Hints:
		Use timeit() function to measure the running time.

#----------------------------------------#
#Question 81

	Please write a program to shuffle and print the list [3,6,7,8].

	#Hints:
		Use shuffle() function to shuffle a list.

#----------------------------------------#
#Question 82

	Please write a program to generate all sentences where subject is in ["I", "You"] 
	and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

	#Hints:
		Use list[index] notation to get a element from a list.

#----------------------------------------#
#Question 83
					      
	Please write a program to print the list after removing even numbers in 
	[5,6,77,45,22,12,24].

	#Hints:
		Use list comprehension to delete a bunch of element from a list.

#----------------------------------------#
#Question 84

	By using list comprehension, please write a program to print the list after
	removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

	#Hints:
		Use list comprehension to delete a bunch of element from a list.

#----------------------------------------#
#Question 85

	By using list comprehension, please write a program to print the list after 
	removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

	#Hints:
		Use list comprehension to delete a bunch of element from a list.
		Use enumerate() to get (index, value) tuple.

#----------------------------------------#

#Question 86

	By using list comprehension, please write a program generate a 3*5*8 3D array 
	whose each element is 0.

	#Hints:
		Use list comprehension to make an array.

#----------------------------------------#
#Question 87

	By using list comprehension, please write a program to print the list after 
	removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

	#Hints:
		Use list comprehension to delete a bunch of element from a list.
		Use enumerate() to get (index, value) tuple.

#----------------------------------------#
#Question 88

	By using list comprehension, please write a program to print the list after 
	removing the value 24 in [12,24,35,24,88,120,155].

	#Hints:
		Use list's remove method to delete a value.

#----------------------------------------#
#Question 89

	With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program 
	to make a list whose elements are in both of the above given lists.

	#Hints:
		Use set() and "&=" to do set intersection operation.

#----------------------------------------#
#Question 90
					      
	With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list
	after removing all duplicate values with original order reserved.

	#Hints:
		Use set() to store a number of values without duplicate.

#----------------------------------------#
#Question 91

	Define a class Person and its two child classes: Male and Female. All classes have 
	a method "getGender" which can print "Male" for Male class and "Female" for Female class.

	#Hints:
		Use Subclass(Parentclass) to define a child class.

#----------------------------------------#
#Question 92

	Please write a program which count and print the numbers of each character in a string 
	input by console.

	#Example:
		If the following string is given as input to the program:

			abcdefgabc

		Then, the output of the program should be:

			a,2
			c,2
			b,2
			e,1
			d,1
			g,1
			f,1

	#Hints:
		Use dict to store key/value pairs.
		Use dict.get() method to lookup a key with default value.

#----------------------------------------#
Question 93

	Please write a program which accepts a string from console and print it in reverse order.

	#Example:
		If the following string is given as input to the program:

			rise to vote sir

		Then, the output of the program should be:

			ris etov ot esir

	#Hints:
		Use list[::-1] to iterate a list in a reverse order.

#----------------------------------------#
#Question 94

	Please write a program which accepts a string from console and print the 
	characters that have even indexes.

	#Example:
		If the following string is given as input to the program:

			H1e2l3l4o5w6o7r8l9d

		Then, the output of the program should be:

			Helloworld

	#Hints:
		Use list[::2] to iterate a list by step 2.

#----------------------------------------#
#Question 95

	Please write a program which prints all permutations of [1,2,3]

	#Hints:
		Use itertools.permutations() to get permutations of list.

#----------------------------------------#
#Question 96

	Write a program to solve a classic ancient Chinese puzzle: 
	We count 35 heads and 94 legs among the chickens and rabbits in a farm. 
	How many rabbits and how many chickens do we have?

	#Hint:
		Use for loop to iterate all possible solutions.

#----------------------------------------#
