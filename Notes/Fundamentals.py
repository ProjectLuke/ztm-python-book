
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


#* Lists
#An ordered sequence of collection of objects that can contain
# any type
#li = [1,2,3,4,5]
#li2 = [1,2,'a', True]

#Keep in mind, each object in the list has a position based on the index
# numbers




#* List Slicing
#* [start:stop:step]
#start position: end position: the increment
#! Slicing makes lists mutable
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
amazon_cart[0] = 'laptop'
print(amazon_cart[0::2])


#? To make a copy of a list
new_cart = amazon_cart[:]
#new_cart = amazon_cart
#The above kinda does the same, but anytime amazon_cart is modified or adjusted, the
# new_cart will also follow because it's referring to the amazon_cart
#If want to make a copy, make sure to use the [:]



#* Matrix
#A way to describe multi-dimensional lists
matrix = [
    [1,2,3],
    [2,4,6],
    [3,6,9]
]
#Basically an array within an array
#These come up a lot in ML

#? Accessing a Matrix
matrix[0][1]
print(matrix[0][1])
#Output will print out the 2 in the first row
#Am able to more arrays and do
matrix[1][2][3][n]



#* List Methods
#Python has some methods used for Lists/Arrays
#? Adding 
basket = [1,2,3,4,5]
new_list = basket.append('100')
print(new_list)
#! The above modifies the list in place, not produce a result
#! The below is the right way to do it
#Run both to see
basket.insert(4, '100')
print(basket)

#? Different methods do different things
#? Google and test to find out
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

#* Common List Patterns
sort()
reverse()
join()



#* List unpacking
#Ex 1
a,b,c = [1,2,3]

print(a)
print(b)
print(c)

#Ex 2
d,e,f, *other, d = [1,2,3,4,5,6,7,8,9]
print(d)
print(e)
print(f)
print(other)
print(d)
#Check out what this happens


#* None
#It basically means nothing/null
#There are use cases for assigning a variable to None


#* Dictionary
#A dataype and a data structure in python
#An unordered key-value pair
#Dictionaries contain objects with a key:value
dictionary = {
    'a': 1,
    'b': 2,
    'x': 3
}

print(dictionary['b'])
#Output will grab where b is stored and grab the value

# Ex
dictionary = {
    'a': [1,2,3],
    'b': 'hello',
    'x': True
}
print(dictionary['a'][1])

#Ex
my_list = [
    {
    'a': [1,2,3],
    'b': 'hello',
    'x': True
    },
    {
    'a': [4,5,6],
    'b': 'hello',
    'x': True
    }
]
print(my_list[0]['a'][2])

#! When to use a List vs Dictionary
#List has order
# Simply an index and value
#Dictionary has no order
# Holds more information such as key
# Can hold more information than Lists

#? The other way of creating Dictionaries
# user2 = dict(name = 'JohnJohn')


#* Dictionary Keys
#The key must be something that is immutable
dictionary = {
    123: [1,2,3], #valid
    True: 'hello', #valid
    [100]: True #Not Valid
}
#Most of the time the key is ususally something
# descriptive and easily understood 
#Also the key has to be unique, one key cannot/should not
# represent two different values


# #* Dictionary Methods
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary



#* Tuples
#Tuples are like lists but they cannot be modified
#Because they cannot be changed, they are faster than regular lists
my_tuple = (1,2,3,4,5)
#Use Cases
# Don't need to change the list
# Also good practice to use the right data structures for clean code purposes
# Real examples: coordinates, pickup point

#? Can also use Tuples as a key in dictionaries
user = {
    (1,2): [1,2,3],
    'greet': 'hello',
    'age': 20
}


#* Tuple Methods
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found


#* Set
#Unordered collection of unique objects
my_set = {1,2,3,4,5}
print(my_set)

my_other_set = {1,2,3,4,5,5}
print(my_other_set)
#! If you print the above, you'll notice it still outputs only one 5
#Basically, sets do not allow duplicates


#* Set Methods
# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two or more sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with another set, or any other iterable




#* Conditional Logic
# if condition:
#     do something here
#     return
# elif condition:
#     do something here
#     return
# else:
#     do this

is_old = True
is_licensed = True

if is_old:
    print("You are old enough to drive!")
print("You need a license to drive")

if is_old and is_licensed:
    print("You can drive")

if is_old or is_licensed:
    print("You need both to drive")

#If the condition is false, then it will not print
# the 'You are old enough to drive' line

#* Indentation matters
#Grouping certain stuff like if and loops
# group them together by using indentation

#* Truthy vs Falsey
#Truthy value: When using a type convertor, print(bool(5)) the result
# somehow comes out 'True' 
#Basically there are some types here or results that lead to 'true' or 'false'
# which leads to the terminology of 'truthy vs falsy'

#* Ternary Operator
#? This is sort of a shothand version of doing ifelse
condition_if_true if condition else condition_if_false
#This does and can work but only in certain situations

#! Ex
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"


#* Short Circuiting
#Using ifelse in such a way that if something is true, the code
# can skip the rest of the unnessecary work and display only what 
# is needed to be displayed

#* Logical Operators
# and
# or
# not <- displays the opposite of the result
# >
# >=
# <
# <=
# ==
# !=  <- this is an actual operator
# The operator above says 'Only true if these two are mismatched'

#* Is vs ==
# == checks for the equality in value
# is checks if the location in memeory where the value is stored, is the same

#* For Loops
#? Naming convention, if you do not need the v
#Allows us to iterate a collection of items
#Iterables are objects are a collection that can be itereated multiple times
# Itereated -> one by one check each item in the collection
for iterate in iterable:
    return

for item in user.items():
    print(item)
    
for item in user.values():
    print(item)
#! More Ex
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for key, value in user.items():
    print(key, value)
    
for item in user.values():
    print(item)

#! The below is pulled from another set of notes
fruits = ["Apple", "Peach", "Pear"]
#fruit is the variable assigned to the items in the list 'fruits'
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)

#Loops and range
for number in range(1,10,2):
    print(number)
#This only prints 1 - 9, have to change the 10 to a 11 if want to print from 1 - 10
#The 2 shows how it will skip/step acorss different numbers

total = 0
for number in range(1, 101):
    total += number
print(total)

#While Loops
while something_is_true:
    print("something")
    #Do something repeatedly
    
#For Loops
for item in list_of_items:
    print("Do this")
    #Do something to each item

for number in range(a, b, c):
    print(number)
#c is a step over, so can have it go by evens, odds, backwards etc
    
#When to use for loop and while loop
#For loops are for when wanting to reiterate specific number of times
#   in a range or list

#While loops are for when you don't really care how many times
#   it takes to carry out a functionality, just as long as it
#   does it until the condition is met

#* Enumerate()
for i, char in enumerate('Hellooooo'):
    print(i, char)
#Take the iterable and gives the index counter and
#   the item of the index

#* While Loops
while condition:
    print("do this")
    i += 1
    break
else:
    print("Done doing the [do this]")
#While loops need a condition to activate and run
    #can use a break to stop
#! The else statement can only be ran if there is no 'break'

#?For simple iterable objects - use for loops
#?For unknown numbers and more heft work use while loops



#* break, continue, pass
#break - breaks out of the current enclosing loop
#continue - whatever happens, continue to the top of the current enclosed loop
#pass - not too useful, kinda just does nothing


