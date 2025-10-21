import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from PIL import Image
import torch
import pandas as pd
import random

# ----------------------------------
# 🎨 Streamlit Page Config
# ----------------------------------
st.set_page_config(page_title="Brand-Aware Caption Generator", layout="centered")
st.title("🛍️ Brand-Aware Image Captioning using Generative AI")
st.markdown("""
Generate **creative marketing captions** for product images using **Generative AI**.  
This demo uses a vision-language model and text generation model to rewrite  
plain product descriptions into brand-styled marketing messages.
""")

# ----------------------------------
# ⚙️ Load Model (cached for speed)
# ----------------------------------
@st.cache_resource
def load_model():
    model_name = "google/flan-t5-base"  # Lightweight and reliable
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return model, tokenizer

model, tokenizer = load_model()
device = "cuda" if torch.cuda.is_available() else "cpu"

# ----------------------------------
# ⚙️ Sidebar Settings
# ----------------------------------
st.sidebar.header("Settings ⚙️")
tone = st.sidebar.selectbox(
    "Select caption tone:",
    ["Trendy", "Formal", "Luxury", "Playful", "Minimalist"]
)
creativity = st.sidebar.slider(
    "Creativity (temperature):", 0.5, 1.5, 0.9, 0.1
)
max_length = st.sidebar.slider(
    "Max caption length:", 20, 80, 45
)

# ----------------------------------
# 📂 Load Sample Dataset
# ----------------------------------
try:
    df = pd.read_csv("styles_sample.csv")
    st.sidebar.success("✅ Sample dataset loaded successfully!")
except FileNotFoundError:
    st.sidebar.error("❌ styles_sample.csv not found. Please add it to your repo.")
    st.stop()

# ----------------------------------
# 🖼️ Image Upload / Sample Selection
# ----------------------------------
uploaded_image = st.file_uploader("Upload a product image", type=["jpg", "jpeg", "png"])

st.markdown("---")
st.subheader("🎯 Or try with a sample product:")

sample_row = random.choice(df.to_dict(orient="records"))
sample_img_path = f"sample_data/{sample_row['image']}"
sample_caption = f"A {sample_row['baseColour']} {sample_row['articleType']} for {sample_row['gender']}"

if st.button("Use a Sample Image"):
    uploaded_image = Image.open(sample_img_path).convert("RGB")
    st.image(uploaded_image, caption=sample_caption, use_column_width=True)
    base_caption = sample_caption
else:
    base_caption = st.text_input("Enter a base caption (optional):", "A red dress for women")

# ----------------------------------
# ✨ Marketing Caption Generation
# ----------------------------------
def generate_marketing_caption(base_caption, tone, temperature, max_len):
    prompt = (
        f"Rewrite this product description in a {tone.lower()} marketing tone "
        f"for a social media post: {base_caption}. Make it short, catchy, and brand-friendly."
    )
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(
        **inputs,
        max_length=max_len,
        do_sample=True,
        temperature=temperature,
        num_beams=5,
        early_stopping=True
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if uploaded_image is not None:
    st.image(uploaded_image, caption="🖼️ Selected Image", use_column_width=True)

    if st.button("🚀 Generate Marketing Caption"):
        with st.spinner("Creating your brand-aware caption..."):
            caption = generate_marketing_caption(base_caption, tone, creativity, max_length)
        st.success("✅ Generated Caption:")
        st.markdown(f"### ✨ {caption}")

st.markdown("---")
st.caption("Developed as a Generative AI Capstone Project | Powered by Streamlit & Hugging Face")
