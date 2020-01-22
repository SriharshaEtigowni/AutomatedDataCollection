# AutomatedDataCollection
Lulzbot Taz 6 printer - Sending Gcode through serial communication and collecting the images of extruder at every point on the print bed


# Moving the extruder throughout the print bed
Run ControlPrinter.py - This controls the extruder movement in the increments of 1mm in X and Y direction and 0.1mm in Z direction. This program will move in z axis from 1.3mm to 3mm.
To change the height change the line number 69 in sendandcapture__ function.


# Move the extruder and Capture image at every point
run AutoCapture.py
