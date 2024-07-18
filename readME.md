# Recruitment Analysis Tool

This project is a recruitment analysis tool that uses OpenAI's GPT-3.5 to evaluate candidate resumes against job descriptions. It extracts text from PDF files, generates evaluation prompts, and outputs an analysis of the candidate's qualifications.

## Table of Contents

- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

- Extract text from PDF files (job descriptions and candidate resumes)
- Generate evaluation prompts for recruitment analysis
- Use OpenAI's GPT-3.5 to evaluate and score candidate resumes
- Display analysis results in a Streamlit web application

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- Virtual environment tool (e.g., `venv` or `virtualenv`)

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/recruitment_analysis_tool.git
    cd recruitment_analysis_tool
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv myenv
    source myenv/bin/activate  # On macOS/Linux
    .\myenv\Scripts\activate  # On Windows
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Set up your OpenAI API key**:
    - Obtain your API key from the [OpenAI website](https://beta.openai.com/signup/).

2. **Run the Streamlit app**:
    ```sh
    streamlit run app.py
    ```

3. **Interact with the application**:
    - Enter your OpenAI API key in the provided text box.
    - Upload the job description PDF file.
    - Upload the candidate resume PDF file.
    - View the recruitment analysis results.

## Project Structure

    recruitment_analysis_tool/
    │
    ├── src/
    │ ├── init.py
    │ ├── pdf_processing.py
    │ └── recruit_ai.py
    │
    ├── app.py
    ├── requirements.txt
    └── README.md

    - `src/`: Contains the source code for PDF processing and recruitment analysis.
    - `pdf_processing.py`: Contains functions to extract text from PDF files.
    - `recruit_ai.py`: Contains the `RecruitAI` class for generating prompts and interacting with OpenAI's API.
    - `app.py`: The main Streamlit application.
    - `requirements.txt`: Lists the Python dependencies for the project.
    - `README.md`: Project documentation.

## Dependencies

- `streamlit`: Web application framework for Python.
- `openai`: OpenAI API client library.
- `PyPDF2`: Library for reading PDF files.
- `fpdf`: Library for creating PDF files.
- `tiktoken`: Tokenizer for counting tokens in text.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.
