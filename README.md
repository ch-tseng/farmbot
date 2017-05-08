Farmbot<br />
---
### countSprout.py (Count sprout number) <br />
example: <br />
*python countSprout.py -n frames/image_20170507010203.jpg -s frames/image_20170508050203.jpg* 
<br /><br />
-n: path for the image which seeds not sprout yet  <br />
-s: path for the image which seeds sprout <br />
![alt tag](https://github.com/ch-tseng/farmbot/blob/master/detectSprout.png)

### countPlantsArea.py (Count plants area) <br />
example: <br />
*python countPlantsArea.py -g 150 -r 137 -i images/weeds/IMAG2569.jpg* 
<br /><br />
-g: threshold for green plants: 0-255, smaller will detect more green plants (more sensitive) <br />
-h: threshold for red plants: 0-255, smaller will detect more red plants (more sensitive) <br />

if you set *"createImage = False"*  ---> will get a tuple (green-Area, red-Area, overlap-Area)<br />
if you set *"createImage = True"*  ---> will get a tuple and create an image at local <br />
![alt tag](https://github.com/ch-tseng/farmbot/blob/master/output.png)

