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

# In[15]:


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




