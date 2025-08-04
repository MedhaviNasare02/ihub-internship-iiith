📌 **PART (A): IMAGE SEGMENTATION FROM A LOCAL FOLDER**

**1. Image Collection**
   
A set of custom images was downloaded from Google and saved in a local directory named images.

**2. Segmentation using YOLOv8**
   
A Python script was developed to perform segmentation using the YOLOv8 segmentation model (yolov8l-seg.pt).
The script reads all images from the images folder, applies the segmentation model, and saves the output in a new directory called segmented_custom_output.

📌 **PART (B): VIDEO SEGMENTATION WORKFLOW**

**1. Video Download**

A short video snippet was downloaded from YouTube (ensuring it is appropriate for the group and doesn’t hurt any sentiments).
Video link(https://youtu.be/Xbz9XaZxRBI?si=E5_MXPi-m3ZZe5hV)

**2. Frame Extraction**

FFmpeg was used to extract frames from the video at a rate of 10 frames per second.
The extracted frames were saved in a directory named extracted_frames_10fps using the following command:

ffmpeg -i video.mp4 -vf "fps=10" extracted_frames_10fps/frame_%03d.jpg

**3. Frame Segmentation**

A separate Python script named segment_frames_10fps.py was written to segment all frames extracted into the extracted_frames_10fps folder.
This script applies YOLOv8 segmentation to each frame and saves the outputs in the segmented_frames_10fps directory.

**4. Video Reconstruction**

After segmentation, the processed frames were reassembled into a video using FFmpeg at 10 frames per second.
The command used:

ffmpeg -framerate 10 -i segmented_frames_10fps/seg_frame_%03d.jpg -c:v libx264 -pix_fmt yuv42

