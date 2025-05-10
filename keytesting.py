import openai

# Test if the API key is working by making a simple completion request
openai.api_key = "your openai API key"

try:
    # Try a simple completion to test the API key
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Say 'Hello' if you can read this."}
        ]
    )
    print("API Key is working! Response:", response.choices[0].message.content)
except Exception as e:
    print(f"API Key error: {e}")
