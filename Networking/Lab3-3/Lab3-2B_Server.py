""" Ricky Smith, Networking:  Lab 3-2B Server, 24 Sept 2018 """

from socket import *

# creates socket to be used
s = socket(AF_INET, SOCK_DGRAM)

# binds socket with the listening port 12345
s.bind(("",12345))


# only does something when true (i.e., waits to recieve)
string1, addr = s.recvfrom(1024)
print("\n==========\n\n{}\n\n===========\n".format(addr))

IPadd = addr[0]
IPport = addr[1]

newAddr = (IPadd, IPport + 1)


print("\n==========\n\n{}\n\n===========\n".format(newAddr))

print("\nRecieved String is:\n{}\n").format(string1)

list1 = string1.split()
list2 = sorted(list1, key=len)

print("String Split into Words are:\n{}\n").format(list1)

string2 = " ".join(list2)

print("Same String with words reversed is:\n{}\n".format(string2))

# newS = socket(AF_INET, SOCK_DGRAM)
# newS.bind(("",12345))

s.sendto(string2, newAddr)

