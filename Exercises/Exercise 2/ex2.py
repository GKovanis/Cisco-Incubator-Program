# Exercise 2 from Cisco Python Course

import re
import sys
from collections import defaultdict 

# Pattern that accepts only the "switchport trunk allowed vlan ..." commands
Comm_pattern = "^switchport trunk allowed vlan (.*)$"

# Read the file and put each line in a list
file = [line.rstrip('\n') for line in open('commands.txt')]

#Initiliaze list of lists for the valid commands
VLAN_comms = []

#Search each line for the valid commands 
for line in range(len(file)):
	LineComm = re.search(Comm_pattern,file[line])
	if LineComm:
		#put each sequence of VLANs as a unique list in VLAN_comms list
		#set function is used to remove possible duplcates in the command (as shown in the example)
		try:
			VLAN_comms.append(list(set(map(int,LineComm.group(1).split(',')))))
		except:
			#In case a non-number value was entered either the VLANs were not separated by comma, the program terminates
			print ("A wrong value was entered as VLAN in line",line,".Exiting...")
			sys.exit(1)
	else:
		continue

#frequency dictionary counts the occurences of a VLAN in the commands
freq_VLAN = defaultdict(int)

#Create the frequency table for each VLAN
VLAN_comms_number = len(VLAN_comms)

for i in range(VLAN_comms_number):
	for j in range(len(VLAN_comms[i])):
		freq_VLAN[VLAN_comms[i][j]] += 1


# Since all VLANs appear once in a command, frequency table gives us the results we want
# Common VLANs will have frequency equal to that of the number of commands (each command will have this VLAN)
# Unique VLANs will have frequency equal to one(only one command will include this VLAN)
List_1 = []
List_2 = []

for k,v in freq_VLAN.items():
	if (v == VLAN_comms_number):
		List_1.append(k)
	elif (v == 1):
		List_2.append(k)

#Sort the Lists and print the results
List_1 = sorted(List_1)
List_2 = sorted(List_2)

print ("List_1 =",List_1)
print ("List_2 =",List_2)
