import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from PIL import Image
import torch
import pandas as pd
import random

# -----------------------------
# App Setup
# -----------------------------
st.set_page_config(page_title="Brand-Aware Caption Generator", layout="centered")
st.title("🛍️ Brand-Aware Image Captioning using Generative AI")
st.markdown("""
Generate **marketing-style captions** for product images using Generative AI.  
Built with **FLAN-T5** and designed for **brand-aware social media captions**.
""")

# -----------------------------
# Load Model (cached)
# -----------------------------
@st.cache_resource
def load_model():
    model_name = "google/flan-t5-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return model, tokenizer

model, tokenizer = load_model()
device = "cuda" if torch.cuda.is_available() else "cpu"

# -----------------------------
# Sidebar Controls
# -----------------------------
st.sidebar.header("⚙️ Settings")
tone = st.sidebar.selectbox("Choose caption tone:", ["Trendy", "Formal", "Luxury", "Playful", "Minimalist"])
creativity = st.sidebar.slider("Creativity (temperature)", 0.5, 1.5, 0.9, 0.1)

# -----------------------------
# Data Upload Section
# -----------------------------
uploaded_image = st.file_uploader("Upload a fashion product image", type=["jpg", "jpeg", "png"])

# Optionally use sample dataset
st.markdown("---")
st.subheader("Or try with a sample product 👇")

df = pd.read_csv("styles_sample.csv")
sample_row = random.choice(df.to_dict(orient="records"))
sample_img_path = f"sample_data/{sample_row['image']}"
sample_caption = f"A {sample_row['baseColour']} {sample_row['articleType']} for {sample_row['gender']}"

if st.button("🎯 Use a sample image"):
    uploaded_image = Image.open(sample_img_path).convert("RGB")
    st.image(uploaded_image, caption=sample_caption, use_column_width=True)
    base_caption = sample_caption
else:
    base_caption = st.text_input("Enter a base description (optional):", "A red dress for women")

# -----------------------------
# Caption Generation
# -----------------------------
def generate_caption(base_caption, tone, temperature):
    prompt = f"Write a {tone.lower()} marketing caption for social media about this product: {base_caption}"
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(**inputs, max_length=50, do_sample=True, temperature=temperature, num_beams=5)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    if st.button("✨ Generate Marketing Caption"):
        with st.spinner("Generating creative caption..."):
            marketing_caption = generate_caption(base_caption, tone, creativity)
        st.success("✅ Generated Caption:")
        st.write(f"**{marketing_caption}**")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit and Hugging Face Transformers.")
