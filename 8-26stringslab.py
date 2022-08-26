#!/bin/python3

message = input("Enter a message: ")

print('Lowercase:', message.lower())
print('Uppercase:', message.upper())
print('Capitaliszed:', message.capitalize())
print('Title Case:', message.title())

#Separating the words from the message
words = message.split()
print('Words:', words)

#Sorting out the words from the message alphabetically
sorted_words = sorted(words)
print('Alphabetic First Word: ', sorted_words[0])
print('Alphabetic Last Word: ', sorted_words[-1])