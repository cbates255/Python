#!/bin/python3

message = input("Enter a message: ")

print("First character:", message[0])
print("Last character:", message[-1])
print("Middle character:", message[int(len(message) / 2)])