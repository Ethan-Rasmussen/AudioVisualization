This solution used a high-speed Arduino microcontroller connected to four 3.3V high-sensitivity digital sound sensors operated by an 
interrupt driven precision timing loop with erroneous input handling. The sensors themselves were unanimously calibrated by plotting 
voltage coming out of the potentiometer for sensitivity in real-time, in parallel... so as to visually observe identical behavior on 
the sensors. From here, the Time Delay of Arrival (TDOA) data was delivered to a Raspberry Pi Model 4 over USB serial in the form of 
4 raw times measured in microseconds. Once retrieved on the RPI, both the raw data collection and source localization was performed. 
The raw input data collected over serial is stored directly into binary files formatted with a user data type. From there an ScKit 
Learn Linear Regression model is trained or 'calibrated' through our GUI python app with user entered X,Y,Z data for test sounds. 
Once calibrated, the system can then show a rotatable and resizable 3d-model depicting the tetrahedral array of sensors and a line 
leaving the array's center heading in the direction of the localized sound source.
![image](https://user-images.githubusercontent.com/113371432/236647279-7e1e62e7-e369-427a-b67e-3f13fde6a88c.png)
![image](https://user-images.githubusercontent.com/113371432/236647646-bcd6aee6-34d5-4ea7-a7dc-d11e2ce248ef.png)


