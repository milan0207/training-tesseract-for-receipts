import os
import pathlib
import random
import subprocess

# File and directory setup
training_text_file = 'Receipts.txt'
output_directory = 'data2'
font_directory ='fonts'  # Directory where the font is located
font_name = 'Hypermarket'

# Read and clean lines from the training text file
lines = []
with open(training_text_file, 'r', encoding='utf-8') as input_file:
    for line in input_file.readlines():
        lines.append(line.strip())

# Create output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.mkdir(output_directory)

# Shuffle and limit the number of lines
random.shuffle(lines)

count = 50
lines = lines[:count]

# Loop through lines and create corresponding .gt.txt and images
line_count = 0
for line in lines:
    # Create the training text file name
    training_text_file_name = pathlib.Path(training_text_file).stem
    line_training_text = os.path.join(output_directory, f'ron_{line_count}.gt.txt')
    
    # Write the line to the .gt.txt file
    with open(line_training_text, 'w', encoding='utf-8') as output_file:
        output_file.writelines([line])
    
    # Base name for the output image file
    file_base_name = f'ron_{line_count}'
    
    # Run the text2image command using subprocess
    result = subprocess.run([
        'text2image',
        f'--fonts_dir={font_directory}',   # Directory of the fonts
        f'--font={font_name}',             # Specific font name to use
        f'--text={line_training_text}',
        f'--outputbase={output_directory}/{file_base_name}',
        '--max_pages=1',
        '--strip_unrenderable_words',
        '--leading=32',
        '--xsize=3600',
        '--ysize=480',
        '--char_spacing=1.0',
        '--exposure=0',
        '--unicharset_file=eng.unicharambigs'
    ], capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error running text2image: {result.stderr}")
    
    line_count += 1

#openCV image augmentation rotation gauss zaj