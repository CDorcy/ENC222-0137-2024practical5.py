class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

def find_largest(f1, f2, f3):
    largest = f1
    if f2.numerator * largest.denominator > largest.numerator * f2.denominator:
        largest = f2
    if f3.numerator * largest.denominator > largest.numerator * f3.denominator:
        largest = f3
    
    return largest

if __name__ == "__main__":
    a = Fraction(1, 2)
    b = Fraction(3, 4)
    c = Fraction(2, 3)

    largest_fraction = find_largest(a, b, c)

    print(f"The largest fraction is: {largest_fraction}") 
