#!/usr/bin/env python3
# Sample script that reads from a file
# By Bryce Bezates 2/1/26


with open("hackme.txt", "r") as file:
    data = file.read()

print("Here is someone to hack - information")

print(data)
