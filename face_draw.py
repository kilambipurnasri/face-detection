import cv2
from deepface import DeepFace

def draw_faces(image_path):
    img = cv2.imread(image_path)
    faces = DeepFace.extract_faces(img_path=image_path, enforce_detection=False)

    for face in faces:
        x, y, w, h = face["facial_area"].values()
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

    output_path = "output.jpg"
    cv2.imwrite(output_path, img)
    return output_path
