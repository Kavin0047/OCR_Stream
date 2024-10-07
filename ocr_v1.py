import os
import streamlit as st
import google.generativeai as genai
from PIL import Image
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

            if st.button("Generate Response"):
                if extracted_text and prompt:
                    result = generate_response_from_text(extracted_text, prompt)
                    st.subheader("Generated Response:")
                    st.write(result)
                else:
                    st.warning("Please ensure both text is extracted and a question is provided.")

if __name__ == "__main__":
    main()
