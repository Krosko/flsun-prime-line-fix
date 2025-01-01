# **Flsun Super Racer Prime Line Fix**  
Fix the issue of the prime line being generated outside of the print bed in OrcaSlicer when using the Flsun Super Racer.

---

## **Overview**  
When slicing with OrcaSlicer for the Flsun Super Racer, the default G-code configuration may result in a prime line placed outside the printable area. This script provides a post-processing solution to adjust the prime line's location within the valid print bed, ensuring smooth operation.

This guide is specifically designed for **macOS users** leveraging the macOS Terminal to run the script.

---

## **Before and After**
### **G-code Before Processing**
![G-code Before](https://github.com/Krosko/flsun-prime-line-fix/blob/main/images/gcode_before.png)

### **G-code After Processing**
![G-code After](https://github.com/Krosko/flsun-prime-line-fix/blob/main/images/gcode_after.png)

---

## **Background changes made by the Script in G-code**
<p align="left">
  <img width="400" src="https://github.com/Krosko/flsun-prime-line-fix/blob/main/images/diff.png">
</p>

---

## **Features**
- Automatically detects and replaces the incorrect prime line routine in the G-code.  
- Inserts a new prime line routine tailored for the Flsun Super Racer.  
- Supports easy customization of the replacement G-code.  
- Provides detailed feedback in the terminal, including the number of lines replaced.  

---

## **Requirements**
1. **macOS** or other os with Terminal access.
2. Python 3.x installed.  
   *You can install Python 3 via [Homebrew](https://brew.sh/):*  
   `brew install python3`
3. OrcaSlicer installed and configured for the Flsun Super Racer.  

---

## **Installation & Usage**

> Steps for Mac, commands may be slightly different on other operating systems

### **Step 1: Clone or Download the Script**
Download the script directly from this repository:  
`git clone https://github.com/Krosko/flsun-prime-line-fix.git`  
`cd flsun-prime-line-fix`

Alternatively, download the `post_process.py` file from the repository and save it to a convenient location.

---

### **Step 2: Slice Your Model**
1. Open **OrcaSlicer** and load your 3D model.  
2. Slice the model and save the resulting `.gcode` file to a known location.  

---

### **Step 3: Run the Script in Terminal**

#### Option 1

1. Open **Terminal** on macOS.  
2. Navigate to the folder containing the script:  
   `cd /path/to/folder/containing/script`
3. Run the script with the following command, replacing `/path/to/file/filename.gcode` with the full path to your `.gcode` file:  
   1. `python3 post_process.py -f /path/to/file/filename.gcode`
   2. `-t /path/to/target/location/filename.gcode` can be added behind the command to define the target location of the processed `.gcode` file  
4. If successful, you will see a message like:  
   `File updated successfully.`  
   `Number of lines replaced: X`

Run `python3 post_process.py --help` for informations about the `-f` and `-t` flags 

#### Option 1

1. Add the path to python and the executable script to the **Post-processing Scripts** section of the OrcaSlicer

---

### **Step 4: Print Your Model**
1. Transfer the processed `.gcode` file to your printer via SD card or another method.  
2. Start your print and verify that the prime line is now correctly placed within the print bed.  

---

## **Customization**
If you'd like to modify the new prime line routine, you can edit the `new_content` variable in the `post_process.py` script. Ensure the G-code commands are compatible with the Flsun Super Racer and OrcaSlicer.

---

## **Contributing**
We welcome contributions to improve the script or documentation! Feel free to open an issue or submit a pull request.

---

### **Support**
If you encounter any issues or have questions, please open an issue in this repository.  

Happy Printing! 🎉  

