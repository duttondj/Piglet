#!/usr/bin/env python

__author__ = "Danny Dutton"
__credits__ = []
__maintainer__ = "Danny Dutton"

__license__ = "MIT"
__email__ = "duttondj@vt.edu"
__status__ = "Prototype"

# Built-in modules:


# Third-party modules:
import smbus


bus = smbus.SMBus(1)
"""bus: The I2C bus we are using. In the Raspberry Pi B+, this is 1.
In other versions, this may be a 0. Read your documentation.
"""

address = 0x08
"""address: This is a hardcoded I2C address of the Teensy. This is 
specified in the Teensy code and can be changed but both must match.
"""

data_reg = 0x00
"""data_reg: This value is not really used because we are not sending
the data to any specific register so 0x00 will do.
"""

def sendKey(value):
	"""
		sendKey uses the module-level variables to send the value
		param through the bus to the address. It first converts the
		string into a list of ascii codes then sends. This returns any
		error codes generated from write_byte. The docs really suck
		for this so who knows what it will return.
	"""
	ascii = [ord(ch) for word in value for ch in word]
	return bus.write_i2c_block_byte(address, data_reg, value)
	
# Ask for input and check if not null
while True:
	char = input("Keypresses to send (32 char limit): ")
	if (char and (len(char) <= 32)):
		break

# Output char and any error code from I2C write
print("Sending ", char, " via USB keyboard\n")
print("Error code: ", sendKey(char))