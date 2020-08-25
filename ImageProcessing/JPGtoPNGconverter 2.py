# 1. grab first and second argument
# 2. check if the new folder exists, if not create a new one
# 3. loop through the jpg
# 4. convert image to png
# 5. save them to new folder

import sys
import os
from PIL import Image

folder = sys.argv[1]
new_folder = sys.argv[2]

if not os.path.exists(new_folder):
    os.makedirs(new_folder)

for file in os.listdir(folder):
    img = Image.open(f'{folder}{file}')
    clean_name = os.path.splitext(file)[0]
    img.save(f'{new_folder}{clean_name}.png', 'png')
    print('all done!')
