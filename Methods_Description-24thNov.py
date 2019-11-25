#!/usr/bin/env python
# coding: utf-8

# # Use of Capitalize()
# name1 = "MUHAmmad Qasim"
# name1.capitalize()
# print(name1)
# 
# 
# 

# # USE OF CASEFOLD()
# firstString = "qasimA"
# secondString = "QASIM" 
# 
# if firstString.casefold() == secondString.casefold():
#     print('The strings are equal.')
# else:
#     print('The strings are not equal.')

# # Center ()
# :returns the string padded with specified fillchar.
# string = "Pakistan is our Country"
# 
# new_string = string.center(30)
# 
# print(new_string)
# 
# 
# 

# # Count() method counts how many times an element has occurred in a list and returns it.¶
# vowels = ['a', 'e', 'i', 'o', 'i', 'u']
# 
# count = vowels.count('i')
# 
# print('The count of i is:', count)

# Method isdigit(). It gives us whether there is any digit in the string or not.
s = "28212"
print(s.isdigit())

# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdigit())


# The string encode() returns the encoded version of the string.
string = 'Pakistan'

print('The string is:', string)

# default encoding to utf-8
string_utf = string.encode()

print('The encoded version is:', string_utf)


# In[16]:


statement = "Islama is our relegion."

result = statement.endswith('relegion.')
# returns False
print(result)


# In[ ]:

# The find() method returns the lowest index of the substring if it is found in given string
statement = "Islam is our relegion."

result = statement. find('relegion.')
# returns False
print(result)

# keyword arguments
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346))



