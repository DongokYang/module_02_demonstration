"""
Description: Module 02 demonstration
Author: Dongok Yang
Date: 2023.09.13
Usage: To demonstrate content from Module 02.
"""
 
# This is a single-line comment.  
 
"""
 This is a multi-line comment.
 It can span multiple lines.
"""
 
# Calling a function
 
absolute_value = abs(-12)
print('absolute value:', absolute_value)
 
# Function embedded within another function.
print('absolute value:' , abs(-12))
 
# SYNTAX: print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print("I am", 25, "years old.")
 
print("apples", "oranges", "bananas", sep = ", ")
 
# Print using f-string
 
name = "John" 
age = 25 
print(f"My name is {name} and I am {age} years old.")
# output: My name is John and I am 25 years old.
 
value = 3.14159 
print(f"The value is {value:.2f}.")
# output: The value is 3.14.
 
number = 123 
print(f"The number is {number:05}.")
#output: The number is 00123.
 
name = "John" 
print(f"Hello, {name:>10}.") 
# output: Hello,      John.