## Proove power outlet controller for Raspberry Pi

This python script was created to remotely control power outlets of the brand Proove from a Raspberry Pi.

**RF transmitter:**
http://www.ebay.com/itm/433Mhz-RF-transmitter-and-receiver-link-kit-for-Arduino-ARM-MCU-WL-/140719918135
or any similar kind will work

**Power Outlets used:**
https://www.kjell.com/se/sortiment/el-verktyg/smarta-hem/433-mhz/fjarrstrombrytare/utanpaliggande-brytare/telldus-fjarrstrombrytare-3680-w-3-pack-p50813

To find out more about the protocol used by these power outlets i recommend this page that was of great help http://tech.jolowe.se/home-automation-rf-protocols/ .
There is also information how to adjust the protocol to control other similar power outlets from other brands.

## Usage

The script defaults to the GPIO pin BCM 22 which you might want to change.
To find what pin and BCM number to use this page is very useful: https://pinout.xyz/


Running the script:
```
./proove_433_transmitter.py <code>
```
