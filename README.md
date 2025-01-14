# Social Media Content Analyzer

An intelligent application that analyzes social media posts from uploaded documents and suggests improvements to maximize engagement. 🚀

## Features

- **Document Upload**:  
  Upload PDF or image files (e.g., scanned documents) with an easy drag-and-drop or file picker interface.

- **Text Extraction**:  
  - **PDF Parsing**: Extracts text from PDF files while maintaining formatting.  
  - **OCR (Optical Character Recognition)**: Extracts text from image files using Tesseract.

- **Engagement Suggestions**:  
  The app provides actionable suggestions for:  
  - Improving readability.  
  - Enhancing positivity and sentiment.  
  - Adding clear calls-to-action (CTAs).  
  - Optimizing keywords and hashtags.

- **User Experience**:  
  - Loading states for smooth interaction.  
  - Informative error handling.

## Installation

### Prerequisites
Ensure that [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) is installed on your system.  
For installation instructions, visit [Tesseract Installation Guide](https://github.com/tesseract-ocr/tesseract).

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/pranavsuriya/social-media-analyzer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd social-media-analyzer
   ```
3. Install the required dependencies
  ```bash
  pip install -r requirements.txt
  ```
4.Run the application
  ```bash
  streamlit run test1.py
  ```

## Usage

1. Upload a PDF or image file containing social media content.
2. View the extracted text in the app.
3. Review the suggested improvements to optimize your post.

## Tech Stack

- **Python**: Core programming language.
- **Streamlit**: Frontend and deployment framework.
- **PyPDF2**: PDF parsing for text extraction.
- **Pillow**: Image processing library.
- **Tesseract-OCR**: OCR technology for image-to-text conversion.
- **TextBlob**: Sentiment analysis.
- **Textstat**: Readability analysis.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.


----

Made with ❤️ by [S R Pranav Suriya](https://github.com/pranavsuriya-sr).  
Connect with me on [LinkedIn](https://www.linkedin.com/in/sr-pranavsuriya/).


  
