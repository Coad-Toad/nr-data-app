
import streamlit as st
import requests

NRDB_URL = "https://netrunnerdb.com/api/2.0/public/card/01001"

@st.cache_data
def load_data():
    response = requests.get(NRDB_URL, timeout=10)
    response.raise_for_status()
    return response.json()

try:
    data = load_data()
    st.success("Card loaded successfully!")

    card = data["data"][0]

    img_url = data["imageUrlTemplate"].replace("{code}", card["code"])

    st.title(card.get("title"))
    
    st.image(img_url)
    
    if st.checkbox("Show raw data", value=True):
        st.subheader("Raw card data")
        st.json(data)

except requests.exceptions.RequestException as e:
    st.error(f"Failed to load card data: {e}")


