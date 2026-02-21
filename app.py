import streamlit as st
import requests

st.set_page_config(page_title="BrandCraft AI", layout="centered")
st.title("🚀 BrandCraft - AI Branding Automation System")
st.markdown("Generate brand name, slogan, and caption instantly")


business_type = st.text_input("Enter Business Type (e.g., Tech, Fashion, Fitness)")

if st.button("Generate Brand Identity"):
    if business_type:
        
        try:
            
            brand_response = requests.get(
                f"http://localhost:5000/generate-brand?businessType={business_type}"
            )
            brand_data = brand_response.json()
            brand_name = brand_data["brandSuggestions"][0]  # Pick first for demo

            
            slogan_response = requests.get(
                f"http://localhost:5000/generate-slogan?brandName={brand_name}"
            )
            slogan_data = slogan_response.json()

            
            caption_response = requests.get(
                f"http://localhost:5000/generate-caption?brandName={brand_name}"
            )
            caption_data = caption_response.json()

  
            st.subheader("🏷 Brand Name")
            st.write(brand_name)

            st.subheader("💬 Tagline")
            st.write(slogan_data["slogan"])

            st.subheader("📱 Social Media Caption")
            st.write(caption_data["caption"])

        except Exception as e:
            st.error(f"Error connecting to backend: {e}")

    else:
        st.warning("Please enter a business type")