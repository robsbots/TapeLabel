# Install PySerail

 $ pip install pyserial						# Install PySerial
 $ sudo usermod -a -G dialout $USER 		# Add your user to dialout group
 $ newgrp dialout							# ?
 $ groups									# List your groups. Verify 'dialout' is listed

# Install in Virtual environment

 $ python -m venv serial-project
 $ source serial-project/bin/activate  		# Linux/macOS
// serial-project\Scripts\activate   		# Windows
 $pip install pyserial

# Verify install

 $ python -c "import serial; print(serial.__version__)"
   // Should return version number

# Script to list connected serial devices

import serial.tools.list_ports

for port in serial.tools.list_ports.comports():
    print(f"{port.device}: {port.description}")  
