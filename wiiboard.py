import bluetooth
import time


#values to send to wii fit board(hex) source: https://github.com/skorokithakis/gr8w8upd8m8/blob/master/gr8w8upd8m8.py
CONTINUOUS_REPORTING = "04" 

#command values for ligts, registering, reading, reporting
COMMAND_LIGHT = 11
COMMAND_REPORTING = 12
COMMAND_REQUEST_STATUS = 15
COMMAND_REGISTER = 16
COMMAND_READ_REGISTER = 17

INPUT_STATUS = 20
INPUT_READ_DATA = 21

EXTENSION_8BYTES = 32

#values given by the board to the sensors
BUTTON_DOWN_MASK = 8
TOP_RIGHT = 0
BOTTOM_RIGHT = 1
TOP_LEFT = 2
BOTTOM_LEFT = 3

#name to search for when discovering devices
TARGET_NAME_bdaddr = "Nintendo RVL-WBC-01"
port1 = 0x11
port2 = 0x15

class WiiBoardOperator:
	def __init__(self):
	#values 
		self.rpi_socket = None #for receiving data from board
		self.wii_cl_socket = None #for sending/control data to the board
		self.address = None
	#set LED to false for now
		self.LED = False; 
		try:
			self.rpi_socket = bluetooth.BluetoothSocket(bluetooth.L2CAP)
			self.wii_cl_socket = bluetooth.BluetoothSocket(bluetooth.L2CAP)
		except ValueError:
			raise Exception("ERROR: bluetoothsocket failed. Check bluetooth and try again")

	def connect(self):
		print("using address to connect to board...")
		#the rpi should continue looking for bluetooth connection, hence the try - except statement
		try:
			self.rpi_socket.connect((self.address, port1))
			self.wii_cl_socket.connect((self.address, port2))
		except:
			pass
	#formats data to send to the wiiboard from the rpi 
	def send(self):
		pass
	
	def find_board_address(self):
		print("Sync board: hold red button on the wii balance board")
		nearby_devices = bluetooth.discover_devices(duration = 5, lookup_names = True)
		#look_names is true, so list will be of tuples with (address, name)
		print("Searching...")
		for device in nearby_devices:
			if device[1] == TARGET_NAME_bdaddr:
				self.address = device[0]
				print("found")
			#if wiiboard is not found by rpi
		if address is None:
			print("The board wasn't found. Please try syncing again")
			#check if no devices are found
		if len(nearby_devices) == 0:
			print("No nearby devices were found. Check the bluetooth on the rpi and board")
			return
		return self.address

def main():
	wiiboard = WiiBoardOperator()
	wiiboard.find_board_address()
	wiiboard.connect()
	while True:
		pass #assuming structure of program will require loop (probable)

#calls main function when script is executed from terminal/ROS
if __name__ == "main":
	main()
