Farmbot=====
---
### countPlantsArea.py (Count plants area)
command execute: *python countPlantsArea.py -g 140 -r 150 -i images/weeds/IMAG2562.jpg*
-g: threshold for green plants: 0~255, smaller will detect more green plants (more sensitive)
-h: threshold for red plants: 0~255, smaller will detect more red plants (more sensitive)

   if you set *"createImage = False"*  ---> will only get the value: 0.151119444444

   if you set *"createImage = True"*  ---> will get the value & plants-area image at local
![alt tag](https://github.com/ch-tseng/farmbot/blob/master/output.png)

