# Face Recognition System

A small, easy-to-run face detection demo using OpenCV's Haar cascades. Captures live video from your webcam and draws rectangles around detected faces.

## Features
- Real-time face detection from webcam
- Uses OpenCV Haar cascade (no external ML model required)
- Minimal, easy-to-read code for learning and prototyping

## Requirements
- Python 3.7+
- OpenCV for Python

Install with pip:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate     # Windows (PowerShell)
pip install opencv-python
```

If you prefer a requirements file, create `requirements.txt` with:

```
opencv-python
```

## Usage
1. Ensure your webcam is connected and free to use.
2. Run the detector:

```bash
python Face_detector.py
```

3. A window named "Video_Live" will open and show the camera feed. Detected faces are highlighted with blue rectangles.
4. Press the `x` key in the window to exit the program.

## How it works
The script uses OpenCV's `CascadeClassifier` with the `haarcascade_frontalface_default.xml` model included in OpenCV. Frames are converted to grayscale and passed to `detectMultiScale` to locate faces, then rectangles are drawn on the color frame.

## Project structure

- `Face_detector.py` — main demo script that opens webcam and detects faces
- `README.md` — this file

## Contributing
Feel free to open issues or PRs for improvements. Suggestions:
- Add a requirements file or packaging
- Add support for video file input or screenshots
- Swap Haar cascades for modern deep-learning face detectors

## License
This project is provided as-is. Add a license file if you want to set terms.

## Contact
Open an issue or contact the repository owner for questions or help.
