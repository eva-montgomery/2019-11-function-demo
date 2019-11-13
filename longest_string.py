# 3. Find the shortest String
# Write a function shortest that accepts a List of Strings as an argument.

# It should return the shortest String in the List.



def longest(lst):
    the_longest = lst[0]
    for word in lst:
        if len(word) > len(the_longest):
            the_longest = word
    return the_longest    
              
print(longest(["horse", "pig", "dog","flamingo"]))




