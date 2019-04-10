# ATtiny 85 USB Boot Loader
>  Purpose  :
>
>  Program ATtiny using USB 
>  and add USB device support

---
Downloads:
[USBaspLoader-tiny85.2012-05-13.zip](https://github.com/downloads/embedded-creations/USBaspLoader-tiny85/USBaspLoader-tiny85.2012-05-13.zip)

GitHub Repo:
[USBaspLoader-tiny85 on github](https://github.com/embedded-creations/USBaspLoader-tiny85)

---
### Hardware:
* ATtiny 85
* Arduino 
* Breadboard
* Jumper wires
---
### Instructions:

 Download the boot loader precompiled hex file or download the source and compile yourself. If you want to use one of the precompiled hex file, reference the fuse settings contained in the makefile and program the flash and fuses using your preferred tools.

Modify the makefile to correct use your preferred AVR programming tool.

Program the boot loader to the tiny85 flash using ```make flash```. Set the fuses appropriately: ```make fuse``` leaves the external reset functionality enabled.

Download the USBasp driver if you need it for Windows. See "drivers" on the  [USBasp](http://www.fischl.de/usbasp/)  homepage.

At this point AVRDUDE should be able to connect to the tiny85 as a USBasp programmer, try reading the signature:
```
avrdude -p attiny85 -c usbasp

avrdude: warning: cannot set sck period. please check for usbasp firmware update
avrdude: AVR device initialized and ready to accept instructions
Reading | ################################################## | 100% 0.04s
avrdude: Device signature = 0x1e930b
avrdude: safemode: Fuses OK
avrdude done. Thank you.
```
Download the modified version of AVRDUDE or download the  [source](http://download.savannah.gnu.org/releases/avrdude/avrdude-5.11.tar.gz), apply the patch, and compile yourself.

Use the modified version of AVRDUDE to program an application on the tiny85, and make sure it verifies successfully. The boot loader code should jump to the application shortly after AVRDUDE disconnects.

To replace or update the application, disconnect and reconnect the USB cable (or otherwise reset the tiny85). The boot loader will connect to the PC as a USBasp programmer for 5 seconds before jumping to the application. If the application is invalid or erased, the boot loader will stay connected as a USBasp programmer until a new application is loaded successfully.

If you need an extra I/O line you can use ```make disablereset``` to disable external reset functionality, allowing reset to be used for I/O - only set this after you're sure the boot loader is working.

---

# [NOT DONE](http://www.embedded-creations.com/projects/attiny85-usb-bootloader-overview)
