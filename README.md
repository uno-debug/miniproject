# Covert Data Embedding Project

## Project Overview
This project aims to demonstrate the concept of steganography—embedding secret data (like text or files) within image or audio files. The main objective is to develop an application where users can hide and extract messages from media files.

## Installation Instructions
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/CovertDataEmbeddingProject.git
   ```
2. Navigate to the project folder:
   ```bash
   cd CovertDataEmbeddingProject
   ```
3. Create a virtual environment:
   ```bash
   python -m venv envi
   ```
4. Activate the virtual environment:
   - **On Windows**:
     ```bash
     .\envi\Scripts\activate
     ```
5. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use
- Run the Streamlit app to start the interface:
  ```bash
  streamlit run app/main.py
  ```

## Project Structure
- `app/`: Contains the main application logic files.
- `resources/`: Contains sample files (test images, audio) for testing.
- `requirements.txt`: List of required libraries.
- `README.md`: Project documentation.
