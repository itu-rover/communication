import serial
import time

# Define and open the serial com ports
ser = [0] * 5
ser[0] = serial.Serial('/dev/ttyUSB0', 9600)
ser[1] = serial.Serial('/dev/ttyUSB1', 9600)

# Wait for initialization
print 'Sleeping for 1 second for initializing'
time.sleep(1)

serial_count = 0;
# Identify the ports
while serial_count != 2:
	for i in range(0,2):
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

	sc.flush()
	sc_data_array = sc.readline().split("\n")
	sc_data_1 = str(sc_data_array[0])
	print "Sc says:", sc_data_1
	ra.flush()
	ra_data_array = ra.readline().split("\n")
	ra_data_1 = str(ra_data_array[0])
	print "Ra says:", ra_data_1 
