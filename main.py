import re
import spacy
import markdown
from bs4 import BeautifulSoup
from transformers import pipeline, DistilBertTokenizer, DistilBertForQuestionAnswering
import torch

# Load spaCy model for NER
nlp = spacy.load("en_core_web_sm")

# Load DistilBERT model and tokenizer for question extraction
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertForQuestionAnswering.from_pretrained('distilbert-base-uncased')

# Function to load and parse the markdown file
def load_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    html = markdown.markdown(content)
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()

# Function to extract questions using regex and DistilBERT
def extract_questions(text):
    # Use spaCy to identify potential questions
    doc = nlp(text)
    potential_questions = [sent.text for sent in doc.sents if sent.text.strip().endswith('?')]

    # Further filter using DistilBERT
    questions = []
    for sentence in potential_questions:
        inputs = tokenizer(sentence, return_tensors='pt', truncation=True, padding=True)
        with torch.no_grad():
            outputs = model(**inputs)
        start_scores = outputs.start_logits
        end_scores = outputs.end_logits

        # Check if the sentence is a valid question based on scores
        if torch.max(start_scores) > 0.5 and torch.max(end_scores) > 0.5:
            questions.append(sentence)

    return questions

# Function to save the extracted questions
def save_questions(questions, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for question in questions:
            file.write(question + '\n')

# Example usage
markdown_file = 'math_workbook.md'
output_file = 'extracted_questions.txt'

print("Loading markdown file...")
text = load_markdown(markdown_file)

print("Extracting questions...")
questions = extract_questions(text)

print("Saving extracted questions...")
save_questions(questions, output_file)

print(f"Extracted questions saved to '{output_file}'")
