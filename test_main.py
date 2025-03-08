import pytest
from unittest.mock import mock_open, patch
from main import load_markdown, extract_questions, save_questions

# Test for loading markdown file
@patch('builtins.open', new_callable=mock_open, read_data='## Sample Markdown\nThis is a sample question?\n')
def test_load_markdown(mock_file):
    result = load_markdown('dummy_path.md')
    assert result == 'This is a sample question?'

# Test for loading empty markdown file
@patch('builtins.open', new_callable=mock_open, read_data='')
def test_load_empty_markdown(mock_file):
    result = load_markdown('empty_path.md')
    assert result == ''

# Test for extracting questions
def test_extract_questions():
    text = 'This is a sample question? And this is not a question.'
    questions = extract_questions(text)
    assert questions == ['This is a sample question?']

# Test for extracting questions from text without questions
def test_extract_questions_no_questions():
    text = 'This is a statement. And this is another statement.'
    questions = extract_questions(text)
    assert questions == []

# Test for saving questions
@patch('builtins.open', new_callable=mock_open)
def test_save_questions(mock_file):
    questions = ['What is Python?', 'How to use pytest?']
    save_questions(questions, 'dummy_output.txt')
    mock_file().write.assert_any_call('What is Python?\n')
    mock_file().write.assert_any_call('How to use pytest?\n')

# Test for saving an empty list of questions
@patch('builtins.open', new_callable=mock_open)
def test_save_empty_questions(mock_file):
    questions = []
    save_questions(questions, 'empty_output.txt')
    mock_file().write.assert_not_called()
