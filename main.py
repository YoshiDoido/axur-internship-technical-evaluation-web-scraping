import requests
from bs4 import BeautifulSoup
import base64

# Page URL
url = "https://intern.aiaxuropenings.com/scrape/2e18e893-6e15-4e15-a1c9-fd230e7ea84a"

# HTTP Request to get the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find an <img> tag with base64
img_tag = soup.find("img", {"src": lambda x: x and x.startswith("data:image/jpeg;base64,")})
img_base64 = img_tag['src'].split(',')[1]

# Decoding and saving the file as a jpg
image_data = base64.b64decode(img_base64)
with open("extracted_image.jpg", "wb") as f:
    f.write(image_data)

print("Image saved as extracted_image.jpg")
