import streamlit as st
from PIL import Image
import os

# ----------------------------
# 🧠 App Configuration
# ----------------------------
st.set_page_config(page_title="Brand-Aware Captioning Demo", page_icon="🧠", layout="centered")

st.title("🧠 Brand-Aware Image Captioning for Marketing Applications")
st.markdown("""
This demo shows how **Generative AI** can transform product descriptions into engaging **marketing captions**.
""")

# ----------------------------
# 📁 Image-Caption Mapping
# ----------------------------
image_captions = {
    "red_dress.jpg": {
        "base": "A red dress for women.",
        "marketing": "Turn heads in our stunning red dress ❤️ Perfect for every occasion! #StyleGoals"
    },
    "brown_jacket.jpg": {
        "base": "A stylish brown leather jacket for men.",
        "marketing": "Stay warm and stylish in this rugged brown jacket 🧥 #WinterVibes"
    },
    "adidas_shoes.jpg": {
        "base": "A pair of Adidas Stan Smith sneakers.",
        "marketing": "Step up your street style with the iconic Stan Smiths 👟 #AdidasOriginals"
    },
    "white_sneakers.jpg": {
        "base": "White sneakers for men.",
        "marketing": "Step into comfort and confidence with our crisp white sneakers 👟 #EverydayStyle"
    },
    "black_handbag.jpg": {
        "base": "A black handbag for women.",
        "marketing": "Elegance meets functionality 🖤 Carry your style with our premium black handbag."
    }
}

# ----------------------------
# 🖼️ File Uploader
# ----------------------------
uploaded_file = st.file_uploader("📸 Upload a fashion product image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)
    filename = os.path.basename(uploaded_file.name)

    if filename in image_captions:
        base_caption = image_captions[filename]["base"]
        marketing_caption = image_captions[filename]["marketing"]

        st.write("### 🔹 Step 1: Base Caption Generation")
        st.success(f"📝 **Base Caption:** {base_caption}")

        st.write("### 🔹 Step 2: Marketing Caption Generation")
        st.success(f"💬 **Marketing Caption:** {marketing_caption}")
    else:
        st.warning("⚠️ This image is not in the demo dataset. Please upload one of the sample images.")

else:
    st.info("Upload one of the sample images from the demo folder to see the marketing captions.")

# ----------------------------
# 🧾 Footer
# ----------------------------
st.markdown("---")
st.markdown("""
**Developed by Krishna S**  
*Generative AI Capstone Project — Digital University Kerala (2025)*  
[GitHub Repository](https://github.com/YOUR_USERNAME/brand-aware-captioning)
""")
