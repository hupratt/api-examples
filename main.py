import requests, os
from dotenv import load_dotenv


load_dotenv()

headers = {
  'Authorization': os.getenv("API_KEY")
}

# change to a full file path of the image you want to transform
body = {
  'contentImage': '@/Users/porky/pig.jpg',
  'styleImage': '@/Users/porky/funky.jpg',
  'focusContent': 'true'
}

response = requests.post('https://api.hotpot.ai/remix-art', headers=headers, files=body)

# change to a full file path where you want to save the resulting image
with open('art.jpg', 'wb') as file:
  file.write(response.content)

print("done")