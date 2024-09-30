from openai import OpenAI

client = OpenAI(api_key='your-api-key')

  # You need to replace 'your-api-key' with your actual OpenAI API key

completion = client.chat.completions.create(model="gpt-4",  # 'gpt-4o-mini' doesn't exist, so you can use 'gpt-4' or 'gpt-3.5-turbo'
messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Write a haiku about recursion in programming."}
])

print(completion.choices[0].message.content)
