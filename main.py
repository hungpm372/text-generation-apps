import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.dev")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

topic = input("Nhập chủ đề bạn muốn viết về: ")
length = int(input("Nhập độ dài mong muốn của bài viết (tính bằng số từ): "))

prompt = f"Hãy viết một bài viết với độ dài khoảng {length} từ về chủ đề '{topic}'."

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt},
    ],
    temperature=1
)

print(response.choices[0].message.content)
