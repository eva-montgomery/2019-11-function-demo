# is_odd function
# Write an is_odd function that uses your is_even 
# function to determine if a number is odd. 
# (That is, do not do the calculation - call a function 
# that does the calculation.)
# Hint: You'll use the not keyword.

# Accept a number as argument
def is_even(number):
    # decide if the number is even
    if (number % 2) == 0:
    # return True if it's even
        return True
    else:
     # return True if it's even   
        return False  
# short way to run above:
# return (number % 2) == 0    
    

def is_odd(number):
    return not is_even(number)
# is an expression

# other option for def is_odd
# if is_even(number):
#     return True
# else:
#     return False  

print(is_odd(23))
print(is_odd(24))
