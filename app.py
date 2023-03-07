import openai
openai.api_key = "xxxxxxxxxxxxxxxx"

output = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "who is the president of india in 2015"}])

# Get the output text only
print(output['choices'][0]['message']['content'])
