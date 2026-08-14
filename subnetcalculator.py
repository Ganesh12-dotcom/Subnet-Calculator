ip = input("IP Address : ")
cidr = int(input("Cidr : "))
ipsplit = ip.split(".")
valid = True
newlist = []
length = len(ipsplit)


network_octet = cidr // 8
remaining_network_bits = cidr % 8
host_bits = 32 - cidr
total_address = 2 ** host_bits

if cidr < 0 or cidr > 32:
    print("enter a valid cidr")
    valid = False

if length != 4:
    print("the length of ip is not 4")
    valid = False
for numbers in ipsplit:
    try:
        convert_numbers = int(numbers)
        if convert_numbers < 0 or convert_numbers > 255:
                print(f"enter a proper ip and {convert_numbers} is not in ip range")
                valid = False
        else:
             newlist.append(convert_numbers)
      
    except ValueError:
        print("the number is string")
        valid = False
if not valid:
    exit()
        

if remaining_network_bits == 0:

    for numbers in range(network_octet, length):
        newlist[numbers] = 0

    broadcast_list = newlist.copy()
    #print(f"Network Address : {newlist}")


    for numbers in range(network_octet,length):
     broadcast_list[numbers] = 255

    #print(f"Broadcast : {broadcast_list}")

else:
   
    host_bits_in_boundary_octet = 8 - remaining_network_bits
    
    block_size = 2 ** host_bits_in_boundary_octet

    boundary_octet_value = newlist[network_octet]
    block_number = boundary_octet_value // block_size
    network_boundary_value = block_number * block_size
   
    newlist[network_octet] = network_boundary_value
    for numbers in range(network_octet+1,length):
        newlist[numbers] = 0

    #print(f"Network Address : {newlist}")


    broadcast_list = newlist.copy()
    
    broadcast_address = network_boundary_value + block_size
    broadcast_address = broadcast_address -1
    broadcast_list[network_octet] = broadcast_address


    for numbers in range(network_octet + 1, length):
        broadcast_list[numbers] = 255
    #print(f"Broadcast : {broadcast_list}")

   

if cidr == 31:
    print("special /31 subnet: 2 usable addresses")
elif cidr == 32:
    print("single-host /32 subnet")

else:
    first_host = newlist.copy()
    first_host[-1] = first_host[-1] + 1

    last_usable_host = broadcast_list.copy()
    last_usable_host[-1] = last_usable_host[-1] - 1


#print(f"Usable hosts : {usable_hosts}")

subnet = [0,0,0,0]
if cidr == 32:
    subnet = [255,255,255,255]
else:
    for number in range(0,network_octet):
        subnet[number] = 255

    partial_mask = 0
    for number in range(remaining_network_bits):
        partial_mask = partial_mask + 2** (7 - number)
        subnet[network_octet] = partial_mask

if cidr == 31:
    usable_hosts = 2
elif cidr == 32:
    usable_hosts = 1
else:
    usable_hosts = total_address - 2






def convert_to_ip(ip_list):
    convert_list = []
    for numbers in ip_list:
        convert = str(numbers)
        convert_list.append(convert)
    join = ".".join(convert_list)
    return join
network_address = convert_to_ip(newlist)
broadcast_address = convert_to_ip(broadcast_list)
Subnet_Mask = convert_to_ip(subnet)
first_host = convert_to_ip(first_host)
last_usable_host = convert_to_ip(last_usable_host)

print(f"Subnet Mask : {Subnet_Mask}")
print(f"Network Address : {network_address}")
print(f"Broadcast : {broadcast_address}")
print("")
print(f"Network Bits : {cidr}")
print(f"Host Bits : {host_bits}")
print(f"Total Address : {total_address}")
print(f"Usable Hosts : {usable_hosts}")
print(f"First Host : {first_host}")
print(f"Last Host : {last_usable_host}")
