import os
import io
import streamlit as st
import google.generativeai as genai
from PIL import Image
from PIL.ExifTags import TAGS
import pytesseract

# Configure the API key
os.environ['GOOGLE_API_KEY'] = 'API_KEY'
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

def load_image_from_file(uploaded_file):
    try:
        return Image.open(uploaded_file)
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None

def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text

def generate_response_from_text(text, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    full_prompt = f"{prompt} Extracted text: {text}"
    response = model.generate_content([full_prompt])
    return response.text

def extract_metadata(uploaded_file):
    metadata = {}
    st.write(f"File name: {uploaded_file.name}")
    st.write(f"File type: {uploaded_file.type}")
    st.write(f"File size: {uploaded_file.size} bytes")
    
    try:
        # Try to open the image with Pillow
        image = Image.open(io.BytesIO(uploaded_file.getvalue()))
        st.write(f"Image format: {image.format}")
        st.write(f"Image mode: {image.mode}")
        st.write(f"Image size: {image.size}")
        
        # Try to get EXIF data
        exif_data = image._getexif()
        if exif_data:
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                metadata[tag] = str(value)
        else:
            st.info("No EXIF metadata found.")
        
        # Try to get other image info
        for key, value in image.info.items():
            if key not in metadata:
                metadata[key] = str(value)
        
    except Exception as e:
        st.error(f"Error processing image: {e}")
    
    return metadata

# Streamlit app
def main():
    st.title("AI-based Image Text Extraction and Response Generator")

    st.write("Upload an image, extract text from it, and ask a question about the image content.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Load the image
        image = load_image_from_file(uploaded_file)

        if image is not None:
            # Display the image
            st.image(image, caption="Uploaded Image", use_column_width=True)

            # Extract text from the image
            extracted_text = extract_text_from_image(image)
            st.subheader("Extracted Text:")
            st.write(extracted_text)

            # Prompt for user input
            prompt = st.text_input("Enter your question about the image")

            col1, col2 = st.columns(2)

            with col1:
                if st.button("Generate Response"):
                    if extracted_text and prompt:
                        result = generate_response_from_text(extracted_text, prompt)
                        st.subheader("Generated Response:")
                        st.write(result)
                    else:
                        st.warning("Please ensure both text is extracted and a question is provided.")

            with col2:
                if st.button("View Metadata"):
                    metadata = extract_metadata(uploaded_file)
                    st.subheader("Image Metadata:")
                    if metadata:
                        for key, value in metadata.items():
                            st.write(f"{key}: {value}")
                    else:
                        st.write("No metadata found for this image.")

if __name__ == "__main__":
    main()
