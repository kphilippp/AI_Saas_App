import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# This is the openai client configuration
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


# Below is configuring the prompt you want to send GPT 3
numberOfWords = "15"
prompt = f"Give me a random sentence containing {numberOfWords} words"

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
)

print(response.choices[0].message.content)