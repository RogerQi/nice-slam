from PIL import Image
import os
import glob
import cv2

color_map = {
    0: (255, 255, 255),
    1: (255, 0, 0), 
    2: (0, 0, 0), 
}

input_dir = '.'
output_dir = 'new_vis_2'

input_files = glob.glob(os.path.join(input_dir, 'semantic_*.png'))
num_files = len(input_files)

for i in range(num_files):
    input_file = os.path.join(input_dir, f'semantic_{i:05d}.png')
    output_file = os.path.join(output_dir, f'new_semantic_{i:05d}.png')

    image = Image.open(input_file)

    width, height = image.size

    new_image = Image.new('RGB', (width, height))

    for y in range(height):
        for x in range(width):
            integer_value = image.getpixel((x, y))

            color = color_map.get(integer_value, (0, 0, 0))

            new_image.putpixel((x, y), color)

    new_image.save(output_file)

input_dir = 'new_vis_2'
output_file = 'output_video_2.avi'

fps = 30  
width = 640  
height = 480  
video_size = (width, height)


input_files = glob.glob(os.path.join(input_dir, 'new_semantic_*.png'))
num_files = len(input_files)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_writer = cv2.VideoWriter(output_file, fourcc, fps, video_size)

for i in range(num_files):
    input_file = os.path.join(input_dir, f'new_semantic_{i:05d}.png')

    frame = cv2.imread(input_file)

    frame = cv2.resize(frame, video_size)

    video_writer.write(frame)

video_writer.release()
