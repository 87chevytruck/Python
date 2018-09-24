""" Ricky Smith, Networking:  Lab 3-2B Client, 24 Sept 2018 """

from socket import *

s = socket(AF_INET, SOCK_DGRAM)

string1 = "My name is Ricky Smith, and I am the coolest dude ever."

s.sendto(string1,("192.168.31.132", 12345))

print("\n\nThis is what I sent:\n{}\n").format(string1)

print("\n===============================\n")

string2, addr = s.recvfrom(1024)

print("This is what I received:\n{}\n").format(string2)
