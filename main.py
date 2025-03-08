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
    # Remove header elements
    for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        header.decompose()
    # Extract text and remove extra lines
    text = '\n'.join([line.strip() for line in soup.get_text().split('\n') if line.strip()])
    return text.strip()

# Function to extract questions using regex and DistilBERT
def extract_questions(text):
    # Look for lines starting with "Example" followed by a number and potential text
    example_pattern = r'Example\s+\d+\s*(.+?)(?=Solution|Example|\Z)'
    examples = re.findall(example_pattern, text, re.DOTALL)
    
    questions = []
    for example in examples:
        # Clean up the example text
        clean_example = example.strip()
        
        # Extract the actual operation being performed
        if "Add" in clean_example:
            # Extract the numbers being added
            numbers = re.findall(r'\$\\frac{[^}]+}{[^}]+}\$', clean_example)
            if len(numbers) >= 2:
                question = f"How do you add the fractions {numbers[0]} and {numbers[1]}?"
                questions.append(question)
    
    # Also look for direct questions (those ending with ?)
    direct_questions = re.findall(r'[^.!?]*\?', text)
    questions.extend([q.strip() for q in direct_questions if q.strip()])
    
    # Remove duplicates while preserving order
    seen = set()
    return [q for q in questions if not (q in seen or seen.add(q))]

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
