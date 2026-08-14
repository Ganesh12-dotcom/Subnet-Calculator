# IPv4 Subnet Calculator

A Python-based IPv4 subnet calculator that calculates important subnetting information from an IPv4 address and CIDR prefix.

This project was built from scratch as a practical Python and networking project to strengthen my understanding of **IPv4 addressing, CIDR notation, subnet masks, network addresses, broadcast addresses, and host calculations**.

## Features

The calculator accepts:

* IPv4 address
* CIDR prefix length

It then calculates:

* Subnet mask
* Network address
* Broadcast address
* Network bits
* Host bits
* Total addresses
* Usable host addresses
* First usable host
* Last usable host

The program also performs input validation for IPv4 octets and CIDR values.

## Example

### Input

```text
IP Address : 192.168.1.2
Cidr : 26
```

### Output

```text
Subnet Mask : 255.255.255.192
Network Address : 192.168.1.0
Broadcast : 192.168.1.63

Network Bits : 26
Host Bits : 6
Total Address : 64
Usable Hosts : 62
First Host : 192.168.1.1
Last Host : 192.168.1.62
```

## How It Works

The calculator uses the CIDR prefix to determine how many bits belong to the network and how many belong to hosts.

For an IPv4 address:

```text
IPv4 = 32 bits
```

The number of host bits is calculated as:

```text
Host Bits = 32 - CIDR
```

The total number of addresses is then:

```text
Total Addresses = 2 ^ Host Bits
```

For normal IPv4 subnets, usable hosts are calculated as:

```text
Usable Hosts = Total Addresses - 2
```

The two reserved addresses are:

* Network address
* Broadcast address

The project also handles `/31` and `/32` separately.

## CIDR Notation

CIDR stands for **Classless Inter-Domain Routing**.

An address such as:

```text
192.168.1.2/26
```

contains:

```text
192.168.1.2
```

as the IPv4 address and:

```text
/26
```

as the CIDR prefix.

The `/26` means that the first 26 bits are network bits and the remaining 6 bits are host bits.

```text
Network bits : 26
Host bits    : 6
```

Therefore:

```text
2^6 = 64
```

total addresses are available in the subnet.

## Subnet Mask Calculation

The program converts the CIDR prefix into a dotted-decimal subnet mask.

For example:

```text
/26
```

becomes:

```text
255.255.255.192
```

The program calculates the mask using the number of complete network octets and the remaining network bits.

## Network Address Calculation

For CIDR prefixes that fall exactly on an octet boundary, the host octets are set to zero.

For example:

```text
192.168.1.2/24
```

results in:

```text
192.168.1.0
```

For CIDR prefixes that split an octet, the program calculates the subnet block size and determines which block the IP address belongs to.

For example:

```text
192.168.1.2/26
```

has a block size of:

```text
64
```

The possible network blocks are:

```text
0
64
128
192
```

Since `2` belongs to the first block:

```text
Network Address = 192.168.1.0
```

## Broadcast Address Calculation

The broadcast address is the last address in the subnet.

For:

```text
192.168.1.2/26
```

the subnet contains:

```text
192.168.1.0 - 192.168.1.63
```

Therefore:

```text
Broadcast Address = 192.168.1.63
```

## First and Last Host

For a normal subnet:

```text
First Host = Network Address + 1
```

and:

```text
Last Host = Broadcast Address - 1
```

For the `/26` example:

```text
Network Address : 192.168.1.0
First Host      : 192.168.1.1

Broadcast       : 192.168.1.63
Last Host       : 192.168.1.62
```

## Input Validation

The program validates the IPv4 address and CIDR input.

### IPv4 validation

Each IPv4 octet must be between:

```text
0 - 255
```

The program also checks that the IP address contains exactly four octets.

For example:

```text
192.168.1.2
```

is valid.

But an address containing an octet outside the valid range is rejected.

### CIDR validation

The CIDR prefix must be between:

```text
0 - 32
```

Values outside this range are rejected.

## Special CIDR Cases

### `/31`

A `/31` subnet contains two addresses and is commonly used for point-to-point links.

The program treats `/31` separately and reports:

```text
2 usable addresses
```

### `/32`

A `/32` represents a single IPv4 address.

The program treats it as a single-host subnet and reports:

```text
1 usable address
```

## Technologies Used

* **Python 3**
* Python lists
* Strings
* Integer conversion
* `if / elif / else`
* `for` loops
* `try / except`
* Functions
* List copying
* String joining
* Basic mathematical operations
* IPv4 subnetting concepts

## Python Concepts Practiced

While building this project, I practiced several Python concepts:

### User Input

```python
input()
```

Used to receive the IPv4 address and CIDR prefix from the user.

### String Operations

```python
split()
```

Used to separate an IPv4 address into its four octets.

Example:

```text
192.168.1.2
```

becomes:

```text
["192", "168", "1", "2"]
```

### Type Conversion

```python
int()
```

Used to convert the string representation of each octet into an integer.

### Lists

Lists are used to store and manipulate the IPv4 octets.

### Loops

`for` loops are used for:

* Validating octets
* Calculating subnet masks
* Modifying network and broadcast addresses
* Converting address components

### Exception Handling

`try` and `except` are used to handle invalid numeric input.

### Functions

The project includes a function for converting a list of IPv4 octets back into dotted-decimal notation.

For example:

```text
[192, 168, 1, 0]
```

becomes:

```text
192.168.1.0
```

### String Joining

The project uses:

```python
".".join(...)
```

to construct a standard IPv4 address from individual octets.

## Project Structure

```text
subnet-calculator/
│
├── subnetcalculator.py
└── README.md
```

## Requirements

Python 3.x is required.

No external Python packages are required.

The project uses only Python's built-in functionality.

## How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/subnet-calculator.git
```

Move into the project directory:

```bash
cd subnet-calculator
```

Run the program:

```bash
python subnetcalculator.py
```

The program will ask for:

```text
IP Address :
Cidr :
```

Enter the required values.

## Example Test Cases

### Test Case 1 — `/24`

```text
IP Address : 192.168.1.100
CIDR : 24
```

Expected:

```text
Subnet Mask     : 255.255.255.0
Network Address : 192.168.1.0
Broadcast       : 192.168.1.255
Network Bits    : 24
Host Bits       : 8
Total Address   : 256
Usable Hosts    : 254
```

### Test Case 2 — `/26`

```text
IP Address : 192.168.1.2
CIDR : 26
```

Expected:

```text
Subnet Mask     : 255.255.255.192
Network Address : 192.168.1.0
Broadcast       : 192.168.1.63
Network Bits    : 26
Host Bits       : 6
Total Address   : 64
Usable Hosts    : 62
```

### Test Case 3 — `/16`

```text
IP Address : 172.16.20.50
CIDR : 16
```

Expected:

```text
Subnet Mask     : 255.255.0.0
Network Address : 172.16.0.0
Broadcast       : 172.16.255.255
Network Bits    : 16
Host Bits       : 16
Total Address   : 65536
Usable Hosts    : 65534
```

## What I Learned

This project helped me connect Python programming with networking concepts.

The main things I practiced were:

* IPv4 address structure
* CIDR notation
* Network and host bits
* Subnet masks
* Network address calculation
* Broadcast address calculation
* Host address ranges
* Input validation
* Python functions
* Lists and loops
* Exception handling
* String manipulation
* Converting between different representations of an IP address

## Future Improvements

Possible improvements for a future version include:

* Support for IPv6
* Binary representation of the subnet mask
* Binary representation of the IP address
* Subnet class information
* Private/public IP detection
* Automatic IP address type detection
* Better handling of special subnet cases
* Command-line arguments
* More extensive automated testing
* A graphical interface

These are potential future improvements and are **not currently implemented**.

## Disclaimer

This project is intended for learning and educational purposes.

It was created to practice Python programming and IPv4 networking concepts.

## Author

**Ganesh Narute**

Aspiring Cybersecurity Professional

Skills currently being developed:

* Linux
* Networking
* Python
* Bash
* Cybersecurity fundamentals

---
