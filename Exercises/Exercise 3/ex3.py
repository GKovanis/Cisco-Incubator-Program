# Exercise 3 from Cisco Python Course

import re


# Codes Pattern to extract all the Codes in the beginning of the file
Codes_pattern = "(\S*) - ([^,]*)"
Codes = {}

# Read the file and put each line in a list
file = [line.rstrip('\n') for line in open('ShowIpRoute.txt')]


for line in range(len(file)):
	LineSearch = re.findall(Codes_pattern,file[line])
	#Find all the Codes in the file
	if LineSearch:
		#Multiple matches in a line, we extract all of them using for
		for j in range(len(LineSearch)):
			#Create a dictionary with all the available Codes and Protocols as key-value pairs
			Codes[LineSearch[j][0]] = LineSearch[j][1]
	# Break when you meet the "Gateway ..." line as there are no more Codes
	if (file[line][0:7] == "Gateway"):
		break

# Result Pattern to extract the required data to print, 
### THIS REGEX DOESN'T FIND THE CONNECTED DEVICES ###
Result_Pattern = """
^					#Beginning of String
(.+?(?=\ \d))\ *	#Match one or More Codes
(\S*)\ *			#Match the prefix
(\[(.*?)\])?\ 		#Match the AD/Metric (may not have one if directly connected)
(via\ )?			#Match the "via " word if it is not directly connected
(.*)?,\ 			#Match the Next-Hop
(.*)?,\ 			#Match the Last Update  
(.*)				#Match the Outbound interface
"""

#Regex for Connected Code ONLY
Connected_Pattern = """
(C)\ * 		 		     #Match Connected Code
(\S*)\ *				 #Match the prefix
(\S*)\ *				 #Match the Next-Hop
([^,]*),\ *  			 #Match the specific string for direct connections
(\S*)\ *
"""
#
#(\S*).*					 #Match the Outbound interface

#Continue to the lines that have the show ip route results
for line in range(line+1,len(file)):
	#Match the Lines to the Pattern
	LineSearch = re.search(Result_Pattern,file[line],re.VERBOSE)
	
	#Print the output as requested

	#Find a non-direct connection matching string
	if LineSearch:

		#Check if there is a candidate default symbol ('*'), if there is, proper action is needed since it doesn't have a whitespace between codes
		LineCode = LineSearch.group(1)
		if ('*' in LineCode):
			LineCode = LineCode.replace('*',' * ').rstrip()

		#Protocols may have more than one Codes
		Protocols = LineCode.split(' ')

		#Print Desired Output
		print("Protocol: 			", ','.join(Codes[item] for item in Protocols))
		print("Prefix: 			",LineSearch.group(2))
		print("AD/Metric: 			",LineSearch.group(4))
		print("Next-Hop: 			",LineSearch.group(6))
		print("Last Update:			",LineSearch.group(7))
		print("Outbound interface		",LineSearch.group(8))
		print()
	else:
		
		#Check if we have a Code Connected Line
		if file[line].startswith('C'):
			ConnectedLine = re.search(Connected_Pattern,file[line],re.VERBOSE)

			#Print Desired Output
			if ConnectedLine:
				print("Protocol: 			",Codes[ConnectedLine.group(1)])
				print("Prefix: 			",ConnectedLine.group(2))
				print("AD/Metric: 			")
				print("Next-Hop: 			",ConnectedLine.group(3))
				print("Last Update:			",ConnectedLine.group(4))
				print("Outbound interface		",ConnectedLine.group(5))
				print()


	