import streamlit as st
import torch
from PIL import Image
from transformers import (
    BlipProcessor,
    BlipForConditionalGeneration,
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)
import os

# ----------------------------
# 🧠 App Configuration
# ----------------------------
st.set_page_config(
    page_title="Brand-Aware Image Captioning",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Brand-Aware Image Captioning for Marketing Applications")
st.markdown(
    """
    Generate **brand-style marketing captions** from product images using Generative AI.  
    Built with **BLIP** (for visual captioning) and **FLAN-T5** (for creative rewriting).
    """
)

# ----------------------------
# ⚙️ Load Models
# ----------------------------
@st.cache_resource
def load_models():
    # Base caption generator
    blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")

    # Marketing caption generator
    model_name = "google/flan-t5-base"  # ✅ you can switch to "google/flan-t5-large" for richer captions
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    t5_model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    return blip_processor, blip_model, tokenizer, t5_model

with st.spinner("🔄 Loading AI models... Please wait..."):
    blip_processor, blip_model, tokenizer, t5_model = load_models()
device = "cuda" if torch.cuda.is_available() else "cpu"
blip_model.to(device)
t5_model.to(device)

# ----------------------------
# 🖼️ Image Upload
# ----------------------------
uploaded_file = st.file_uploader("📸 Upload a fashion or product image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # ----------------------------
    # 🧩 Step 1: Generate Base Caption (BLIP)
    # ----------------------------
    st.write("### 🔹 Step 1: Base Caption Generation")
    inputs = blip_processor(images=image, return_tensors="pt").to(device)
    with torch.no_grad():
        output = blip_model.generate(**inputs, max_new_tokens=20)
    base_caption = blip_processor.decode(output[0], skip_special_tokens=True)
    st.success(f"📝 **Base Caption:** {base_caption}")

    # ----------------------------
    # ✨ Step 2: Generate Marketing Caption (FLAN-T5)
    # ----------------------------
    st.write("### 🔹 Step 2: Marketing Caption Generation")

    style = st.selectbox("Select marketing tone:", ["Formal", "Trendy", "Fun", "Luxury"])

    # Build prompt based on tone
    prompt_map = {
        "Formal": f"Rewrite this image caption in a professional brand marketing tone: {base_caption}",
        "Trendy": f"Rewrite this caption in a trendy and engaging style with hashtags and emojis: {base_caption}",
        "Fun": f"Rewrite this caption in a fun, playful, and social media-friendly tone with emojis: {base_caption}",
        "Luxury": f"Rewrite this caption in a premium and luxurious marketing tone: {base_caption}"
    }

    prompt = prompt_map[style]
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True).to(device)
    with torch.no_grad():
        outputs = t5_model.generate(
            **inputs,
            max_new_tokens=64,
            temperature=0.9,
            top_p=0.95,
            do_sample=True
        )
    marketing_caption = tokenizer.decode(outputs[0], skip_special_tokens=True)

    st.success(f"💬 **Marketing Caption:** {marketing_caption}")

    # ----------------------------
    # 💾 Save Results
    # ----------------------------
    if st.button("💾 Save Caption"):
        os.makedirs("generated_captions", exist_ok=True)
        with open("generated_captions/results.txt", "a") as f:
            f.write(f"{uploaded_file.name}\t{base_caption}\t{marketing_caption}\n")
        st.info("✅ Captions saved successfully!")

# ----------------------------
# 🧾 Footer
# ----------------------------
st.markdown("---")
st.markdown(
    """
    **Developed by Krishna S**  
    *Generative AI Capstone Project — Digital University Kerala (2025)*  
    [GitHub Repository](https://github.com/YOUR_USERNAME/brand-aware-captioning)
    """
)
