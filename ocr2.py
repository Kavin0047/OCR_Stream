import os
import google.generativeai as genai
from PIL import Image, ImageOps
import pytesseract
import streamlit as st
from io import BytesIO
from streamlit_cropper import st_cropper

st.sidebar.title("Configuration")
api_key = st.sidebar.text_input("Enter Google API Key", type="password")
if api_key:
    os.environ['GOOGLE_API_KEY'] = api_key
    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])


st.sidebar.title("OCR Settings")
language = st.sidebar.selectbox(
    "Select OCR Language",
    options=["eng", "spa", "fra", "deu", "ita"],
    format_func=lambda x: {
        "eng": "English",
        "spa": "Spanish",
        "fra": "French",
        "deu": "German",
        "ita": "Italian"
    }[x]
)

def load_image_from_upload(uploaded_file):
    """Load an uploaded image file."""
    try:
        return Image.open(uploaded_file)
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None

def preprocess_image(image, preprocess_option):
    """Apply preprocessing to the image."""
    try:
        if preprocess_option == "Grayscale":
            return ImageOps.grayscale(image)
        elif preprocess_option == "Thresholding":
            return image.convert("L").point(lambda x: 0 if x < 128 else 255, '1')
        else:
            return image
    except Exception as e:
        st.error(f"Error preprocessing image: {e}")
        return None

def extract_text_from_image(image, lang):
    """Extract text from the image using pytesseract."""
    try:
        text = pytesseract.image_to_string(image, lang=lang)
        return text.strip()
    except Exception as e:
        st.error(f"Error during text extraction: {e}")
        return None

def generate_response_from_text(text, prompt, tone):
    """Generate a response from the Generative AI model."""
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        full_prompt = f"{prompt}\nExtracted text: {text}\nResponse tone: {tone}"
        response = model.generate_content([full_prompt])
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return None

def download_text_file(filename, content):
    """Download content as a text file."""
    buffer = BytesIO()
    buffer.write(content.encode())
    buffer.seek(0)
    st.download_button(
        label=f"Download {filename}",
        data=buffer,
        file_name=filename,
        mime="text/plain"
    )

def main():
    """Main function to run the Streamlit app."""
    st.title("Advanced OCR and Generative AI Interface")
    st.write("Upload an image, preprocess it, extract text, and interact with Google's Generative AI.")


    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

    if uploaded_file:

        image = load_image_from_upload(uploaded_file)
        if image:
            st.image(image, caption="Uploaded Image", use_column_width=True)

            st.write("### Crop the Image (Optional)")
            cropped_image = st_cropper(image, realtime_update=True, aspect_ratio=None)

            preprocess_option = st.radio(
                "Preprocessing Options",
                options=["None", "Grayscale", "Thresholding"]
            )
            processed_image = preprocess_image(cropped_image, preprocess_option)
            if processed_image:
                st.image(processed_image, caption="Processed Image", use_column_width=True)

                extracted_text = extract_text_from_image(processed_image, lang=language)
                if extracted_text:
                    st.write("### Extracted Text")
                    st.write(extracted_text)

                    download_text_file("Extracted_Text.txt", extracted_text)

                    st.write(f"**Word Count**: {len(extracted_text.split())}")
                    st.write(f"**Character Count**: {len(extracted_text)}")

                    prompt = st.text_input("Enter your prompt for the AI model", value="Describe the content of the image.")
                    tone = st.selectbox("Select Response Tone", options=["Formal", "Casual", "Concise", "Descriptive"])

                    if st.button("Generate AI Response"):
                        response = generate_response_from_text(extracted_text, prompt, tone)
                        if response:
                            st.write("### AI Generated Text")
                            st.write(response)

                            download_text_file("AI_Response.txt", response)

if __name__ == "__main__":
    main()
