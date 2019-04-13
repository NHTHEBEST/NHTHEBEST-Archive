
# ATtiny 85 USB Boot Loader

> Purpose :

>

> Program ATtiny using USB and add USB device support

  

---

### Downloads:

* 1

* 2

---

### Hardware:

* 1x ATtiny 85

* 1x Arduino

* 1x Breadboard

* 1x 10uf 25v capacitor

* 6x Jumper wires

  

---

### Instructions:

  

1. Download [files](/static/data/attiny usb boot loader/USB_Boot.zip)

2. Connect

3. Run code

4. Get [Board](https://www.ebay.com/sch/i.html?_nkw=Mini+ATTINY85+Micro+USB+Development+Programmer+Board+for+Tiny85-20PU+DIP-8+IC)

  

#### connect:

Arduino +5V      --->  ATtiny Pin 8

Arduino Ground --->  ATtiny Pin 4

Arduino Pin 10   --->  ATtiny Pin 1

Arduino Pin 11    --->  ATtiny Pin 5

Arduino Pin 12    --->  ATtiny Pin 6

Arduino Pin 13    --->  ATtiny Pin 7

<img  src="/static/data/attiny usb boot loader/52713d5b757b7fc0658b4567.png"  style="height:200PX"/>

Put the 10uF capacitor between ground and the Arduino reset pin. Make sure to keep an eye on the capacitors polarity (ground to ground!).

It is rumored you only need this for the Arduino Uno, but I have found it helped matters to include it with earlier versions as well. If you find that it is not working in the next steps, simple remove it and see if that helps.

Now open the Arduino IDE

Select the "ArduinoISP" sketch from the "Examples" menu

Select your Arduino type and port and flash

#### code:

change com9 with ardoino port

```bat
cd USB_boot

avrdude -c stk500v1 -p attiny85 -C avrdude.conf -b 19200 -U lfuse:w:0xe1:m -U hfuse:w:0xdd:m -U efuse:w:0xfe:m -U flash:w:usb_bootloader.hex:i -P com9
```

#### Finishing

Add this board url ```https://raw.githubusercontent.com/damellis/attiny/ide-1.6.x-boards-manager/package_damellis_attiny_index.json``` 
And add the Digistump AVR Boards 

### Install Drivers
[download](/static/data/attiny usb boot loader/Digistump.Drivers.zip)