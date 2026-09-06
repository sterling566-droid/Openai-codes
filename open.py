from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="your openrouter api key"
)

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
      {"role":"system","content":"models personality"},
        {"role": "user", "content":"generate a image of a dog"}
    ]
)

print(response.choices[0].message.content)
