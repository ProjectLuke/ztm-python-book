
# *Fundamental Data Types
# int: 1 2 3
# float: 1.0 2.01 3.99
# bool 
# str 
# list 
# tuple 
# set 
# dict 


# *Variables
# snake_case
# Start with lowercase or underscore
# Letters, numbers, underscores
# Case sensitive
# Don't overwrite keywords
# !Putting an underscore in front usually
#   !indicates a private variable

user_IQ = 190
print(user_IQ)


# *Operator Precedence
# !From high to low
# Parantheses ()
# Exponents **
# Multiplication or Division * /
# Addition or Subtraction + -

# * bin() and complex
# complex - only use this for very complex math,
# may not use it ever
# bin() - displays the binary representation
# of whatever you use

# *Expressions vs Statements
# Expression: piece of code that produces
# a value [only the iq / 5]
# Statement: an entire line of code [line 45]

iq = 100
user_age = iq / 5


#* Augmented Assignment Operator
some_value = 5
some_value = some_value + 2
# !Instead of this, use an augmented assignment operator
new_value = 5
new_value += 2


#* String
# Simply a piece of text
'hi hello there'
"Hi hello there!"
# This is how you would use double vs single 
" emphasizing 'sarcasm' here"
#Third way of strings
long_string = '''
Long
STRINGS
'''
print(long_string)


#* String Concatenation
print('hello' + ' Andrei')
#Cannot concatenate a string + int together

#* Type Conversion
print(type(str(100)))

#The below is a representation of literally the same thing
a = str(100)
b = int(a)
c = type(b)
print(type(str(100)))



#* Escape Sequence
weather = "It\'s \kind of\" sunny" 
#The slash is known as the 'escape' in quotes to allow
# certain character to be added as a character
#There is also \n \t
weather = "\n It\'s \"kind of\" sunny, good day! "


#* Formatted Strings
name = 'Johnny'
age = 55

#The first formatted string is the preferred and recomennded
# method
print(f'hi {name}. You are {age} years old') 
print('hi {}. You are {} years old'.format(name, age))


#* String Indexes
'one'
#012

first_word = 'fourth'
             #012345
#Basically each character of the string is assigned 
# a location in the memory, the number is the index of 
# each char in the string

print(first_word[0:4:1])
#[start_from_here:end_before_here:step_through]



#* Immutability
#Strings are immutable, meaning the value cannot be changed
# once created
#Would have to reassign the value



#* Built-in Functions & Methods
#Python has some built-in functions and stuff that
# we can use
#Our job is to understand the resource exists
#? .upper()
#? .format()
#? .lower()


#* Booleans
#simple, a bool can be true or false
is_cool = False
now_cool = True


#* Commenting Rules
#Write code that is easy to read and easy to understand like english
#Resource link
# https://realpython.com/python-comments-guide/
