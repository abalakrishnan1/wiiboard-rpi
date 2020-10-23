# wiiboard-rpi
Wiiboard and rpi bluetooth socket interface

v1.0: Update manual methods
- Added first-time user's "manual"
- Removed prints from findAdress()
- Added a disconnect method to disconnect device

v1.1: Updating stopping procedures for program
- Added try --> except to stop errors or malfunctions
- Added close() to stop the sockets from continuing the send adn recieve processes
- Changed status to become a local variable within wiiboard allowing String instead of booleans
  - Allows for knowing where program stops... --> Connecting, Connected, Disconnecting, Disconnected; rather than simply... --> True (connected), False (disconnected)
