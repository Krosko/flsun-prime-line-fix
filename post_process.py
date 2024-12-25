import argparse

color_green = "\033[0;32m"
color_red = "\033[0;31m"  
color_reset = "\033[0m" 

def modify_content_between_strings(filename, string1, string2, new_content):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Find the index of the lines containing string1 and string2
        start_index = None
        end_index = None

        for i, line in enumerate(lines):
            if string1 in line and start_index is None:
                start_index = i
            if string2 in line and start_index is not None:
                end_index = i
                break

        # If both string1 and string2 are found
        if start_index is not None and end_index is not None:
            # Capture the lines being replaced
            replaced_lines = lines[start_index + 1:end_index]
            num_replaced_lines = len(replaced_lines)

            # Replace content between string1 and string2 with new content
            updated_lines = (
                lines[:start_index + 1]  # Keep everything up to and including string1
                + [new_content + '\n']  # Add the new content
                + lines[end_index:]  # Keep everything from string2 onward
            )

            # Write the updated lines back to the file
            with open(filename, 'w') as file:
                file.writelines(updated_lines)

            # Output details
            print(color_green + "File updated successfully." + color_reset)
            print(f"Number of lines replaced: {num_replaced_lines}")
            print("Replaced lines:")
            print("---")
            print("".join(replaced_lines))
        else:
            print(color_red + f"Could not find both '{string1}' and '{string2}' in the file." + color_reset)

    except Exception as e:
        print(color_red + f"An error occurred: {e}" + color_reset)

parser = argparse.ArgumentParser()
parser.add_argument("-file", "--filename", dest="filename", default="file.gcode", help="Name of the file")
args = parser.parse_args()
filename = args.filename

string1 = '; Prime line routine'
string2 = 'Display: Printing started...'
new_content = """M117 Printing prime line
;M900 K0; Disable Linear Advance (Marlin) for prime line
G92 E0.0; reset extrusion distance
G1 Z150
G1 X-130 Y0 Z0.4 F3000
G92 E0
G3 X0 Y-130 I130 Z0.3 E40 F2700
G92 E0.0 ; reset extrusion distance
; Final print adjustments
M117 Preparing to print
;M82 ; extruder absolute mode
M221 S{if layer_height<0.075}100{else}95{endif}
M300 S40 P10 ; chirp"""

modify_content_between_strings(filename, string1, string2, new_content)

