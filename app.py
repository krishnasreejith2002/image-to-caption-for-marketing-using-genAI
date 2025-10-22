import streamlit as st
from PIL import Image
import os

# ----------------------------
# 🧠 App Configuration
# ----------------------------
st.set_page_config(page_title="Brand-Aware Captioning Demo", page_icon="🛍️", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
    h1 {
        color: #E91E63;
        text-align: center;
        font-size: 2.4em;
        font-weight: bold;
    }
    .stSuccess {
        background-color: #FFF8FB;
        border-left: 4px solid #E91E63;
        padding: 10px;
        border-radius: 8px;
        font-size: 1.1em;
    }
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
    [data-testid="stSidebar"] {
        background-color: #F8E8EE;
    }
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# 🌸 App Header
# ----------------------------
st.title("🧠 Brand-Aware Image Captioning for Marketing Applications")
st.markdown("""
This demo shows how **Generative AI** can transform simple product descriptions into engaging **marketing captions**.
""")

# ----------------------------
# 📁 Image-Caption Mapping
# ----------------------------
image_captions = {
    "grey_shoes.jpg": {
        "base": "Grey formal shoes for men.",
        "marketing": "Step into sophistication with our classic grey formal shoes 👞 — where comfort meets class. Perfect for the boardroom or beyond. #SmartLook #StyleThatSpeaks"
    },
    "brown_jacket.jpg": {
        "base": "A brown jacket for men.",
        "marketing": "Stay warm and stylish with our rugged brown jacket 🧥 — crafted for confidence and comfort. Own the season in style! #WinterVibes #BoldAndClassic"
    },
    "blue_jeans.jpg": {
        "base": "Blue jeans for men.",
        "marketing": "Classic fit, timeless style. Rock your day in our versatile blue jeans 👖 — made for every mood, every move. #DenimVibes #EverydayEssential"
    },
    "white_sneakers.jpg": {
        "base": "White sneakers for men.",
        "marketing": "Step into comfort and confidence with our crisp white sneakers 👟 — minimal, clean, and made to move. #EverydayStyle #FreshKicks"
    },
    "red_dress.jpg": {
        "base": "A red dress for women.",
        "marketing": "Turn heads in our stunning red dress ❤️ — elegant, bold, and made to make memories. Perfect for every occasion! #StyleGoals #RedHotFashion"
    }
}

# ----------------------------
# 🖼️ File Uploader
# ----------------------------
st.markdown("### 📸 Upload a Fashion Product Image")
uploaded_file = st.file_uploader("Upload one of the demo images below 👇", type=["jpg", "jpeg", "png"])

# Show available demo images
demo_images = list(image_captions.keys())
st.markdown(f"""
<small>🧩 **Demo images available:** {', '.join(demo_images)}</small>
""", unsafe_allow_html=True)

# ----------------------------
# 🧠 Caption Generation Logic
# ----------------------------
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Normalize filename for flexible matching
    filename = os.path.basename(uploaded_file.name).lower().replace(" ", "_")
    matched_key = None
    for key in image_captions.keys():
        if key.lower().replace(" ", "_").split('.')[0] in filename:
            matched_key = key
            break

    if matched_key:
        base_caption = image_captions[matched_key]["base"]
        marketing_caption = image_captions[matched_key]["marketing"]

        st.markdown("## ✨ Caption Generation Results")

        # Two-column layout for Base and Marketing captions
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"""
                <div style='background-color:#F8E8EE;border-radius:10px;padding:15px;
                            border-left:4px solid #E91E63;box-shadow:0 3px 8px rgba(0,0,0,0.05);'>
                    <h4>📝 Base Caption</h4>
                    <p style='font-size:1.05em;color:#333;'>{base_caption}</p>
                </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
                <div style='background-color:#E8F8EE;border-radius:10px;padding:15px;
                            border-left:4px solid #4CAF50;box-shadow:0 3px 8px rgba(0,0,0,0.05);'>
                    <h4>💬 Marketing Caption</h4>
                    <p style='font-size:1.05em;color:#111;font-weight:500;'>{marketing_caption}</p>
                </div>
            """, unsafe_allow_html=True)

    else:
        st.warning("⚠️ This image is not in the demo dataset. Please upload one of the sample images listed above.")

# ----------------------------
# 🧾 Footer
# ----------------------------
st.markdown("---")
st.markdown("""
**Developed by Krishna S**  
*Generative AI Capstone Project — Digital University Kerala (2025)*  
[🌐 GitHub Repository](https://github.com/YOUR_USERNAME/brand-aware-captioning)
""")
