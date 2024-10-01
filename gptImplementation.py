import os
# imports for the ai
from openai import OpenAI
from dotenv import load_dotenv

#imports for the main initalization
import argparse

load_dotenv()

# This is the openai client configuration
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


# Below is configuring the prompt you want to send GPT 3
def useGPT(argument):
    prompt = f"Give me a random sentence containing {argument} words"
    response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
    )

    return response.choices[0].message.content


# 2) This is the main function that takes retrieves inputs using argparse library
# The argument is then passed into gpt to get a response
def main():
    print("Entry Point Configured")

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    userInput = args.input

    print(useGPT(userInput))

    pass


# 1) This is what sets the entry points
# When the app is ran as 'python gptImplementation.py' for example, 
# the var __name__ is auto'd to __main__, so we can check then and execute functions from it
if __name__ == "__main__":
    main()
