# Ducky Script to USB Enabled ATTiny 

### Requirements 
- Linux
- Java
- Python

### What to do
1.  Download [Ducky Encoder](static/data/ducky script to usb enabled attiny/duckencoder.jar) and [Duck2Spark](static/data/ducky script to usb enabled attiny/duck2spark.py) 
2. Run ```java -jar duckencoder.jar -l us -o inject.bin -i <your ducky script>```
3. Run ```python duck2spark.py -l 1 -f 2500 -r 3000 -i inject.bin -o <project name>.ino```
4. Flash ```<project name>.ino``` to USB Enabled ATTiny 