import os


file1 = open("for py file test.txt", "a")
file1.write("added new text")
file1.close()

file1 = open("for py file test.txt", "r") # rb for like code binery
print(file1.read())
# print(file1.readline())   # readlines for all line in a list
# print(file1.readline())

