from moviepy.editor import ColorClip
import base64
import io
import os
from PIL import Image

ONE_PX_PNG = base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+P+/HgAFhAJ/wlseKgAAAABJRU5ErkJggg==')

# Write PNG data to a file
with open("test_image.png", "wb") as png_file:
    png_file.write(ONE_PX_PNG)

# Convert PNG to JPG
img = Image.open("test_image.png")
rgb_img = img.convert('RGB')  # convert image to RGB mode
rgb_img.save("test_image_1.jpg", "JPEG")
rgb_img.save("test_image_2.jpg", "JPEG")

clip = ColorClip((1, 1), col=(0, 0, 0), duration=1)
clip.write_videofile('temp_video.mp4', codec='libx264', fps=24)

with open('temp_video.mp4', 'rb') as f:
    video_bytes = f.read()
video_base64 = base64.b64encode(video_bytes)

print(video_base64.decode('utf-8'))
os.remove('temp_video.mp4')

import zipfile

zip_buffer = io.BytesIO()
with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
    zip_file.write('test_image_1.jpg')
    zip_file.write('test_image_2.jpg')

zip_bytes = zip_buffer.getvalue()
zip_base64 = base64.b64encode(zip_bytes)

print()
print()

print(zip_base64.decode('utf-8'))

input()

# Remove temporary files
os.remove("test_image.png")
os.remove("test_image_1.jpg")
os.remove("test_image_2.jpg")

