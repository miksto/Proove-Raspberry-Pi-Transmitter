## Proove power outlet controller for Raspberry Pi

This python script was created to remotely control power outlets of the brand Proove from a Raspberry Pi.

**RF transmitter:**
http://www.ebay.com/itm/433Mhz-RF-transmitter-and-receiver-link-kit-for-Arduino-ARM-MCU-WL-/140719918135
or any similar kind will work

**Power Outlets used:**
https://www.kjell.com/se/sortiment/el-verktyg/smarta-hem/433-mhz/fjarrstrombrytare/utanpaliggande-brytare/telldus-fjarrstrombrytare-3680-w-3-pack-p50813

**The Protocol**
To learn more about the protocol and how to create commands for the power outlets I recommend a visit to these two pages:
http://tech.jolowe.se/home-automation-rf-protocols/ and http://tech.jolowe.se/home-automation-rf-protocol-update/ .
There you will also find information on how to adjust the protocol to control similar power outlets from other brands.

## Usage

The script defaults to the GPIO pin BCM 22 which you might want to change.
To find what pin and BCM number to use this page is very useful: https://pinout.xyz/

The script uses **pigpio** to generate the pulses for the GPIO pin, and a **pigpio daemon** needs to to be running.
Download and installation instructions are available here: http://abyz.co.uk/rpi/pigpio/download.html

Sending a command:
```
sudo pigpiod    #Start the pigpio daemon
./proove_433_transmitter.py 00101010001001010010110001100000 #send command
```
