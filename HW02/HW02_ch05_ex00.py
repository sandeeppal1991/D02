#!/usr/bin/env python
# HW02_ch05_ex00 (See 5.9)

# Write a function called do_n that takes a function object and a number, n, as
# arguments, and that calls the given function n times.

################################################################################
# Write your functions below:
# Body

def print_hello(n):
    if(n > 0):
        print("Hello")
        n = n-1;
        print_hello(n)

def do_n(function_name , n):
    print_hello(n)


# # Write your functions above:
# def print_hello():
#     print("Hello World")
################################################################################
def main():
    """Call your function within this function.
    When complete have one function call in this function:
    do_n(print_hello, 10)
    """

    do_n(print_hello,10)

if __name__ == "__main__":
    main()
