import subprocess
import os

# Folder where the .tif and .gt.txt files are located
input_folder = "data"

# Range of file numbers
start_index = 3100
end_index = 6198

def add_spaces_to_box(box_file, gt_file):
    """
    Adds spaces to the .box file based on the ground truth text.
    """
    try:
        with open(box_file, "r", encoding="utf-8") as box_f:
            box_lines = box_f.readlines()

        with open(gt_file, "r", encoding="utf-8") as gt_f:
            gt_text = gt_f.read().strip()

        new_box_lines = []
        gt_index = 0

        for char in gt_text:
            if char == " ":
                # If the character is a space, add a placeholder box
                x1, y1, x2, y2, page = 0, 0, 0, 0, 0
                new_box_lines.append(f"  {x1} {y1} {x2} {y2} {page}\n")
            else:
                # Add the next box line from the original file
                new_box_lines.append(box_lines[gt_index])
                gt_index += 1

        with open(box_file, "w", encoding="utf-8") as box_f:
            box_f.writelines(new_box_lines)

        print(f"Spaces added to {box_file}")
    except Exception as e:
        print(f"Error processing {box_file}: {e}")

# Loop through the range and run the Tesseract command
for index in range(start_index, end_index + 1):
    tif_file = f"{input_folder}/ron_{index}.tif"
    gt_file = f"{input_folder}/ron_{index}.gt.txt"
    output_base = f"{input_folder}/ron_{index}"
    box_file = f"{output_base}.box"

    try:
        # Run Tesseract with the makebox option
        command = [
            "tesseract",
            tif_file,
            output_base,
            "--psm", "3",
            "batch.nochop", "makebox"
        ]
        subprocess.run(command, check=True)
        print(f"Successfully processed {tif_file} to {box_file}")

        # Add spaces to the box file
        if os.path.exists(gt_file):
            add_spaces_to_box(box_file, gt_file)
        else:
            print(f"Ground truth file not found: {gt_file}")

    except subprocess.CalledProcessError as e:
        print(f"Error processing {tif_file}: {e}")
    except FileNotFoundError:
        print(f"File not found: {tif_file}")
