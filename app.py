import streamlit as st
from PIL import Image
import os

# ----------------------------
# 🧠 App Configuration
# ----------------------------
st.set_page_config(
    page_title="Brand-Aware Captioning Demo",
    page_icon="🛍️",
    layout="centered"
)

# 💅 Custom Styling + Animations
st.markdown("""
    <style>
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(15px);}
        to {opacity: 1; transform: translateY(0);}
    }
    div[data-testid="stMarkdownContainer"] > div {
        animation: fadeIn 0.8s ease-in-out;
    }

    /* Page background */
    [data-testid="stAppViewContainer"] {
        background-color: #fffafc;
        font-family: "Poppins", sans-serif;
    }

    h1 {
        color: #E91E63;
        text-align: center;
        font-size: 2.3em;
        font-weight: 700;
        margin-bottom: 10px;
    }

    h4 {
        margin-bottom: 5px;
    }

    /* Card styling */
    .card {
        border-radius: 12px;
        padding: 18px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        margin-top: 10px;
        background-color: #fff;
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

    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# 🧠 App Header
# ----------------------------
st.title("🧠 Brand-Aware Image Captioning for Marketing Applications")
st.markdown("""
This demo shows how **Generative AI** can transform plain product descriptions 
into stylish, brand-ready **marketing captions**.
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
uploaded_file = st.file_uploader("📸 Upload a fashion product image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)
    filename = os.path.basename(uploaded_file.name)

    if filename in image_captions:
        base_caption = image_captions[filename]["base"]
        marketing_caption = image_captions[filename]["marketing"]

        st.markdown("## ✨ Caption Generation Results")

        # 🌸 Two-column comparison layout
        col1, col2 = st.columns(2)

        with col1:
            st.markdown(f"""
                <div class='card' style='border-left: 5px solid #E91E63; background-color:#fff6f9;'>
                    <h4>📝 Base Caption</h4>
                    <p style='font-size:1.05em;color:#333;'>{base_caption}</p>
                </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
                <div class='card' style='border-left: 5px solid #4CAF50; background-color:#f3fff6;'>
                    <h4>💬 Marketing Caption</h4>
                    <p style='font-size:1.05em;color:#111;font-weight:500;'>{marketing_caption}</p>
                </div>
            """, unsafe_allow_html=True)

    else:
        st.warning("⚠️ This image is not in the demo dataset. Please upload one of the sample images below:")
        st.write(", ".join(list(image_captions.keys())))

else:
    st.info("📤 Upload one of the sample images to see results.")

# ----------------------------
# 🧾 Footer
# ----------------------------
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:gray; font-size:0.9em; margin-top:25px;'>
Developed by <b>Krishna S</b> | Generative AI Capstone Project 🎓<br>
<span style='color:#E91E63;'>Digital University Kerala — 2025</span><br>
<a href='https://github.com/YOUR_USERNAME/brand-aware-captioning' style='color:#E91E63;text-decoration:none;'>
🔗 GitHub Repository
</a>
</div>
""", unsafe_allow_html=True)
