import streamlit as st
import requests
import hashlib
import pandas as pd

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="BrandCraft AI Dashboard",
    layout="wide",
    page_icon="🚀"
)

# -------------------------------
# Gradient background and button styling
# -------------------------------
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
        color: #000000;
    }
    .stButton>button {
        background-color: #FF6F61;
        color: white;
        font-size:16px;
        border-radius:12px;
        padding:12px;
        font-weight:bold;
    }
    .box:hover {
        transform: scale(1.02);
        transition: transform 0.3s;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.header("BrandCraft AI Controls")
business_type = st.sidebar.text_input("Business Type (e.g., Tech, Fashion, Fitness)")
num_suggestions = st.sidebar.slider("Number of Brand Suggestions", 1, 5, 3)
theme_color = st.sidebar.color_picker("Theme Color", "#FF6F61")

# -------------------------------
# Title
# -------------------------------
st.markdown(f"""
    <h1 style='text-align:center;color:{theme_color};text-shadow: 2px 2px #ffffff;'>🚀 BrandCraft AI Dashboard</h1>
    <p style='text-align:center;font-size:18px'>AI-powered branding automation: names, taglines, captions, logos & color palettes</p>
""", unsafe_allow_html=True)
st.markdown("---")

# -------------------------------
# Generate Button
# -------------------------------
if st.sidebar.button("Generate Brand Identity") and business_type:
    try:
        # Backend API
        brand_response = requests.get(f"http://localhost:5000/generate-brand?businessType={business_type}")
        brand_data = brand_response.json()
        all_brand_names = brand_data["brandSuggestions"][:num_suggestions]

        # Metrics
        total_brands = len(all_brand_names)
        total_taglines = total_brands
        total_captions = total_brands
        all_colors = []

        # Metrics Panel
        st.markdown("### 📊 AI Dashboard Metrics")
        col_metrics = st.columns(3)
        col_metrics[0].metric("Total Brands Generated", total_brands)
        col_metrics[1].metric("Taglines Generated", total_taglines)
        col_metrics[2].metric("Captions Generated", total_captions)
        st.markdown("---")

        # Grid layout for live demo feel
        for idx, brand_name in enumerate(all_brand_names, 1):
            # Tagline
            slogan_response = requests.get(f"http://localhost:5000/generate-slogan?brandName={brand_name}")
            slogan_data = slogan_response.json()

            # Caption
            caption_response = requests.get(f"http://localhost:5000/generate-caption?brandName={brand_name}")
            caption_data = caption_response.json()

            # Generate dynamic colors
            def generate_colors(name, num_colors=5):
                colors = []
                for i in range(num_colors):
                    hash_obj = hashlib.md5(f"{name}{i}".encode())
                    colors.append(f"#{hash_obj.hexdigest()[:6]}")
                return colors

            colors = generate_colors(brand_name)
            all_colors.extend(colors)

            # Grid columns
            col1, col2, col3 = st.columns([1.5,1.5,1.5])

            # Column 1: Brand Info Box
            with col1:
                st.markdown(f"""
                    <div class='box' style='background-color:#FFDAB9;padding:20px;border-radius:15px'>
                        <h3>🏷 Brand Name</h3>
                        <p style='font-size:20px;color:#8B4513'>{brand_name}</p>
                        <h4>💬 Tagline</h4>
                        <p style='font-size:18px;color:#4B0082'>{slogan_data['slogan']}</p>
                    </div>
                """, unsafe_allow_html=True)

            # Column 2: Social Caption Box
            with col2:
                st.markdown(f"""
                    <div class='box' style='background-color:#E6E6FA;padding:20px;border-radius:15px'>
                        <h4>📱 Social Media Caption</h4>
                        <p style='font-size:16px;color:#B22222'>{caption_data['caption']}</p>
                        <h4>🖌 Logo Idea</h4>
                        <p style='font-size:16px;color:#4A148C'>{brand_name}</p>
                    </div>
                """, unsafe_allow_html=True)

            # Column 3: Color Palette Box
            with col3:
                st.subheader("🎨 Color Palette")
                color_cols = st.columns(len(colors))
                for i, c in enumerate(colors):
                    color_cols[i].markdown(f"<div style='background-color:{c};padding:40px;border-radius:10px'></div>", unsafe_allow_html=True)

                # AI Insight
                st.markdown(f"<p style='color:#2E7D32;font-weight:bold'>Insight: This brand is catchy, modern, and suitable for {business_type} industry.</p>", unsafe_allow_html=True)

        # -------------------------------
        # Color Distribution Chart
        # -------------------------------
        st.markdown("---")
        st.subheader("🎨 Color Distribution Across All Brands")
        color_counts = pd.Series(all_colors).value_counts()
        st.bar_chart(color_counts)

    except Exception as e:
        st.error(f"Error connecting to backend: {e}")

elif not business_type:
    st.info("Enter a business type in the sidebar and click Generate Brand Identity")