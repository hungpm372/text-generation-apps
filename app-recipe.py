from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv(dotenv_path=".env.dev")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

no_movies = input("Số lượng phim được đề xuất (ví dụ: 5): ")
genres = input("Thể loại phim yêu thích (ví dụ: hành động, hài, drama): ")
actors = input("Diễn viên yêu thích (ví dụ: Tom Hanks, Meryl Streep): ")

prompt = f"Hãy cho tôi {no_movies} đề xuất phim trong các thể loại: {genres}, với sự góp mặt của các diễn viên sau: {actors}. Đối với mỗi bộ phim, hãy cung cấp một bản tóm tắt ngắn gọn và danh sách diễn viên chính: "
messages = [{"role": "user", "content": prompt}]

completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages, max_tokens=600, temperature=0.1)

print("Đề xuất phim:")
print(completion.choices[0].message.content)

old_prompt_result = completion.choices[0].message.content
prompt_watchlist = "Hãy gợi ý một vài bộ phim dựa trên các đề xuất phim này: "

new_prompt = f"Dựa trên các đề xuất phim này: {old_prompt_result}, {prompt_watchlist}"
messages = [{"role": "user", "content": new_prompt}]
completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages, max_tokens=600, temperature=0)

print("\n=====Danh sách xem ======= \n")
print(completion.choices[0].message.content)
