# Fill in the two functions and the two classes below (look for the TODO comments).
#
# Parts 1 and 2 must use RECURSION - a function that calls itself on a smaller version
# of the problem. Do NOT use a loop for those two.
#
# Do not rename anything, because the automated tests use these names.

def count_occurrences(target, values):
    if not values:
        return 0
    match = 1 if values[0] == target else 0
    return match + count_occurrences(target, values[1:])

def is_sorted(values):
    if len(values) <= 1:
        return True
    if values[0] > values[1]:
        return False
    return is_sorted(values[1:])

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"{self.width}x{self.height}"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

def main():
    pass

if __name__ == "__main__":
    main()