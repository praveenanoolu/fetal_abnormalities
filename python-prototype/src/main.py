import streamlit as st
from PIL import Image

def detect_abnormality(image):
    # Placeholder for actual AI model inference
    # Replace this with your model's prediction logic
    return "No abnormality detected (demo result)"

def main():
    st.set_page_config(page_title="Fetal Abnormalities Agent")
    st.title("Fetal Abnormalities Agent")
    st.write("Upload a fetal ultrasound image to detect abnormalities.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write("Analyzing...")
        result = detect_abnormality(image)
        st.success(f"Result: {result}")

if __name__ == "__main__":
    main()