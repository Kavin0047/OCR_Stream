import os
import google.generativeai as genai
from PIL import Image
import pytesseract


os.environ['GOOGLE_API_KEY'] = 'AIzaSyBwram1ejmI0wYme63-XauP-PDXsLN1UDs'
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])


def load_image_from_path(image_path):
    try:
        return Image.open(image_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text

def generate_response_from_text(text, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    full_prompt = f"{prompt} Extracted text: {text}"
    response = model.generate_content([full_prompt])
    return response.text

def main():
    while True:
        image_path = input("Enter the full image file path (or 'q' to quit): ")
        if image_path.lower() == 'q':
            break
        
        image = load_image_from_path(image_path)
        if image is None:
            continue
        
        extracted_text = extract_text_from_image(image)
        
        prompt = input("Enter your question about the image: ")

        result = generate_response_from_text(extracted_text, prompt)
        print("\nExtracted Information:")
        print(result)
        print()
        print("****The Result may not be accurate please verify at once****")
        print()

        another_image = input("Do you want to process another image? (yes/no): ")
        if another_image.lower() not in ['yes','y']:
            break

if __name__ == "__main__":
    main()
