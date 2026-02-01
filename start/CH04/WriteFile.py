#!/usr/bin/env python3
# Sample script that writes to a file
# By Bryce Bezates 2/1/26

name  = input("What is you name? ")
color = input("What is your favorite color? ")
pet = input("What was your first pet's name? ")
mother_maiden = input("What is your mother's maiden name? ")
school = input("What elementary school did you attend? ")

with open("hackme.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Favorite Color: " + color + "\n")
    file.write("First Pet's Name: " + pet + "\n")
    file.write("Mother's Maiden Name: " + mother_maiden + "\n")
    file.write("Elementary School: " + school + "\n")

print("Information saved to hackme.txt")