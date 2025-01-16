import streamlit as st
from PyPDF2 import PdfReader
from PIL import Image
import pytesseract
import tempfile
import os
from textblob import TextBlob
import textstat

# Title and description
st.title("Social Media Content Analyzer")
st.write("An application that analyzes social media posts and suggests engagement improvements.")

# File upload
uploaded_file = st.file_uploader("Upload a PDF or Image file", type=["pdf", "jpg", "jpeg", "png"])

# Function to suggest improvements
def suggest_improvements(text):
    suggestions = []

    # Readability analysis
    readability_score = textstat.flesch_reading_ease(text)
    if readability_score < 60:
        suggestions.append("Consider simplifying the text for better readability.")

    # Sentiment analysis
    sentiment = TextBlob(text).sentiment
    if sentiment.polarity < 0.1:
        suggestions.append("Consider using more positive language to engage your audience.")

    # Call-to-action detection
    if not any(word in text.lower() for word in ["click", "subscribe", "follow", "learn", "join"]):
        suggestions.append("Add a clear call-to-action to guide your audience.")

    # Keyword and hashtag optimization
    if len(text.split()) > 50 and "#" not in text:
        suggestions.append("Consider adding relevant hashtags for better reach.")

    return suggestions

# Loading state
if uploaded_file:
    with st.spinner("Processing your file..."):
        try:
            extracted_text = ""

            # Handling PDF files
            if uploaded_file.type == "application/pdf":
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                    temp_pdf.write(uploaded_file.read())
                    temp_pdf_path = temp_pdf.name

                pdf_reader = PdfReader(temp_pdf_path)
                for page in pdf_reader.pages:
                    extracted_text += page.extract_text() + "\n"

                os.remove(temp_pdf_path)

            # Handling Image files
            elif uploaded_file.type in ["image/jpeg", "image/png", "image/jpg"]:
                image = Image.open(uploaded_file)
                extracted_text = pytesseract.image_to_string(image)

            # Display extracted text
            if extracted_text.strip():
                st.subheader("Extracted Text")
                st.text_area("", extracted_text, height=300)

                # Display suggestions
                st.subheader("Suggested Improvements")
                improvements = suggest_improvements(extracted_text)
                if improvements:
                    for i, suggestion in enumerate(improvements, 1):
                        st.write(f"{i}. {suggestion}")
                else:
                    st.write("Your content looks great! No major improvements needed.")
            else:
                st.warning("No text could be extracted from the file. Please try with another document.")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Instructions
else:
    st.info("Please upload a PDF or image file to begin text extraction.")

# Additional notes
st.markdown("---")
st.markdown("### Approach Documentation")
st.markdown(
    "- **Document Upload**: Supports PDF and common image formats like JPG, JPEG, and PNG.\n"
    "- **Text Extraction**: Utilizes `PyPDF2` for PDF parsing and `pytesseract` for OCR-based text extraction from images.\n"
    "- **Error Handling**: Includes file type validation and extraction error warnings.\n"
    "- **User Experience**: Displays loading states for improved interactivity."
)

# External dependencies reminder
st.markdown(
    "**Note**: Ensure Tesseract-OCR is installed and available in your system's PATH. [Installation Instructions](https://github.com/tesseract-ocr/tesseract)."
)

st.markdown("---")
st.markdown(
    "<div style='text-align: center;'>" \
    "Made with ❤️ by <a href='https://github.com/pranavsuriya-sr' target='_blank'>S R Pranav Suriya</a>. " \
    "Connect with me on " 
    "<a href='https://www.linkedin.com/in/sr-pranavsuriya/' target='_blank'>"
    "<img src='https://cdn-icons-png.flaticon.com/512/174/174857.png' alt='LinkedIn' style='width:20px; height:20px; vertical-align:middle;'></a>" \
    "</div>",
    unsafe_allow_html=True
)
