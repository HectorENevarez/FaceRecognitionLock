# Client Side 

## Dependencies
To run the client side scripts the following requirements are needed:
* Python 3.3+
* RPIO.GPIO
* picamera

## The Client is composed of 3 main scripts, each ran on the Raspberry Pi:
1. CS530_Project.py
2. snap.py
3. client_real.py

### CS530_Project.py
This is the main script for the client side. It contains the methods to manipulate the lock through the GPIO pins on the Pi. 
It also contains the "main" functionality for our project:
* The lock starts in a locked state until a user prompts for unlock
* Then, a photo of the user's face is taken and saved
* Next, the client - server connection is initiated and the photo is sent to the server, run through the facial recognition algorithm, and the result is sent back and returned to a variable
* Then, if algorithm returns a match, the lock is unlocked through the GPIO methods, otherwise, the loop starts over
* Once the lock is unlocked, the program waits for user input to lock, then calls the respective GPIO method to spin the lock back
This loop continues until exited manually. 

### snap.py
This is the script for taking and saving a photo of the user attempting to unlock. 
It identifies the piCam, snaps a singular photo, and saves it to our specified directory

### client_real.py
This is the script for our client side of the client-server connection.
The script proceeds as follows:
* First, the host IP and port are identified and saved 
* Then, a client socket is initialized and connected
* Next, the snapped image of the user is read and sent to the server
* After the server finishes the facial recognition, the result is received on the client side, decrypted, and returned to a variable for use in the main script
