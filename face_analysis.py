from deepface import DeepFace

def analyze_face(image_path):
    result = DeepFace.analyze(
        img_path=image_path,
        actions=['emotion', 'age', 'gender'],
        enforce_detection=False
    )
    return result
