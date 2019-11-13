# Only_evens function
# Write a function that accepts a List of numbers as an argument.

# Return a new List that includes the only the even numbers.
# Hint: use your is_even() function to determine which numbers to include in your new List.

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False  

def only_evens(arr):
    x = []
    for number in arr:
        if is_even(number):
            x.append(number)
    return x        
        
print(only_evens([11, 20, 42, 97, 23, 10])) 

# correct function but does not refer to previous function:
# def only_evens(n):
#     x = []
#     for number in n:
#         if number % 2 == 0:
#             x.append(number)
#     return x        
        
# print(only_evens([11, 20, 42, 97, 23, 10])) 



