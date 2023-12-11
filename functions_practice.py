# Functions practice
# author: me
# 24 nov 2023

def area_of_a_square(sidelength: float) -> float:
    """Return the area of a square.
    Results are in units squared.

    Params:

    sidelength - length of one side of the square
    """

    area = sidelength**2

    return area


def print_area_of_a_square(sidelength: float) -> None:
    """Calculate and print the area of a square.
    Results are in units squared.

    Params:

    sidelength - length of one side of the square
    """

    area = sidelength**2

    print(
        f"The area of a square with side length {sidelength} is: {area} square units."
    )


print(print_area_of_a_square(12.2))
print(area_of_a_square(12.2))

# Given two squares of two sidelengths
#    12.2 and 144
# Add the area of both squares

# area_of_squares = area_of_a_square(12.2) + area_of_a_square(144)
# print(area_of_squares)

# Quesiton 1
# Create function called stars()
# Takes int as perameter
# Returns string of stars of given
def stars(star_amount):
    return "*" * star_amount

print(stars(5))

# Question 2

def biggest_of_three(a: int, b: int, c: int) -> int:
    if a > b and a > c:
        return a
    
    elif b > a and b > c:
        return b
    
    else:
        return c
    
a = input("give a ")
b = input("give b ")
c = input("give c ")

print(biggest_of_three(a, b, c))

# question 3
def pyramid(pyramid_amount: int) -> int:
    for i in range(1, pyramid_amount+1):
        print("*" * i)

print(pyramid(5))


# question 4
def pyramid(pyramid_amount: int) -> int:
    for i in range(1, pyramid_amount+1):
        print(" " * stars(pyramid))
print(pyramid(5))