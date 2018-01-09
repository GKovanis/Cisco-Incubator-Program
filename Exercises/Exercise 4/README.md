# Exercise 4

Exercise4:

You are given the following templates (just put them as it is in your script):

access_template = ['switchport mode access',  
'switchport access vlan {}',  
'switchport nonegotiate',  
'spanning-tree portfast',  
'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',  
'switchport mode trunk',  
'switchport trunk allowed vlan {}']

**Your program should ask:**

‘Enter interface mode (access/trunk):’  
‘Enter interface type and number:’  
For access interfaces, script should request “Enter VLAN number”.   
For trunk interface, script should request list of allowed vlans “Enter allowed VLANs:”.  
  
Your script should print the configuration depends on the input.

## Example:

### Input:

Enter interface mode (access/trunk): *access*  
Enter interface type and number: *Fa2/1*  
Enter VLAN number: *5*

### Output:  

Interface Fa2/1  
switchport mode access  
switchport access vlan 5  
switchport nonegotiate  
spanning-tree portfast  
spanning-tree bpduguard enable  
