#Exercise 1 from Cisco Python Course

import re

#Check IP address validity

#Pattern for IP which has XXX.XXX.XXX.XXX format with range from 0.0.0.0 to 255.255.255.255
IP_pattern = "^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.)){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)($)"

while True:
	ip_addr = input("Enter IP address:")
	if re.search(IP_pattern,ip_addr): #check that the IP address matches the pattern
		ipaddr_octets = list(map(int,ip_addr.split('.'))) #split the IP address into a list of its 4 octets
		break
	else:
		print("Invalid IP address format")

#Checking Subnet Mask validity

#Pattern for Subnet Mask which has /XX format with range from 0 to 32
SubMask_pattern ="\/([1-2]?[0-9]|3[0-2])$"

while True:
	subnet_mask = input("Enter subnet mask in decimal format:")
	searchMask = re.search(SubMask_pattern,subnet_mask)

	if searchMask: #if mask is in the correct form

		#create Subnet Mask in binary
		subnet_maskB = ('1'*int(searchMask.group(1))).ljust(32,'0')  #group(1) is the CIDR i.e. the number of ones in 32-bits of subnet mask, the rest are filled with zeros

		# Make Subnet Mask into a list of 4 8-bits elements/octets
		subnet_maskB = [subnet_maskB[i:i+8] for i in range(0,32,8)]
		# Convert the 8-bit strings to integers to be able to use bitwise operators
		for i in range(4):
			subnet_maskB[i] = int(subnet_maskB[i],2)
		break
	else:
		print("Subnet mask is invalid")

#Get the binary equivalent
ipaddr_octetsB = list(map(bin,ipaddr_octets))
for i in range(len(ipaddr_octetsB)):
	ipaddr_octetsB[i] = ipaddr_octetsB[i].split('b')[1].zfill(8) # 8-bit binary conversion

#Print ip address in decimal and binary format
print ('{0:10} {1:10} {2:10} {3:10}'.format(*ipaddr_octets))
print (' '.join(item for item in ipaddr_octetsB))


#Create the network address & broadcast address

#initiliaze the addresses
network_addr = [0]*4
brocast_addr = [0]*4

# network address = IP address AND Subnet mask(CIDR)
for i in range(4):
	network_addr[i] = str(ipaddr_octets[i] & subnet_maskB[i])

#broadcast address = IP address OR inverse of Subnet Mask(CIDR)
for i in range(4):
	brocast_addr[i] = str(ipaddr_octets[i] | (0xFF ^ subnet_maskB[i]))

#Printing the addresses in the format requested
print("network address is: " + '.'.join(item for item in network_addr) + subnet_mask)
print("broadcast address is: " + '.'.join(item for item in brocast_addr) + subnet_mask)
