# Fusion360_SteamVR_Json
A Fusion360 add-in for generating SteamVR Tracking JSON files from 3D CAD Data
# Required software
* Autodesk Fusion360
# Installation Instructions:
1) Clone this repository or download .zip and extract to: C:\Users\<your user name>\AppData\Roaming\Autodesk\Autodesk Fusion 360\API\AddIns\
2) If Fusion360 is open, close the software
3) Launch Fusion360
4) A new command should appear in the "Model" Panel under "ADD-INS" called "Generate SteamVR JSON (Triad Semiconductor)"
# Usage Insturctions
This script will generate a steamVR sensor definintion JSON file based on ConstructionPoints and ConstructionAxes that are added to a solid model.

For example, consider the following 3D model for the HTC Vive Tracker:
![Picture of Tracker Model in Fusion360](images/step0.jpg?raw=true "Tracker Model")

If we wanted to generate a JSON file for one sensor location, we would do the following:
1) Select CONSTRUCT>Point at Center of Circle/Sphere/Torus
![Step 1](images/step1.JPG?raw=true "CONSTRUCT>Point at Center of Circle/Sphere/Torus")
2) Select the Sensor Aperture circle where the center point should be placed
![Step 2](images/step2.JPG?raw=true "Select Center Point")
3) A point will appear in the center of the circle (yellow arrow), you will also see a new entry in the heirarchy Browser (green arrow)
![Step 3](images/step3.JPG?raw=true "Center Point Appears")
Note: In this example, the point is called "Point1", this point will correlate to sensor 0 in the json channel map
4) Select CONSTRUCT>Axis Through Cylinder/Cone/Torus
![Step 4](images/step4.JPG?raw=true "CONSTRUCT>Axes Through Cylinder/Cone/Torus")
5) Select the Cone surronding the Sensor Aperture
![Step 5](images/step5.JPG?raw=true "Select Cone")
6) An Axis will appear in the center of the cone (yellow arrow), you will also see a new entry in the heirarchy Browser (green arrow)
![Step 6](images/step6.JPG?raw=true "Axis Appears")
Note: In this example, the axis is called "Axis1", this vector will correlate to sensor 0 in the json channel map
7) The sensor location is now specified by the point in Step 3 and the normal vector is specified by the Axis created in step 6, we may now test this by genearting a JSON file, to do this, select ADD-INS>Generate SteamVR JSON (Triad Semiconductor)
![Step 7](images/step7.JPG?raw=true "Generating JSON")
8) The Script will automatically detect each construction point and axis, match them based on index and generate a JSON file where each pair is mapped to a channel of index-1
![Step 8](images/step8.JPG?raw=true "Viewing JSON")
9) To add more sensors to the JSON file, repeat step 1 through step 6 for each sensor in the channel map
10) After doing this N more times for each sensor, your model may look like this:
![Step 10](images/step10.JPG?raw=true "Additional Sensors Added")
11) If we regenerate the JSON per step 7, the following file is generated:
![Step 11](images/step11.JPG?raw=true "5 Sensor JSON")
12) When you are satisfied with your JSON file, you may File>Save As in your text editor