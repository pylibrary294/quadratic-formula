import math
from time import sleep

list_of_values = []

# Start of by collecting all values
def get_values(clean = False):
    if clean == True:
      list_of_values.clear()
    for values in input("A: >>> "),input("B: >>> "),input("C: >>> "):
        list_of_values.append(values)

# Coverts the list items to integers
def int_cov(list_to_be_converted):
    values = list(map(int, list_to_be_converted))

    return values

# Function to evaluate requests

def quad():
    #__init__    
    a,b,c = int_cov(list_of_values)

    b = -b

    b_square = b ** 2

    four_ac = 4*a*c
    
    # In case of complex numbers :)
    re_run = True
    while re_run == True:
      try:
        square_root = math.sqrt(b_square - four_ac)
        re_run = False
      except ValueError:
        print("That was a complex equation. Try again!")
        # Get new set of values
        get_values(clean=True)
        
        # Set new values to new_values
        new_values  = quad()
        
        return new_values

        
    # To be divided
    first_half = [b + square_root,b - square_root]
    
    # Processing answers into a list and
    # rounding all values to 3 deecimal places
    
    answers = [round(first_half[0]/2*a, ndigits = 3), round(first_half[1]/2*a, ndigits = 3)]
    return answers

# Main Program
def main(clean = False):
  get_values(clean = clean)
  x1, x2 = quad()
  print("The first value of x is equal to {} and the second value is equal to {}".format(x1,x2))
  sleep(5)

if __name__ == '__main__':
    main()
