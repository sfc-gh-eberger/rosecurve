import streamlit as st

def main():
    st.title('Image Uploader')

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.write('Uploaded Image:')
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

if __name__ == '__main__':
    main()

