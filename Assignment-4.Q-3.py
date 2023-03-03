#Write a Python program to square the elements of a list using map() function.

def square(x):
        return x*x
numbers = [4,5,2,9]
s = list(map(square, numbers))
print(s)