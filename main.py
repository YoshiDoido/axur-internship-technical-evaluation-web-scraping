import os
import requests
from bs4 import BeautifulSoup
import base64
from urllib.parse import urljoin
from dotenv import load_dotenv


# Load .env and verify user token
load_dotenv()   # pip install python-dotenv
TOKEN = os.getenv("AXUR_API_TOKEN")
if not TOKEN:
    raise RuntimeError("⚠️ AXUR_API_TOKEN wasn't loaded properly. Please check your .env or environment variables.")
print("✔️ Token carregado:", TOKEN[:4] + "…" )

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type":  "application/json"
}


# --- Configs ---
PAGE_URL    = "https://intern.aiaxuropenings.com/scrape/2e18e893-6e15-4e15-a1c9-fd230e7ea84a"
API_URL     = "https://intern.aiaxuropenings.com/v1/chat/completions"
SUBMIT_URL  = "https://intern.aiaxuropenings.com/api/submit-response"
MODEL       = "microsoft-florence-2-large"
PROMPT_TAG  = "<DETAILED_CAPTION>"
TOKEN       = os.getenv("AXUR_API_TOKEN")


# --- 1) Scraping and all image downloads ---
resp = requests.get(PAGE_URL)
resp.raise_for_status()
soup = BeautifulSoup(resp.text, "html.parser")

output_dir = "extracted_images"
os.makedirs(output_dir, exist_ok=True)

img_tags = soup.find_all("img")
saved_files = []

for idx, img in enumerate(img_tags, start=1):
    src = img.get("src")
    if not src:
        continue

    filename = f"extracted_image{idx:02}.jpg"
    filepath = os.path.join(output_dir, filename)

    if src.startswith("data:image/"):
        # base64
        b64_data = src.split(",", 1)[1]
        img_bytes = base64.b64decode(b64_data)
        saved_files.append((filepath, b64_data))
    else:
        # Absolute URL or relative
        full_url = urljoin(PAGE_URL, src)
        img_bytes = requests.get(full_url).content
        # encode to base64 for later use in interference
        saved_files.append((filepath, base64.b64encode(img_bytes).decode()))

    with open(filepath, "wb") as f:
        f.write(img_bytes)

    print(f"✓ Saved image: {filepath}")

# --- 2) Interference using only the first image ---
first_path, first_b64 = saved_files[0]
img_markdown = f"data:image/jpeg;base64,{first_b64}"

payload = {
    "model": MODEL,
    "messages": [
        {
            "role": "user",
            "content": [
                { "type": "text", "text": PROMPT_TAG },
                { "type": "image_url", "image_url": { "url": img_markdown } }
            ]
        }
    ]
}


resp_api = requests.post(API_URL, json=payload, headers=HEADERS)
resp_api.raise_for_status()
result_json = resp_api.json()
print("✓ Received response from model")

# --- 3) Sending Raw JSON ---
resp_submit = requests.post(SUBMIT_URL, json=result_json, headers=HEADERS)
resp_submit.raise_for_status()
print(f"✓ Submission successful (status: {resp_submit.status_code})")
