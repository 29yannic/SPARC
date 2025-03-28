# Assignment
my_list = [0, 1, 2, 3] # [] for mutable lists
my_tuple = (0, 2, 4, 8) # () for immutable tuples
my_dict = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4} # {'key': value} for dictionaries

my_list[3] = 4 # replace value
print(my_list) # > [0, 1, 2, 4]

# Use of operators
print(my_tuple + (16, 32, 64)) # > (0, 2, 4, 8, 16, 32, 64)

print(16 in my_tuple) # > False
print(4 in my_list) # > True
print(4 in my_dict) # > False
print('fourth' in my_dict) # > True

# Use of built-in functions
print(len(my_dict)) # > 4

my_list.append(16) # add value to the end
my_list.pop(0) # remove first item
my_list.insert(3, 8) # add value 8 at 4th position (remember, sequences start with 0)
print(my_list) # > [1, 2, 4, 8, 16]

# Oops
my_tuple[5] = 16 # Program crashes :( -> TypeError