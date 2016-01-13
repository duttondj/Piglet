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

def sendKey(value):
	"""
		sendKey uses the module-level variables to send the value
		param through the bus to the address. This returns any error
		codes generated from write_byte. The docs really suck for this
		so who knows what it will return.
	"""
	return bus.write_byte(address, value)
	
# Ask for input and check if not null
while True:
	var = input("Keypress to send: ")
	if not var:
		continue

# Output var and any error code from I2C write
print("Sending ", var, " via USB keyboard\n")
print("Error code: ", sendKey(var))