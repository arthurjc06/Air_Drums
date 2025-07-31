# Virtual Drum Kit by Computer Vision
*Welcome to my first computer vision project using python!*

The goal of this project is to simulate a drum kit using computer vision to read the user's movements and reproduce sound or send MIDI signals.

## Features
- **Pose Detection**: Utilizes MediaPipe library to identify and track articulations (wrists, knees, etc).

- **Audio Playback**: Plays 4 different drum sounds (kick, snare, hat and pedal) using Pygame Mixer.

- **Visual Feedback**: Displays pose landmarks on the video.

## Requirements
- **Python 3.12**

- **OpenCV (cv2)**: For video capture and processing

- **MediaPipe (mediapipe)**: For pose detection

- **Pygame (pygame)**: For audio playback

## Setup
Follow these steps to run the project on your machine:

### Library Instalation

Open your terminal or command prompt and run the following:

```pip install opencv-python mediapipe pygame```

### Audio Files
Make sure to have a folder **drums** with the audio files in the same directory as *main.py*. Ensure that the file names correspond to those used in *sound.py*.

### Video
You can use your device's camera or a video file.

```cv2.VideoCapture(0)``` Or other values, if your device has more than one camera

```cv2.VideoCapture(path_to_video.mp4)```

## How to Use
### Run The Script:
Open your terminal or command prompt in the project directory and execute:

```python main.py```

### If video is flipped:
```frame = cv2.flip(frame, 0) # Switch between 0, 1 and -1```

### Sensitivity Adjustment:
Adjust the sensitivity by modifying the threshold values.

```arm_threshold = 0.03 # Higher values require a "stronger" movement```

## How to Improve Performance

### Video Quality
A video with good lighting and high contrast between the user and the background facilitates movement detection!

### Processing
I've created two variables to help with the processing:

```scale = 0.4 # Values less than 1 reduce resolution and increase fluidity```

```process_every_n_frames = 2 # Increasing this value can help with the processing but may prejudice movement detection```

## Next Updates
### MIDI Integration
Implement the functionality to send MIDI signals to a DAW (FL Studio, Ableton, Logic, etc).

### Trigger Areas
Currently, each body part is associated to a specific sound. This makes impossible to add more elements, such as toms and crashes, and to play more complex rhytms, where different limbs may be required to play the same sound (snares and cymbals, for instance).

The solution proposed is to define trigger areas in the video for each drum element. By doing so, when a movement is detected, the sound of the trigged area is played, regardless of the body part that performed the movement.

### Automatic Calibration
Develop a calibration that adjusts the trigger areas based on the user's pose.

### Graphical User Interface (GUI)
Create a simple GUI to adjust sounds, sensitivity, volume, etc.

### More Complex Gesture Detection
Implement recognition of specific gestures and combinations to play different sounds and variations, such as release and velocity.

# Have Fun! XD
