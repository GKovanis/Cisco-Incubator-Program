# Exercise 2

Your program should read the content of the file **commands.txt** which contains list of different commands (each command is in a new line). Your program should look only for commands "switchport trunk allowed vlan ..."  all other commands should be ignored. 
(Example of the good command “switchport trunk allowed vlan 1,3,5,11,25,111,23,8”.)

**Your program should**:

1. print list of all common vlans in all commands, i.e. any good command from commands.txt contains this vlan
2. print list of all unique vlans, i.e for any vlan number from this list there should be only one command in the commands.txt file containing this vlan.
3. the output lists should not contains duplicated entries and should be sorted in accidental order.

### Example of the commands.txt:

switchport trunk allowed vlan 1,3,5,11,25,111,23, 8  
switchport trunk allowed vlan 1,11,5,8,111,100,77,75  
switchport trunk allowed vlan 5,111,77,88,44,8,112,11,8   
switchport mode auto

### Example of the output:

List_1=[‘5’,’8’,’11’,’111’]  
List_2=[‘3’,’23’,’25’,’44’,’75’,’88’ ,’100’,’112’]
