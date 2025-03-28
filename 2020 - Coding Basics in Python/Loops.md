## Exiting a Loop early
One of the ways to exit a loop early is by using a "break" statement.  can save valuable time and resources by skipping any remaining iterations. Here's an example to help you understand how it works:
```
numbers = [5, 8, 3, 9, 2, 4, 7]
search_value = 3
for index in range(len(numbers)):
   print("Comparing", numbers[index], "with", search_value)
   if numbers[index] == search_value:
      print("Found searched value", search_value, "at index", index)
      break
```
In this example, we are iterating through the indexes of the "numbers" list to search for a specific value called "search_value". For better visibility we always log what we are currently comparing the search value with. When the "numbers" list value for the current index matches the search value, we print the index at which we found the searched value inside the list and then use the "break" statement to immediately exit the loop. Although there would be more values inside the "number" list, no further iterations are performed and we don’t get any more comparison log messages.