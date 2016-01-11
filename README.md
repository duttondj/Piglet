# Piglet
<img src="https://cdn.rawgit.com/duttondj/Piglet/master/docs/blockdiagram.svg" alt="Blockdiagram" height="350">

The Piglet is an Out-of-Band Management (OOBM) device based on a Raspberry Pi (master) and a small microcontroller. It can handle serial communications, USB emulation, and direct control of headers on a slave computer motherboard.

## Breakdown

### Overview
The Raspberry Pi B+ (master) runs Arch Linux ARM and contains software for easy interfacing with the machine you wish to control. There is a `pigletctl` program that is run via an SSH console that can manipulate the GPIO pins to control either the direct connections to the slave, can open a new serial terminal to the slave, or will talk to a slave Teensy 3.2 microcontroller to direct it to send emulated key presses.

### Hardware
Running is a Raspberry Pi B+ and a Teensy 3.2. Additional components included are a logic level converter for converting the Pi's 3.3V to 5V for serial communications and a SN7400 quad NAND logic chip used to display power status for both boards on one LED. The Pi may be connected to the Teensy, pending more research, so it can be updated with new code so all maintenance can be remote and the box not be opened. There is also a power switch (momentary pushbutton) on the box that will reset both the Pi and Teensy if need be. The Pi is directly wired to the slave computer's motherboard so that it can mimic power and reset button presses. It can also read the voltage across the power status LED to determine if the slave computer is on (or may determine power status through some other manner pending research).

### Software
`pigletctl` is built using python/C/C++/shell scripting. It shows a menu which lists various tasks such as:

* SEND POWER ON
* SEND POWER OFF
* SEND RESET
* CHECK POWER STATUS
* OPEN NEW SERIAL TERMINAL
* SEND KEY PRESSES

Opening a new serial console would simply bring up a connection to the slave computer using the Linux serial console with a console program like minicom.

Sending key presses would allow you to enter in a string of ASCII characters or allow you to pick from a list of non-typable ASCII characters like arrows, return, backspace, etc. This command would then be sent via I2C/SPI to the slave Teensy where it would act as a USB HID and send keypress commands to the slave computer.

`pigletctl` may later be a daemon so that commands can be sent quicker to the slave computer such as `pigletctl on` or `pigletctl send return_key`.

The Teensy will run C code created using Arduino sketches to ease the use of its HID libraries as this is the primary use.

## Goals
### Needs
* Piglet is as portable as possible: attaching to a new system should not be any more work than connecting plugs
* Minimal hardwiring for both boards (use headers where possible)
* Raspberry Pi must have no soldered connections
* Raspberry Pi accessible via SSH via Ethernet LAN
* Raspberry Pi can access slave computer via serial
* Raspberry Pi can access slave computer's power button header
* Raspberry Pi can access slave computer's reset button header
* Raspberry Pi can determine slave computer's power status
* Raspberry Pi can communicate with Teensy over I2C/SPI
* Teensy can send key presses over USB to slave computer
* Piglet power button resets both boards
* Piglet power status LED shows status for both boards
* `pigletctl` should be as small as possible or should rely on as few libraries as possible (depending on language)

### Wants
* Piglet access over a 3G/4G modem with an external antenna in the case of Internet service loss (costs money unless a pay as you go solution can be found)
* Web dashboard for running commands (power control, serial, etc) and checking status with various access control
* Android app for managing Piglet, similar to RasPi Check
* Configure Teensy in some way that allows both HID connection to slave computer and a USB connection to the Pi flashing new firmware for future features
* Interface with the current temperature display on slave computer to get values or add in dedicated temperature sensors for Piglet
* Capture the slave computer's VGA output and save as an image (streaming is expensive)

## Future Analysis
The Teensy seems like a very capable board and using it strictly for keyboard emulation is a shame. I may add additional features later to use the other pins on the board so that it can control more things. I might even move the power control to the Teensy so that the Pi's GPIO pins can be freed for things like an LCD status screen. If I want to add temperature sensors, I may need to just move all of that to the Teensy and have the Pi strictly as the master control device. Something like a BeagleBone or Arduino with an Ethernet shield might even be capable of doing what I want and trim some fat. Plus, this would give me the chance of moving the project from a hobbyist board to a dedicated board, reducing size and power usage. However, not having a Linux environment might make some tasks more difficult and might end up having me rely on single channels of communication like a web dashboard due to less general capability. Whereas a Pi will give me SSH and web access if I want it.
