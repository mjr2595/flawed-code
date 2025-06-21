import os
import sys

from dotenv import load_dotenv
from google import genai

if len(sys.argv) != 2:
    print("Usage: python main.py <prompt>")
    sys.exit(1)

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY environment variable is not set.")
    sys.exit(1)

client = genai.Client(api_key=api_key)
model = "gemini-2.0-flash-001"
prompt = sys.argv[1]

response = client.models.generate_content(model=model, contents=prompt)

print("\nModel's response:")
print(response.text)

print("\nToken usage:")
if response.usage_metadata is not None:
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
else:
    print("Token usage metadata is not available.")
