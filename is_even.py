# is_even function
# Write a function that accepts a number as an argument and 
# returns a Boolean value. Return True if the number is even; 
# return False if it is not even.

def is_even(number):
    # decide if the number is even
    if (number % 2) == 0:
        return True
        # return True if it's even
    else:
        return False    
        # return False if it's not even 
print(is_even(5))
print(is_even(6))




