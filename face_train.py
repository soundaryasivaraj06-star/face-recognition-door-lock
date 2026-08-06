import cv2
import os
import numpy as np

dataset_path = "dataset"
faces = []
labels = []
label_map = {}
label_id = 0

for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)
    if not os.path.isdir(person_path):
        continue

    label_map[label_id] = person

    for image_name in os.listdir(person_path):
        img_path = os.path.join(person_path, image_name)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue

        faces.append(img)
        labels.append(label_id)

    label_id += 1

if len(faces) == 0:
    print("No face images found. Training skipped.")
else:
    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(faces, np.array(labels))
    model.save("face_model.yml")
    print("Training complete. Model saved.")
