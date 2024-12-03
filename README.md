
# Advanced OCR and Generative AI Application

## Key Features

### Core Functionalities
1. **Image Upload and Cropping**:
   - Upload images in `.jpg`, `.jpeg`, or `.png` formats.
   - Optionally crop the image to focus on specific areas.

2. **Preprocessing Options**:
   - Apply **Grayscale** or **Thresholding** filters to enhance OCR accuracy.

3. **OCR (Optical Character Recognition)**:
   - Extract text from images using Tesseract OCR with support for multiple languages:
     - **English**, **Spanish**, **French**, **German**, **Italian**.

4. **AI-Generated Insights**:
   - Generate detailed responses based on the extracted text using Google's Generative AI.
   - Customize the tone of responses: **Formal**, **Casual**, **Concise**, or **Descriptive**.

5. **Download Options**:
   - Download the extracted text or AI-generated response as `.txt` files.

---

### Advanced Features
1. **Dynamic Image Quality Feedback**:
   - Visualize and confirm preprocessing results to ensure optimal OCR performance.

2. **Text Analysis**:
   - Display **Word Count** and **Character Count** for extracted text.

3. **Interactive Prompts**:
   - Provide custom prompts for AI interaction to generate contextually relevant responses.

4. **User-Friendly Design**:
   - Intuitive interface with clear headings, organized layouts, and easy-to-use controls.

---

## How to Use

### Step 1: Set Up the Application
1. **Install Required Libraries**:
   ```bash
   pip install pillow pytesseract streamlit google-generativeai streamlit-cropper
   ```

2. **Run the App**:
   ```bash
   streamlit run app.py
   ```

### Step 2: Configure API Key
1. On the left sidebar, enter your **Google API Key** (required for Generative AI features).

---

### Step 3: Process Images
1. **Upload an Image**:
   - Drag and drop or select an image from your local system.

2. **Crop the Image** *(Optional)*:
   - Adjust the cropping tool to focus on specific areas.

3. **Preprocess the Image**:
   - Choose preprocessing options:
     - **None**: Use the original image.
     - **Grayscale**: Convert the image to black and white.
     - **Thresholding**: Enhance contrast for OCR.

---

### Step 4: Extract Text
1. Select the **OCR Language** in the sidebar.
2. View the extracted text displayed in the "Extracted Text" section.
3. **Download the Text**:
   - Click the "Download Extracted_Text.txt" button.

---

### Step 5: Generate AI Response
1. Enter a **Custom Prompt** to describe what you want the AI to generate.
2. Choose the **Response Tone** (e.g., Formal, Casual, etc.).
3. Click "Generate AI Response" to see the output.
4. **Download the Response**:
   - Click the "Download AI_Response.txt" button.

---

## Example Use Cases
- **Business**:
  - Extract and analyze text from invoices, forms, or scanned documents.
- **Education**:
  - Generate summaries or explanations from textbook images.
- **Content Creation**:
  - Generate creative writing or captions based on image content.
- **Translation**:
  - Extract text in one language and use a translator for localization.

---

## Troubleshooting

### Common Issues and Fixes
1. **API Key Errors**:
   - Ensure your API Key is active and entered correctly in the sidebar.

2. **Poor OCR Accuracy**:
   - Use high-quality images with clear text.
   - Apply preprocessing filters like Grayscale or Thresholding.

3. **Library Installation Issues**:
   - Ensure Python is installed, and libraries are up to date:
     ```bash
     pip install --upgrade pytesseract pillow streamlit
     ```

4. **Image Cropping Errors**:
   - Use the cropping tool to focus only on areas containing text.

---

## Acknowledgments
- **Tesseract OCR**: For robust text extraction capabilities.
- **Google Generative AI**: For AI-driven insights and responses.
- **Streamlit**: For a seamless, interactive user interface.

---

## Contributing
Want to add more features or improve the app? Fork the project and submit a pull request. Suggestions are welcome!

---

## License
This project is licensed under the **MIT License**. Feel free to use, modify, and distribute it. 😊

---

Enjoy using the **Advanced OCR and Generative AI Application**! 🚀
