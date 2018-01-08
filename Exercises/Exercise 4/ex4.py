# Exercise 4 from Cisco Python Course


#Access and Trunk mode templates
access_template = ['switchport mode access',
'switchport access vlan {}',
'switchport nonegotiate',
'spanning-tree portfast',
'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
'switchport mode trunk',
'switchport trunk allowed vlan {}']


# Request User Input
Interface_mode = input("Enter interface mode (access/trunk): ")
Interface_Type_Number = input("Enter interface type and number: ")


# Access Mode
if (Interface_mode == "access"):
	VLAN_Number = input("Enter VLAN Number: ")
	print ("Interface ",Interface_Type_Number)
	for i in range(len(access_template)):
			print(access_template[i].format(*VLAN_Number))
# Trunk Mode
elif (Interface_mode == "trunk"):
	Allowed_VLANs = input("Enter allowed VLANs: ")
	print ("Interface ",Interface_Type_Number)
	for i in range(len(trunk_template)):
			print(trunk_template[i].format(Allowed_VLANs))
	#Format allowed VLANs to List
	Allowed_VLANs = list(map(int,Allowed_VLANs.split(',')))	
# Error Message if wrong mode is entered
else:
	print("Wrong Interface Mode. Terminating ...")


