# Server Side
### Dependencies
To run the server side scripts the following requirements are needed:
- Python 3.3+
- [face recognition 1.3](https://pypi.org/project/face-recognition/)
- OpenCV

### The server is composed of 2 main scripts and 1 directory
Files:
1. server.py
2. face_detection_small.py

Directory:
1. faces

### server.py
This is the main server side script. Running this will allow for server-client communication to be established. The main goal of this file is to:
1. Establish a connection with the client
2. Recieve an image
3. Convert the image from a raw file to a JPG
4. Call the face recognition script
5. Return the results

The connection between the client and server is achieved through python sockets. The server will wait until it binds to a client and then go through the process mentioned above

### face_detection_small.py
This script will automatically be called in server.py. The goal of this script is to identify whether an image of a person is registered in the database or not. the script pulls images from the registered users, located in the faces directory, and encodes the images. encoded images are then compared to an encoded version of the given image. If the module, face-recognition, detects that the face is recognized it will return that information to server.py, if not it will return "Unknown."

### faces
This directory serves as a database of images of registered users. A registered users must have submitted a couple images of themselves that clearly shows their face. There is not limit as to how many images of one user can be uploaded to the directory, however the run time might take longer if too many images are added. We recommended have 2-3 images per registered user with a maximum of 5 users.

### The server side components
The server can be ran on any system that is connected to the same wifi as he client side. The server.py file should be ran before running any other parts of the software. Here is how the server interaction with the client should proceed.
1. Server recieves image from client
2. Server converts raw image into JPG in order to process
3. The image is passed through the face recognition software located in face_detection_small.py automatically
4. If the picture depicts a registered user that information will be passed to the client
