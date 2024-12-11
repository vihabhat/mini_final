import streamlit as st
from PIL import Image
import os

# Import the backend functions
from backend import generate_caption, answer_question

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Image Insight", 
        page_icon=":camera:", 
        layout="wide"
    )

    # Title
    st.title("🖼️ Image Insight")
    st.write("Explore your images with AI-powered caption generation and Q&A")

    # Sidebar for instructions
    st.sidebar.header("How to Use")
    st.sidebar.info("""
    1. Upload an image
    2. Generate a caption
    3. Ask a question about the image
    """)

    # Image upload
    uploaded_file = st.file_uploader(
        "Choose an image...", 
        type=["jpg", "jpeg", "png", "webp"],
        help="Upload an image you want to analyze"
    )

    # If an image is uploaded
    if uploaded_file is not None:
        # Create a temporary file to save the uploaded image
        with open("temp_image.jpg", "wb") as f:
            f.write(uploaded_file.getvalue())
        
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Columns for buttons
        col1, col2 = st.columns(2)

        # Caption generation
        with col1:
            if st.button("Generate Caption", type="primary"):
                try:
                    caption = generate_caption("temp_image.jpg")
                    st.success(f"Caption: {caption}")
                except Exception as e:
                    st.error(f"Error generating caption: {e}")

        # Question answering
        with col2:
            question = st.text_input("Ask a question about the image")
            if st.button("Get Answer", type="secondary"):
                if question:
                    try:
                        answer = answer_question("temp_image.jpg", question)
                        st.info(f"Answer: {answer}")
                    except Exception as e:
                        st.error(f"Error answering question: {e}")
                else:
                    st.warning("Please enter a question")

        # Clean up the temporary file
        if os.path.exists("temp_image.jpg"):
            os.remove("temp_image.jpg")

if __name__ == "__main__":
    main()