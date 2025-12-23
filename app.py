import streamlit as st
from face_analysis import analyze_face
from face_draw import draw_faces

st.title("DeepFace AI Tool")

img = st.file_uploader("Upload Image")

if img:
    with open("temp.jpg", "wb") as f:
        f.write(img.getbuffer())

    analysis = analyze_face("temp.jpg")
    output_img = draw_faces("temp.jpg")

    st.image(output_img)
    st.json(analysis)
