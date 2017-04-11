Farmbot<br />
---
### countPlantsArea.py (Count plants area) <br />
example: <br />
*python countPlantsArea.py -g 150 -r 137 -i images/weeds/IMAG2569.jpg* 
<br /><br />
-g: threshold for green plants: 0-255, smaller will detect more green plants (more sensitive) <br />
-h: threshold for red plants: 0-255, smaller will detect more red plants (more sensitive) <br />

if you set *"createImage = False"*  ---> will get a tuple (green-Area, red-Area, overlap-Area)<br />

if you set *"createImage = True"*  ---> will get a tuple and create an image at local <br />
![alt tag](https://github.com/ch-tseng/farmbot/blob/master/output.png)

