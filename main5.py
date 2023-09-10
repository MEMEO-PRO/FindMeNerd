import spacy
from PyPDF2 import PdfReader
import os

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()

# Load the spaCy model
nlp = spacy.load("en_core_web_lg")

# Sample resume text
sample_resume = extract_text_from_pdf("/Users/yashedake/Downloads/web-main/sample/sample.pdf")  # Replace 'paths' with the actual path to your sample resume PDF

# Function to calculate similarity score between two texts
def calculate_similarity(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    similarity_score = doc1.similarity(doc2)
    return similarity_score

# Define a function to find the most compatible resume based on preference
def predictss(preference):
    if preference == "Male":
        pdf_resume_directory = "resumes/Male/"
    else:
        pdf_resume_directory = "resumes/Female/"

    most_compatible_resume = None
    highest_similarity = -1

    for filename in os.listdir(pdf_resume_directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_resume_directory, filename)
            resume_text = extract_text_from_pdf(pdf_path)
            similarity = calculate_similarity(sample_resume, resume_text)
            if similarity > highest_similarity:
                highest_similarity = similarity
                most_compatible_resume = os.path.splitext(filename)[0]

    # Normalize the similarity score to a scale of 0 to 100
    compatibility_score_normalized = (highest_similarity + 1) * 50

    return most_compatible_resume, compatibility_score_normalized

# Example usage:
# result = predictss(paths, preference)
# print("Most compatible resume:", result[0])
# print("Compatibility score:", result[1])

