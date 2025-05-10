import os
import sys
from transformers import pipeline

def create_summaries(text, summarizer):
    summaries = []
    
    # 1. Concise Summary (short and to the point)
    concise = summarizer(text, max_length=100, min_length=30, do_sample=False)
    summaries.append("--- Concise Summary ---\n" + concise[0]['summary_text'] + "\n")
    
    # 2. Detailed Summary (more comprehensive)
    detailed = summarizer(text, max_length=200, min_length=100, do_sample=False)
    summaries.append("--- Detailed Summary ---\n" + detailed[0]['summary_text'] + "\n")
    
    # 3. Key Points Summary (focusing on main ideas)
    key_points = summarizer(text, max_length=150, min_length=50, do_sample=False)
    summaries.append("--- Key Points Summary ---\n" + key_points[0]['summary_text'] + "\n")
    
    # 4. Technical Summary (more formal and structured)
    technical = summarizer(text, max_length=180, min_length=80, do_sample=False)
    summaries.append("--- Technical Summary ---\n" + technical[0]['summary_text'] + "\n")
    
    return summaries

def main():
    # Check if file path is provided
    if len(sys.argv) < 2:
        print("Usage: python HFsumAPImain.py path/to/article.txt")
        sys.exit(1)

    # Get the article path from command line
    article_path = sys.argv[1]

    # Create summaries folder if it doesn't exist
    output_folder = "Summaries_OPAIsumAPI"
    os.makedirs(output_folder, exist_ok=True)

    # Read the article
    try:
        with open(article_path, "r", encoding="utf-8") as file:
            article_text = file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    # Load the summarization model
    print("Loading BART summarization model...")
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    print("Model loaded successfully!")

    # Generate summaries
    print("Generating summaries...")
    summaries = create_summaries(article_text, summarizer)

    # Create output filename
    article_filename = os.path.splitext(os.path.basename(article_path))[0]
    output_filename = f"{article_filename}_summary_HF.txt"
    output_path = os.path.join(output_folder, output_filename)

    # Save summaries to file
    with open(output_path, "w", encoding="utf-8") as out_file:
        out_file.write("\n".join(summaries))

    print(f"\n✅ Summaries saved to: {output_path}")

if __name__ == "__main__":
    main()
