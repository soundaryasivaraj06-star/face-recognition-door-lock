import cv2
import datetime
import os
import pandas as pd
import winsound

# ---------- SETTINGS ----------
THRESHOLD = 60
OWNER_NAME = "Soundarya"
# ------------------------------

# ---------- LOG FILE ----------
LOG_FILE = "entry_log.csv"

if not os.path.exists(LOG_FILE):
    df = pd.DataFrame(columns=["Name", "Time"])
    df.to_csv(LOG_FILE, index=False)

# ---------- LOAD MODEL ----------
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face_model.yml")

faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# ---------- CAMERA ----------
cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

# Tracks whether the owner is currently in front of the camera
person_present = False

print("🔐 Face Recognition System Started... Press 'Q' to exit")

while True:

    ret, frame = cam.read()

    if not ret:
        print("❌ Failed to capture frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5
    )

    # Indicates whether the owner was detected in this frame
    recognized_this_frame = False

    for (x, y, w, h) in faces:

        id_, conf = recognizer.predict(gray[y:y+h, x:x+w])

        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        # ---------- KNOWN PERSON ----------
        if conf < THRESHOLD:

            recognized_this_frame = True

            text = f"{OWNER_NAME} ({int(conf)})"
            color = (0, 255, 0)

            # Log only once when the person first appears
            if not person_present:

                print(f"✅ Access Granted to {OWNER_NAME}")

                # Save entry log
                df = pd.read_csv(LOG_FILE)
                df.loc[len(df)] = [OWNER_NAME, current_time]
                df.to_csv(LOG_FILE, index=False)

                print(f"📝 Entry logged at {current_time}")

                person_present = True

            cv2.putText(
                frame,
                "ACCESS GRANTED",
                (20, 40),
                font,
                1,
                (0, 255, 0),
                2
            )

        # ---------- UNKNOWN PERSON ----------
        else:

            text = f"UNKNOWN ({int(conf)})"
            color = (0, 0, 255)

            img_name = f"unknown_{current_time.replace(':','-')}.jpg"
            cv2.imwrite(img_name, frame)

            winsound.Beep(1000, 800)

            cv2.putText(
                frame,
                "ACCESS DENIED",
                (20, 40),
                font,
                1,
                (0, 0, 255),
                2
            )

        # Draw rectangle around detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

        # Display name
        cv2.putText(
            frame,
            text,
            (x, y - 10),
            font,
            0.8,
            color,
            2
        )

    # Reset when the known person leaves the camera
    if not recognized_this_frame:
        person_present = False

    cv2.imshow("Face Recognition Door Lock System", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()