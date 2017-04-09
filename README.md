Farmbot===== <br />
---
### countPlantsArea.py (Count plants area) <br />
command execute: <span style="color:orange;">python countPlantsArea.py -g 140 -r 150 -i images/weeds/IMAG2562.jpg</span> <br />
-g: <span style="color:blue;">threshold for green plants: 0~255, smaller will detect more green plants (more sensitive) </span><br />
-h: <span style="color:blue;">threshold for red plants: 0~255, smaller will detect more red plants (more sensitive) </span><br />

   if you set *"createImage = False"*  ---> will only get the value: 0.151119444444 <br />

   if you set *"createImage = True"*  ---> will get the value & plants-area image at local <br />
![alt tag](https://github.com/ch-tseng/farmbot/blob/master/output.png)

