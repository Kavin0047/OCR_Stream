import os
import google.generativeai as genai
from PIL import Image
import pytesseract

os.environ['GOOGLE_API_KEY'] = 'AIzaSyBwram1ejmI0wYme63-XauP-PDXsLN1UDs'
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

def load_image_from_path(image_path):
    return Image.open(image_path)

def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text

def generate_response_from_text(text, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    full_prompt = f"{prompt} Extracted text: {text}"
    
    response = model.generate_content([full_prompt])
    
    return response.text

image_path = "C:\\Users\\KAVIN\\OneDrive\\Desktop\\1733206996511.jpeg"
image = load_image_from_path(image_path)

extracted_text = extract_text_from_image(image)

prompt = "whats the card holder name"

result = generate_response_from_text(extracted_text, prompt)
print("\nExtracted Information:")
print(result)
