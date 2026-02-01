#!/usr/bin/env python3
# example workign with Loops
#By Bryce bezates on 1/21/2026
# Updated on 2/1/26

def send_message():
    for i in range(10):
        print("Yeah it is")

# Ask the user for input
answer = input("is today a good day? (y/n): ")

# Check the answer
if answer == "y":
    send_message()
elif answer == "Y":
    print("thats amazing!")
if answer == "n":
    print("hopefully it gets better") 