# Exercise 1

Your program should ask two **inputs** from the user:

*“Enter Ip address:”*
*“Enter subnet mask in decimal format:”*

Program **should**:

Check the validity of ip address. If address is invalid, it should generate the error “Invalid IP address format” and prompt again “Enter ip address:”

Check the validity of the subnet mask. If subnet mask is not in decimal format or incorrect, then generate the error “Subnet mask is invalid” and prompt again “Enter subnet mask in decimal format”

The program should present the ip address in the binary formal like in example below (each number in decimal ip address has it’s own row of width 10 symbols).

Your program should print the network address and broadcast address for the given ip.

### Example of the input:

Please enter the ip address: 10.1.1.1

Please enter the subnet mask: /24

### Example of the output:

   10         1         1          1

00001010	00000001	00000001	00000001

network address is: 10.1.1.0/24 
broadcast address is: 10.1.1.255/24 
