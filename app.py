import streamlit as st
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #1e5631 10%, #a7c957 100%);
        color: white;
    }
   div[data-baseweb="slider"] > div > div {
        background: #2196F3 !important;  /* Blue track */
    }

    /* Empty track color */
    div[data-baseweb="slider"] > div {
        background: rgba(255, 255, 255, 0.3) !important;
    }

    /* The actual knob (thumb) */
    div[data-baseweb="slider"] > div > div > div {
        background: white !important;  /* White knob */
        border: 2px solid #2196F3 !important; /* Blue outline */
        box-shadow: 0px 0px 6px rgba(33, 150, 243, 0.6);
        width: 22px !important;
        height: 22px !important;
    }
    stSlider label, .stMarkdown p, .stSelectSlider label {
        color: white !important;
        font-weight: 500;
    }
    </style>
    """,
    unsafe_allow_html=True
)
def main():
    st.title("Monthwise Stubble Content mapping")
    months = ['September', 'October', 'November', 'December', 'January']
    image_map = {
    'September': 'images/september.jpeg',
    'October': 'images/october.jpeg',
    'November': 'images/november.jpeg',
    'December': 'images/december.jpeg',
    'January': 'images/january.jpeg'
}

    selected_month = st.select_slider(
        "Select a month:",
        options=months
    )
    if selected_month:
        st.write(f"Displaying map for: **{selected_month}**")

        image_url = image_map[selected_month]
        st.image(image_url, caption=f"This is the map for {selected_month}.")


if __name__ == "__main__":
    main()












