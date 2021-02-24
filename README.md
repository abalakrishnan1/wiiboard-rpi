# wiiboard-rpi
Wiiboard and rpi bluetooth socket interface

# Version Info
- v1.x: Manual/control instructions
- v2.x: Send/receive data to/from RPI and Wii Board

# v1.x
v1.0: Update manual methods
- Added first-time user's "manual"
- Removed prints from findAdress()
- Added a disconnect method to disconnect device

v1.1: Updating stopping procedures for program
- Added try --> except to stop errors or malfunctions
- Added close() to stop the sockets from continuing the send adn recieve processes
- Changed status to become a local variable within wiiboard allowing String instead of booleans
  - Allows for knowing where program stops... --> Connecting, Connected, Disconnecting, Disconnected; rather than simply... --> True (connected), False (disconnected)

# v2.x
v2.0: Started on send() method
- Addded and finished send() method regarding only "hex" values

v2.1: Finished send() method translation
- Decoded "hex" array with placeholder into String array for RPI
- hexArray.decode()/stringArray.encode() belong to bluetooth module

v2.2: Fixed errors
-  5 errors fixed
-  0 errors remain
