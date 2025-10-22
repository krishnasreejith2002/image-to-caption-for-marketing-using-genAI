import streamlit as st
from PIL import Image
import os

# ----------------------------
# 🧠 App Configuration
# ----------------------------
st.set_page_config(page_title="Brand-Aware Captioning Demo", page_icon="🛍️", layout="centered")
st.markdown("""
    <style>
    /* Title Styling */
    h1 {
        color: #E91E63;
        text-align: center;
        font-size: 2.4em;
        font-weight: bold;
    }

    /* Captions */
    .stSuccess {
        background-color: #FFF8FB;
        border-left: 4px solid #E91E63;
        padding: 10px;
        border-radius: 8px;
        font-size: 1.1em;
    }

    /* Buttons */
    div.stButton > button:first-child {
        background-color: #E91E63;
        color: white;
        font-weight: 600;
        border-radius: 10px;
        height: 3em;
        width: 12em;
        border: none;
        transition: all 0.3s ease-in-out;
    }

    div.stButton > button:first-child:hover {
        background-color: #C2185B;
        transform: scale(1.05);
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #F8E8EE;
    }

    /* Footer */
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Brand-Aware Image Captioning for Marketing Applications")
st.markdown("""
This demo shows how **Generative AI** can transform product descriptions into engaging **marketing captions**.
""")

# ----------------------------
# 📁 Image-Caption Mapping
# ----------------------------
image_captions = {
    "grey_shoes.jpg.jpg": {
        "base": "Grey formal shoes for men.",
        "marketing": "Step into sophistication with our classic grey formal shoes 👞 — where comfort meets class. Perfect for the boardroom or beyond. #SmartLook #StyleThatSpeaks"
    },
    "brown_jacket.jpg.jpg": {
        "base": "A brown jacket for men.",
        "marketing": "Stay warm and stylish with our rugged brown jacket 🧥 — crafted for confidence and comfort. Own the season in style! #WinterVibes #BoldAndClassic"
    },
    "blue_jeans.jpg.jpg": {
        "base": "Blue jeans for men.",
        "marketing": "Classic fit, timeless style. Rock your day in our versatile blue jeans 👖 — made for every mood, every move. #DenimVibes #EverydayEssential"
    },
    "white_sneakers.jpg.jpg": {
        "base": "White sneakers for men.",
        "marketing": "Step into comfort and confidence with our crisp white sneakers 👟 — minimal, clean, and made to move. #EverydayStyle #FreshKicks"
    },
    "red_dress.jpg.jpg": {
        "base": "A red dress for women.",
        "marketing": "Turn heads in our stunning red dress ❤️ — elegant, bold, and made to make memories. Perfect for every occasion! #StyleGoals #RedHotFashion"
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
