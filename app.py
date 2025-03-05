import streamlit as st
import cv2
import numpy as np
from deepface import DeepFace

st.title("Face Detection & Recognition System")
st.write("Upload an image to recognize faces.")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    try:
        result = DeepFace.find(img_path=image, db_path="faces_db", enforce_detection=False)
        if len(result) > 0:
            name = result[0]["identity"][0].split("/")[-1].split(".")[0]
            st.success(f"Recognized: {name}")
        else:
            st.error("No Match Found!")
    except:
        st.error("Error in recognition!")