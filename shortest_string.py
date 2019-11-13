# Find the shortest String
# Write a function shortest that accepts a List of Strings as an argument.
# It should return the shortest String in the List.

# shortest "accepts" a list of strings
# or shortest "expects and receives" a list of strings

def shortest(lst):
    # assume the first is the shortest
    the_shortest = lst[0]
    # work through the list or check every item in the list
    for word in lst:
        # compare the lenghts
        if len(word) < len(the_shortest):
            # if we find one that is shorter, we "save" that in a new variable "the shortest"
            the_shortest = word  
    return the_shortest     
print(shortest(["horse", "pig", "dogs","flamingo", "a"]))

# or:
# some words = ["horse", "pig", "dogs","flamingo", "a"]
# the_word = shortest[some_words]
# print[the_word]

# list [ ] can be changed with .append() and .pop() and other methods
# tupeles () cannot be changed

####################
# "incorrect/other" way:
# def shortest(lst):
#     x = []
#     for word in lst:
#         x.append((len(word), word))
#     x.sort()
#     return x[0][1]  

# print(shortest(["horse", "pig", "dogs","flamingo"]))