# db_level_sensor describe
This is a db level sensor, send data by wifi to the custom api

## Material
1. raspberry pi
![raspberry pi](https://github.com/Dan19920406/db_level_sensor/blob/main/picture/raspberry_pi.png)
2. FT232 * 2
![FT232](https://github.com/Dan19920406/db_level_sensor/blob/main/picture/FT232.png)
3. sensor
> spec <https://www.taiwansensor.com.tw/product/工業級噪音分貝感測器模組-高精度分貝計模組-ttl-uart-輸/>
![sensor](https://github.com/Dan19920406/db_level_sensor/blob/main/picture/db_level_sensor.png)

## Following the step by step and finish the project
### 1. Raspberry pi setting
1. Use Raspberry Pi Imager install os to SD card
> - Enable SSH
> - Configure wifi
![imager](https://github.com/Dan19920406/db_level_sensor/blob/main/picture/raspberry_pi_imager.png)
2. Power on your raspberry pi
3. Find your raspi in the intranet
4. SSH connection
5. sudo raspi-config and enable serial port
6. sudo nano /boot/config.txt add "dtoverlay=pi3-disable-bt" to avoid the serial connection with garbled text
7. scp the file to raspi
8. python
> 1. sudo apt-get update
> 2. sudo apt-get install python3-pip
> 3. pip3 install pyserial
9. Connect by serial port

### 2. Configure raspi's wifi
1. sudo python3 wifi_connect.py
2. Enter a number the ESSID you choice.
![choice ap](https://github.com/Dan19920406/db_level_sensor/blob/main/picture/configure_wifi.png)
3. Enter the ap password

### 3. Configure the serial_port.in
1. Hardware connection

FT232 >> Sensor

RX --------- TX

VVC -------- 5V

GND ------- GND

2. raspi type "ls /dev/tty*" find the serial port
3. Modify the .in file content

### 4. Data upload
1. Open send_db_level.py
> - Change the internalUrl and externalUrl to your own api
> - Change the requests.post data to your own format
2. Execute the send_db_level.py



