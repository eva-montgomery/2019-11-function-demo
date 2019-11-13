# only_odds function
# Write a function that accepts a List of numbers as an argument.

# Return a new List that includes the only the odd numbers.
# Hint: use your is_odd() function to determine which numbers 
# to include in your new List.

def is_even(arr):
    if arr % 2 == 0:
        return True
    else:
        return False  

def is_odd(arr):
    return not(is_even(arr))

def only_odds(arr):
    x = []
    for number in arr:
        if is_odd(number):
            x.append(number)
    return x       
        
print(only_odds([11, 20, 42, 97, 23, 10]))

 
# correct function but does not refer to previous function:
# def only_odds(n):
#     x = []
#     for number in n:
#         if number % 2 != 0:
#             x.append(number)
#     return x        
        
# print(only_odds([11, 20, 42, 97, 23, 10]))
