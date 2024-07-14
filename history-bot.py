import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.dev")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

persona = input("Hãy cho tôi biết nhân vật lịch sử bạn muốn tôi đóng vai: ")
question = input("Hãy hỏi câu hỏi của bạn về nhân vật lịch sử này: ")
prompt = f"""
Bạn sẽ đóng vai một nhân vật lịch sử {persona}.

Mỗi khi được hỏi một số câu hỏi nhất định, bạn cần nhớ các sự kiện và thông tin về thời gian xảy ra và chỉ trả lời chính xác. Đừng tự tạo nội dung. Nếu bạn không nhớ điều gì đó, hãy nói rằng bạn không nhớ.

Hãy cung cấp câu trả lời cho câu hỏi: {question}
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt},
    ],
    temperature=0
)

print(response.choices[0].message.content)