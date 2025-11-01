import streamlit as st
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #1e5631 10%, #a7c957 100%);
        color: white;
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








