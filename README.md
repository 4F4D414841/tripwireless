# Trip Wire(less)

This is the documentation and code presented at the [2019 ShmooCon](https://www.shmoocon.org/speakers/#tripwire) hacking conference. Abstract:

>At DEF CON 26, multiple guests of Caesars Entertainment properties were taken off-guard by the security practices employed by the hotel chain. A series of alarming tweets ignited significant press coverage, highlighting the inconsistent and poorly-published hotel policies. DEF CON management met with Caesars representatives, and were informed that while a Do Not Disturb sign will trigger a security visit by “clearly identifiable” hotel staff, no belongings should be disturbed, opened, or taken.
>
>Planning on staying at Caesars property for DEF CON 27, or just concerned about privacy while traveling in general? This presentation will show you how to set up customizable travel “trip wires” that operate over 433 MHz and fit in a small toiletries case. With a Raspberry Pi, less than $20 worth of supplies, and an hour of spare time, you can configure 4 or 5 sensors that will alert you if your favorite things are moved, opened, or disturbed while you’re away from the room. 

## Dependencies
Install pigpio and associated Python3 libraries.
```
sudo apt-get install pigpio
sudo systemctl start pigpiod   		# start daemon
sudo systemctl status pigpiod  		# confirm daemon active
sudo pip3 install pgiozero pigpio
```
Handy charts to figure out which pins you want to use.
```
pinout
gpio readall
```
Optional: Download \_433.py from the [pigpio examples library](http://abyz.me.uk/rpi/pigpio/examples.html) if you don't want to use the copy in this repo.
```
wget http://abyz.me.uk/rpi/pigpio/code/_433_py.zip
unzip _433_py.zip
```

## Other notes
This script is currently set up to detect and name new codes each time it runs. You can hard-code the codes into the script if you already know them.