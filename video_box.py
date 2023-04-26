import cv2
import subprocess

# Load the input video
input_file = "input_video.mp4"
cap = cv2.VideoCapture(input_file)

# Set up the output video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output_file = "output_video.mp4"
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Set up the human detection model
human_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

# Loop through each frame of the input video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect humans in the frame
    humans = human_classifier.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw a thin outline around each human
    for (x, y, w, h) in humans:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Write the modified frame to the output video
    out.write(frame)

# Release the input and output video
cap.release()
out.release()

# Use FFmpeg to compress the output video
subprocess.call(["ffmpeg", "-i", output_file, "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-c:a", "aac", "-b:a", "128k", "-ac", "2", "compressed_video.mp4"])
