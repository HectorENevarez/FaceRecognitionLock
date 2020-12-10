# Face Recognition Lock
Guadiana - Mechanical Design
Matt - Client Side
Hector - Server Side

we'll each edit our readme in our assigned file. From there we will have a general overview linking everything together on this main readme. Don't modify this readme until all of the assigned parts are done. Let me know if you have questions.
- Hector

# MECHANICAL DESIGN  

# Hardware

- Raspberry Pi 3
- Sliding lock 
- Wood
- Jumper Wires
- Pi Camera
- Uxcell 300RPM 6V 0.45A High Torque Mini Electric DC Geared Motor
- 9V battery holder with switch
- L298N Motor driver controller dual H-bridge
- Machine screw & nut 
- Splicer/Reducer connector
- Gorilla Tape
- Epoxy

# 
# Design

The purpose of the design was to get the sliding lock to lock/unlock succesfully without any mechanical failures. This includes: no failures with the lock, the raspberry pi, the motor driver, and the dc motor. 

- The Raspberry Pi 3B GPIO map was used alongside the layout for the L298N Motor Driver to hook everything up. The 9V battery holder was connected to the following power pins: GND & 12V on the L298N motor driver. The DC Motor was connected to the Motor A side with jumper wires of the motor driver, and on the Raspberry Pi GPIOs 23-25 were used. Pin #6 on the Raspberry Pi was used for ground. 

- In order to have the DC motor interact with the lock the DC motor would have to be placed a certain way where the rotation would move the lock from sided to side smoothly. The best design option to go with was to use a machine screw and nut accompanied by a clamp/connector. The nut would have to be attached to the small handle of the sliding lock and the best way was to attach it to the top of the handle. That being said, the machine screw would have to go through the nut in order to have the lock slide from its lock state to unlocked state and vice-versa.

- The sliding lock was screwed in place on a small wood board while the DC motor was taped (with Gorilla Tape) to stacked wood chips that were approximately equal in height to the handle of the sliding lock. These wood chips were glued to the small wood board by using epoxy. 
 
- To continue, a clamp/connector with a tightening screw would have to be attached to the end of the DC motor while the other end of the clamp/connector would tighten down the machine screw that goes through the nut. This would enable the machine screw to rotate while the nut stays locked in position to the handle of the sliding locked allowing the nut to move along the screw; hence locking and unlocking the sliding lock. 

- The PiCamera was then hooked up and can be placed as desired by the user with all of it's functionality intact. 

#
# Testing

- The mechanical design's rigidity was tested by tweaking the script that rotates the DC motor. This enabled us to see how the everything worked together by making rotation times longer or shorter and by applying some force to see if anything would break/move out of position. These script tweaks also allowed us to see how efficient and consistent the system worked. 
