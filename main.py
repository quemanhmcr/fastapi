from fastapi import FastAPI

app = FastAPI()

"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os
import time

import google.generativeai as genai

import requests


genai.configure(api_key="AIzaSyCbhcCCaoX7JdOlyh_-S87-c86IuPWdmf4")




def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """



  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

def wait_for_files_active(files):
  """Waits for the given files to be active.

  Some files uploaded to the Gemini API need to be processed before they can be
  used as prompt inputs. The status can be seen by querying the file's "state"
  field.

  This implementation uses a simple blocking polling loop. Production code
  should probably employ a more sophisticated approach.
  """
  print("Waiting for file processing...")
  for name in (file.name for file in files):
    file = genai.get_file(name)
    while file.state.name == "PROCESSING":
      print(".", end="", flush=True)
      time.sleep(10)
      file = genai.get_file(name)
    if file.state.name != "ACTIVE":
      raise Exception(f"File {file.name} failed to process")
  print("...all files ready")
  print()

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-exp-0801",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

# TODO Make these files available on the local file system
# You may need to update the file paths
files = [
  
]

videos = ["https://res.cloudinary.com/dqneghcme/video/upload/v1722732230/gemini/s88ebzwrf6n1l9n8mrea.mp4"]

for video in videos:
  response = requests.get(video)
  filename = video.split("/")[-1]
  with open(filename, "wb") as f:
    f.write(response.content)
  
  files.append(upload_to_gemini(filename, mime_type="video/mp4"))

# Some files have a processing delay. Wait for them to be ready.
wait_for_files_active(files)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        files[0],
      ],
    },
    {
      "role": "user",
      "parts": [
        "Phan tich video nay",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Video này có cảnh nam diễn viên Nicolas Cage đang đeo tai nghe và ngồi trước micrô. Dường như anh ấy đang ở trong một phòng thu âm tại nhà hoặc phòng thu nhỏ. Anh ấy nhìn xuống một thứ gì đó ngoài màn hình, có lẽ là một kịch bản hoặc lời bài hát, và thỉnh thoảng ngước lên, có vẻ như đang suy nghĩ hoặc tập trung.\n \n Anh ấy dường như đang chuẩn bị để thu âm giọng nói, có thể là cho một bộ phim, trò chơi điện tử hoặc dự án âm thanh khác. Biểu cảm trên khuôn mặt anh ấy cho thấy anh ấy đang tập trung và nghiêm túc với công việc của mình.\n \n Có một số chi tiết thú vị trong video, chẳng hạn như ánh sáng màu tím phát ra từ tai nghe của anh ấy và micrô chuyên nghiệp anh ấy đang sử dụng. Những chi tiết này góp phần tạo nên bầu không khí của video và gợi ý rằng đây là một bản thu âm chuyên nghiệp.\n \n Nhìn chung, đây là một video đơn giản nhưng hấp dẫn ghi lại Nicolas Cage trong một khoảnh khắc làm việc. Nó cho thấy một cái nhìn thoáng qua về quá trình sáng tạo đằng sau các buổi thu âm giọng nói và sự tập trung mà Cage dành cho nghề nghiệp của mình.\n",
      ],
    },
  ]
)

@app.get("/")
async def root(input_string: str):
    response = chat_session.send_message(input_string).text
    return {"message": response}
