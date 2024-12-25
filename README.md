# flsun-prime-line-fix
Flsun Super Racer prime line outside of the print bed - OrcaSlicer

[issue:](https://github.com/SoftFever/OrcaSlicer/issues/5583)

* OrcaSlicer
* Flsun Super Racer
* Prime line outside of print bed

### Post processing python script to fix the issue

<br>

**gcode from orca slicer**
<p align="left">
  <img width="400" src="https://github.com/Krosko/flsun-prime-line-fix/blob/main/images/gcode_before.png">
</p>

**post processed gcode with this script**
<p align="left">
  <img width="400" src="https://github.com/Krosko/flsun-prime-line-fix/blob/main/images/gcode_after.png">
</p>

<br>

### Apply

1. Download the script from the github
2. Slice your model using OrcaSlicer and save the gcode
3. Open the Terminal
4. ```cd``` to download location of the script
5. Run the script locally from the terminal ```python3 post_process.py -file {path/to/file/filename}.gcode```
