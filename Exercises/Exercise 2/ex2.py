# Exercise 2 from Cisco Python Course

import re
from functools import reduce

# Pattern that acceps only the "switchport trunk allowed vlan ..." commands
Comm_pattern = "^switchport trunk allowed vlan (.*)$"

# Read the file and put each line in a list
file = [line.rstrip('\n') for line in open('commands.txt')]

#Initiliaze list of sets for the valid commands
VLAN_comms = []

#Search each line for the valid commands 
for line in range(len(file)):
	LineComm = re.search(Comm_pattern,file[line])
	if LineComm:
		#put each sequence of VLANs as a unique set in VLAN_comms list
		VLAN_comms.append(set(map(int,LineComm.group(1).split(','))))
	else:
		continue

for i in range(len(VLAN_comms)):
	#Common VLANs i.e. those who appear to ALL the VLAN commands in the file
	Set_1 = reduce(lambda a,b:a&b,VLAN_comms)
	#Unique VLANs i.e. those who appear in only one VLAN command in the file
	Set_2 = reduce(lambda a,b:a^b,VLAN_comms)


#Convert to required list format and print the results (elements of List are integers for easier manipulation)
List_1 = sorted(list(Set_1))
List_2 = sorted(list(Set_2))

print (List_1)
print (List_2)
