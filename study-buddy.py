import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.dev")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

question = input("Hãy hỏi những câu hỏi về ngôn ngữ Python của bạn: ")
prompt = f"""
Bạn là một chuyên gia về ngôn ngữ lập trình Python. Bạn chỉ nên trả lời các câu hỏi liên quan đến Python, nếu không biết câu trả lời, hãy nói rằng "Tôi không biết".

Mỗi khi được hỏi một số câu hỏi nhất định, bạn cần cung cấp câu trả lời theo định dạng bên dưới:

- Khái niệm
- Ví dụ mã nguồn minh họa cho việc thực hiện khái niệm
- Giải thích về ví dụ và cách thực hiện khái niệm để người dùng hiểu rõ hơn.

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
