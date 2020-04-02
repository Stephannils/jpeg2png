import sys
import os
from PIL import Image

work_dir = sys.argv[1]
new_dir =sys.argv[2]

try:
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
except OSError:
    print('Something went wrong')

try:
    for img in os.listdir(work_dir):
        clean_name = os.path.splitext(img)
        img2edit = Image.open(f'{work_dir}\{img}')
        img2edit.save(f'{new_dir}\{clean_name[0]}.png', 'png')
        print('Image converted')
except ValueError:
    print('No image file found')

print('All done')