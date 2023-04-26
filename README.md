# video_target_marker
uses OpenCV and FFmpeg to spot humanoid figures in moving video, draw an outline around them, and output a new movie file

The code first loads the input video and sets up the output video with the same properties (fourcc, fps, width, height). It then sets up the human detection model using the Haar cascade classifier for full body detection.

In the main loop, each frame is converted to grayscale, and humans are detected using the detectMultiScale() function of the human_classifier object. A thin outline is drawn around each human using the rectangle() function of OpenCV. The modified frame is then written to the output video using the write() function of the out object.

After processing all the frames, the input and output videos are released. Finally, FFmpeg is used to compress the output video using the H.264 video codec and AAC audio codec. The compressed video is saved as "compressed_video.mp4".
