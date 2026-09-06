from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
      {"role":"system","content":"Your name is Sterling you are Mr.Sterling's personal assistant he is 16yrs and he us a Ghanian Address him as Mr.Sterling.."},
        {"role": "user", "content":"generate a image of a dog"}
    ]
)

print(response.choices[0].message.content)