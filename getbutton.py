import serial
arduino = serial.Serial('COM3', 9600, timeout=.1)
while True:
	data = str(arduino.readline()[:-2]) #the last bit gets rid of the new-line chars
	if data == "b'send'":
		print(data)
