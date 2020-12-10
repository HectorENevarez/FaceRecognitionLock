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

# 
# Design

The purpose of the design was to get the sliding lock to lock/unlock succesfully without any mechanical failures. This includes: no failures with the lock, the raspberry pi, the picamera, the motor driver, and the dc motor. 

- The Raspberry Pi 3B GPIO map was used along side the layout for the L298N Motor Driver to hook everything up. The 9V battery holder was connected to the following power pins: GND & 12V. The DC Motor was connected to the Motor A side with jumper wires, and on the Raspberry Pi GPIOs 23-25 were used. Pin #6 on the Raspberry Pi was used for ground. 

- In order to have the DC motor interact with the lockt he DC motor would have to be placed a certain way where the rotation would move the lock from sided to side without compromising time and speed. The best design option was to go with as machine screw and nut accompanied by a clamp/connector. The nut would have to be attached somehow to the small handle of the slidin lock and the best way was to attach it to thew top of the handle. With that being said, the machine screw would have to obviously go through the nut in order to have the lock slide from its lock state to unlocked state and vice-versa.
 
- To continue, a clamp/connector with a tightening screw would have to be attached to the end of the DC motor while the other end of the clamp/connector woudl tighten down the machine screw that goes through the nut. This would enable the machine screw to rotate while the nut stays locked in position to the handle of the sliding locked allowing the nut to move along the screw; hence locking and unlocking the sliding lock. 
