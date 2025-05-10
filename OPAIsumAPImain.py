import openai
import os
import sys

# Set up OpenAI client with your key
openai.api_key = "your openai API key"

# Get article path from command line
if len(sys.argv) < 2:
    print("Usage: python OPAIsumAPI.py path/to/article.txt")
    sys.exit(1)

article_path = sys.argv[1]

# Read the article
with open(article_path, "r", encoding="utf-8") as file:
    article_text = file.read()

# Create summaries folder and output file
output_folder = "Summaries_OPAIsumAPI"
os.makedirs(output_folder, exist_ok=True)

article_filename = os.path.splitext(os.path.basename(article_path))[0]
output_filename = f"{article_filename}_summary_OPAIsumAPI.txt"
output_path = os.path.join(output_folder, output_filename)

# Define tones and initialize storage
tones = ["casual", "formal", "academic"]
all_summaries = []

# Loop through tones and generate summary
for tone in tones:
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Summarize the following article in a {tone} tone."},
                {"role": "user", "content": article_text}
            ]
        )
        summary = response.choices[0].message.content
        all_summaries.append(f"--- {tone.capitalize()} Summary ---\n{summary}\n")
    except Exception as e:
        print(f"Error generating {tone} summary: {e}")
        continue

# Save to file
with open(output_path, "w", encoding="utf-8") as out_file:
    out_file.write("\n".join(all_summaries))

print(f"\n✅ Summaries saved to: {output_path}")