#!/usr/bin/env python3
# example workign with Loops
#By Bryce bezates on 1/21/2026

# Ask the user for input
answer = input("is today a good day? (y/n): ")

# Check the answer
if answer == "y":
    for i in range(10):
        print("Yeah it is")
elif answer == "Y":
    print("thats amazing!")
if answer == "n":
    print("hopefully it gets better") 