from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Test the summarizer
text = "The capital of France is Paris. It is known for its beautiful architecture and rich history."
summary = summarizer(text, max_length=130, min_length=30, do_sample=False)

print(summary)
