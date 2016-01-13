import smbus
import time

bus = smbus.SMBus(1)

address = 0x08

def sendKey(value):
	bus.write_byte(address, value)
	return -1
	
while True:
	var = input("Keypress to send: ")
	if not var:
		continue

sendKey(var)
print("Sending ", var, " via USB keyboard\n")