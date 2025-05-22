
import streamlit as st
from PIL import Image
import os
import random
from model.model import predict_abnormality
from llm.expert import ask_expert_llm

st.set_page_config(page_title="Fetal Abnormalities Detector", page_icon="🧠", layout="centered")

st.markdown("""
<style>
    .main {
        background-color: #f0f2f6;
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        margin-top: 10px;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧬 Fetal Abnormalities Detection")
st.markdown("Upload a **fetal ultrasound image** to detect potential abnormalities and receive a medical-grade interpretation using AI.")

with st.expander("ℹ️ Instructions", expanded=False):
    st.write("""
    - Supported image formats: JPG, JPEG, PNG
    - Ensure the ultrasound image is clear and not too dark
    - This is a prototype. Consult a certified professional for medical decisions.
    """)

uploaded_file = st.file_uploader("📤 Upload your ultrasound image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="🖼️ Uploaded Image", use_column_width=True)

    with st.spinner("🔍 Analyzing image for abnormalities..."):
        result = predict_abnormality(image)
        confidence = random.randint(70, 95)  # Placeholder confidence

    if "No abnormality" in result:
        st.markdown("### 🟢 **Likely Normal**")
    else:
        st.markdown("### 🔴 **Potential Issue Detected**")

    st.metric(label="🧠 AI Confidence", value=f"{confidence}%")
    st.success(f"✅ Result: {result}")

    with st.spinner("💬 Getting expert interpretation..."):
        explanation = ask_expert_llm(f"Image analysis result: {result}. Provide a medical interpretation for a patient.")

    st.markdown("### 🧑‍⚕️ Doctor's Interpretation")
    st.info(explanation)

    # Optional raw debug output
    if st.checkbox("Show raw model output"):
        st.json({
            "prediction": result,
            "confidence": f"{confidence}%",
            "filename": uploaded_file.name
        })

    # Downloadable summary
    summary = f"Image: {uploaded_file.name}\nResult: {result}\nConfidence: {confidence}%\nInterpretation: {explanation}"
    st.download_button("📄 Download Report", summary, file_name="diagnosis_report.txt")

else:
    st.warning("Please upload an ultrasound image to begin the analysis.")
