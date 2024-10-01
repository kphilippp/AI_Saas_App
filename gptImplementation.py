import os
from typing import List
# imports for the ai
from openai import OpenAI
from dotenv import load_dotenv

#imports for the main initalization argument parsing
import argparse

#imports to configure response messages from gpt
import re


# Description
# currently what this does is take user input in main function
# then it passes than to validateInput to make sure its not too long
# then it passes the input to getBrandingSnippet to get a branding snipper
# then it passes it to getKeywords to get a list of the keywords

load_dotenv()



MAX_INPUT_LENGTH = 20


# This is the openai client configuration
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


# Below is configuring the prompt you want to send GPT 3
def getBrandingSnippet(argument: str) -> str:
    prompt = f"Generate a branding snippet for {argument}"
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

# function makes eywords from the branding snippet
def getKeywords(argument: str) -> List[str]:
    prompt = f"Generate at least 5 single branding keywords pertaing to this snippet: {argument}"
    response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
    )

    keywordsString = response.choices[0].message.content

    # delimit the words
    delimiter = ",|\n|;|-|[1-9]."
    keywords = re.split(delimiter, keywordsString)
    keywords = [k.lower().strip() for k in keywords]
    keywords = [k for k in keywords if len(k) > 0]

    return keywords

# function makes sure the input is not too long, safes us from wasting credits and protects us from malicious GPT usage
def validateInput(input: str) -> bool:
    if (len(input) >= MAX_INPUT_LENGTH):
        return False
    return True

# 2) This is the main function that takes retrieves inputs using argparse library
# The argument is then passed into gpt to get a response
def main():
    print("Entry Point Configured")

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    userInput = args.input
    print ("INPUT : " + userInput)

    if validateInput(userInput):
        brandingSnippet = getBrandingSnippet(userInput)
        brandingKeywords = getKeywords(brandingSnippet)
        print("\nBranding Snippet: " + brandingSnippet)
        for word in brandingKeywords:
            print("\nKey Words: " + word + ", ")
    else:
        raise ValueError("Input is greater than {MAX_INPUT_LENGTH} characters, please validate input") 
    pass


# 1) This is what sets the entry points
# When the app is ran as 'python gptImplementation.py' for example, 
# the var __name__ is auto'd to __main__, so we can check then and execute functions from it
if __name__ == "__main__":
    main()
