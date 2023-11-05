from glob import glob
from os import system, path
from time import sleep

def clear(clear):
    system(clear)

def get_files(cls):
    clear(cls)
    for image_path in glob("*.3dst"):
        extract_colors(image_path, clear)
        clear(cls)
        print(f"Current File: '{image_path}'.")

def extract_colors(image_path, cls):
    tmp0 = image_path.replace('.3dst','')
    output_path = f"colors_{tmp0}.txt"

    existing_colors = set()
    
    try:
        with open(output_path, "r") as existing_file:
            existing_colors = {line.strip() for line in existing_file}
    except FileNotFoundError:
        pass
    
    with open(image_path, "rb") as image_file:
        image_file.seek(0x20)
        argb_data = image_file.read()
        
        rgb_hex_values = []
        for i in range(0, len(argb_data), 4):
            b, g, r, _ = argb_data[i:i+4]
            rgb_hex = "#{:02X}{:02X}{:02X}".format(r, g, b)
            
            if rgb_hex not in existing_colors:
                existing_colors.add(rgb_hex)
                rgb_hex_values.append(rgb_hex)
                print(rgb_hex)
                sleep(0.005)
        
        with open(output_path, "a") as output_file:
            for hex_value in rgb_hex_values:
                output_file.write(hex_value + "\n")

win_chk = path.exists("C:\\Windows\\SysWOW64\\drivers")

if win_chk == True:
    cls = "clear"

if win_chk == False:
    cls = "cls"

get_files(cls)