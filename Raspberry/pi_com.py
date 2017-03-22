import serial
import time
import glob
import termios

time.sleep(1)
ports = glob.glob('/dev/ttyUSB*')
# Define and open the serial com ports
""" To be added:
BM as Battery Management
MC as Motor Controller
LR as LORA
Exception for termios.error in flush
"""
ser = [0] * 5
port_no = 0
for port in ports:
	try:
		ser[port_no] = serial.Serial(port,9600) 
		port_no += 1
		print port
	except (OSError, serial.SerialException):
		pass
# Wait for initialization
print 'Sleeping for 1 second for initializing'
time.sleep(1)
#print port_no
serial_count = 0;
# Identify the ports
while serial_count != port_no :
	for i in range(0,port_no):
		data_array = ser[i].readline().split("\n")
		usb_id = str(data_array[0])
		if usb_id == 'SC': # If Sensor Controller
			print "SC Identified"
			sc = ser[i]
			sc.write('i') # Send something to sensor controller indicating that we are hearing it 
			print "Connected to Sensor Controller, initializing"
			time.sleep(.5)
			sc.flushInput()
			sc.flushOutput()
			serial_count += 1
		elif usb_id == "RA": # Else if Robotic Arm
			print "RA Identified"
			ra = ser[i]
			ra.write('i') # Send something to sensor controller indicating that we are hearing it 
			print "Connected to Robotic Arm, initializing"
			time.sleep(.5)
			ra.flushInput()
			ra.flushOutput()
			serial_count += 1

# Read the data	
while True:
	if 'sc' in locals():
		try:
			if sc.inWaiting:
				sc.flush()
				sc_data_array = sc.readline().split("\n")
				sc_data_1 = str(sc_data_array[0])
				print "Sc says:", sc_data_1
		except Exception as e:
			pass

	if 'ra' in locals():
		try:
			if ra.inWaiting:
				ra.flush()
				ra_data_array = ra.readline().split("\n")
				ra_data_1 = str(ra_data_array[0])
				print "Ra says:", ra_data_1
		except Exception as e:
			pass		 


