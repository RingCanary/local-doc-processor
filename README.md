# local-doc-processor

## Question Extraction from Markdown Files

This project aims to extract questions from markdown files, particularly those containing mathematical content. The extracted questions can be used for educational purposes, such as creating practice problems or assessments.

### Features

- **Question Extraction**: Identifies and extracts questions from markdown files using natural language processing techniques.
- **Efficient Models**: Utilizes spaCy and DistilBERT to ensure the solution runs efficiently on machines with limited resources.
- **Customizable**: Easily adaptable to different types of text files and extraction criteria.

### Requirements

- Python 3.7 or higher
- Libraries: `spacy`, `transformers`, `torch`, `markdown`, `beautifulsoup4`

### Setup

1. **Install Dependencies**:
   ```bash
   pip install spacy transformers torch markdown beautifulsoup4
   ```

2. **Download spaCy Model**:
   ```bash
   python -m spacy download en_core_web_sm
   ```

### Usage

1. **Prepare Your Markdown File**: Ensure your markdown file (e.g., `math_workbook.md`) is in the same directory as the script or provide the full path.

2. **Run the Script**:
   ```bash
   python main.py
   ```

3. **Output**: The extracted questions will be saved in `extracted_questions.txt`.

### TODO List

- [ ] **Improve Question Filtering**: Enhance the filtering mechanism to reduce false positives in question extraction.
- [ ] **Add Configuration File**: Allow users to configure extraction parameters via a configuration file.
- [ ] **Support for Multiple File Formats**: Extend the functionality to support other file formats like PDF and DOCX.
- [ ] **GUI Interface**: Develop a simple graphical user interface for easier interaction.
- [ ] **Unit Tests**: Write unit tests to ensure the reliability of the question extraction process.
- [ ] **Optimize Performance**: Further optimize the code for better performance on large files.
- [ ] **Documentation**: Improve documentation with examples and detailed explanations of the code.
- [ ] **Error Handling**: Implement robust error handling to manage exceptions and edge cases.

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Contact

For any questions or suggestions, please open an issue or contact the maintainers directly.


### Explanation

- **Features**: Highlights the key functionalities of the project.
- **Requirements**: Lists the necessary dependencies and their installation commands.
- **Usage**: Provides step-by-step instructions on how to use the script.
- **TODO List**: Outlines future improvements and features to be implemented.
- **Contributing and License**: Encourages contributions and specifies the licensing details.