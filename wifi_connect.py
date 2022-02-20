import os
import time

def choice_ap():
	tmp = ''
	apList = list()
	while tmp == '':
		try:
			tmp = os.popen("sudo iwlist wlan0 scan | egrep \'ESSID|Signal\'").readlines()
		except:
			pass

	tmp = [i.replace(' ','').replace('\n','') for i in tmp]
	for i in range(0,len(tmp),2):
		rssi = tmp[i].split('=')[-1]
		print(f'{i/2:.0f}. {tmp[i+1]} rssi = {rssi}')
		apList.append(tmp[i+1].split(':')[-1].replace('\"',''))
	num = ''
	while num == '':
		try:
			num = int(input("Choice a number for connect ap :"))	
		except:
			print("Please enter a number!")
	return apList[num]

def init_wlan_interface():
	info = os.popen("sudo kill -9 $(ps -ef | grep wpa | awk \'{print $2}\')")
	for i in info:
		print(i)
	time.sleep(1)
	info = os.popen("sudo wpa_supplicant -B -i wlan0 -c /etc/wpa_supplicant/wpa_supplicant.conf")
	for i in info:
		print(i)
	try:
		time.sleep(1)
		info = os.popen("sudo wpa_supplicant -B -i wlan1 -c /etc/wpa_supplicant/wpa_supplicant.conf")
		for i in info:
			print(i)
	except:
		print("Don't have wlan1 interface.")
ap = choice_ap()
print(ap)
password = str(input("Please enter the password : "))

with open("/etc/wpa_supplicant/wpa_supplicant.conf", 'w') as f:
	f.write("ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n")
	f.write("update_config=1\n")
	f.write("country=TW\n\n")
	f.write("network={\n")
	f.write(f"\tssid=\"{ap}\"\n")
	f.write(f"\tpsk=\"{password}\"\n")
	f.write("}\n")

init_wlan_interface()
print("Process done!")
