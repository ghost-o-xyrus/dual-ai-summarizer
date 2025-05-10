# dual-ai-summarizer
Transform any text into multiple summary formats using state-of-the-art AI models. Choose between OpenAI's GPT or Hugging Face's BART for different summarization styles. Includes concise, detailed, key points, and technical summaries. Easy to use, highly configurable, and perfect for content analysis.
<<<<<<< HEAD
# AI Text Summarizer

A powerful text summarization tool that supports both OpenAI's GPT models and Hugging Face's BART model for generating multiple types of summaries from any text file.

## Features

- Multiple summary types:
  - Concise Summary
  - Detailed Summary
  - Key Points Summary
  - Technical Summary
- Support for both OpenAI GPT and Hugging Face BART models
- Command-line interface for easy usage
- Automatic output organization in a dedicated folder

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Hugging Face token

## Getting API Keys

### OpenAI API Key
1. Go to [OpenAI's website](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to API keys section
4. Create a new API key
5. Copy the key and keep it secure

### Hugging Face Token
1. Go to [Hugging Face](https://huggingface.co/)
2. Sign up or log in to your account
3. Go to Settings -> Access Tokens
4. Create a new token with read access
5. Copy the token and keep it secure

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-text-summarizer.git
cd ai-text-summarizer
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure your API keys:
   - Open `OPAIsumAPImain.py` and replace `"your openai API key"` with your OpenAI API key
   - Open `tokenlogin.py` and replace `"your hugging face token ID"` with your Hugging Face token

## Usage

### Using OpenAI Summarizer
```bash
python OPAIsumAPImain.py path/to/your/article.txt
```

### Using Hugging Face Summarizer
```bash
python HFsumAPImain.py path/to/your/article.txt
```

The summaries will be saved in the `Summaries_OPAIsumAPI` folder with the format:
- OpenAI: `[filename]_summary_OPAIsumAPI.txt`
- Hugging Face: `[filename]_summary_HF.txt`

## Output Format

Each summary file contains four different types of summaries:
1. Concise Summary - A brief overview
2. Detailed Summary - A comprehensive version
3. Key Points Summary - Main ideas and concepts
4. Technical Summary - More formal and structured version

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for their GPT models
- Hugging Face for their BART model and transformers library 
=======
# dual-ai-summarizer
Transform any text into multiple summary formats using state-of-the-art AI models. Choose between OpenAI's GPT or Hugging Face's BART for different summarization styles. Includes concise, detailed, key points, and technical summaries. Easy to use, highly configurable, and perfect for content analysis.
>>>>>>> 388308fb07468d983899549aa6460220eb2c25a6
