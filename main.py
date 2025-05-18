import os
import requests
from bs4 import BeautifulSoup
import base64
from urllib.parse import urljoin

# Page URL
url = "https://intern.aiaxuropenings.com/scrape/2e18e893-6e15-4e15-a1c9-fd230e7ea84a"

# HTTP Request to get the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Create a file directory if it doesn't exist
output_dir = "extracted_images"
os.makedirs(output_dir, exist_ok=True)

# Find all <img> tags
img_tags = soup.find_all("img")

# Process and save all images
for idx, img in enumerate(img_tags, start=1):
    src = img.get("src")
    if not src:
        continue

    filename = f"extracted_image{idx:02}.jpg"
    filepath = os.path.join(output_dir, filename)

    if src.startswith("data:image/jpeg;base64,"):
        # base64 image
        base64_data = src.split(",")[1]
        img_bytes = base64.b64decode(base64_data)
    else:
        # Imagem por URL
        full_url = urljoin(url, src)
        img_response = requests.get(full_url)
        img_bytes = img_response.content

    with open(filepath, "wb") as f:
        f.write(img_bytes)

    print(f"Saved image as {filepath}")
