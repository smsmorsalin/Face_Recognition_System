import cv2

while True:
    video_cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    ret, video_data = video_cap.read()

    gray = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow("Video_Live", video_data)

    if cv2.waitKey(2) == ord('x'):
        break

video_cap.release()
