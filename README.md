
# Axur Internship Technical Evaluation

## 🕸️ Web Scraping with Python & BeautifulSoup + API Integration

This project performs web scraping on a given page to extract images, and sends the first image to a machine learning model API for inference. The result is then automatically submitted to a verification endpoint.

---

## ✅ Prerequisites

- [Python 3](https://www.python.org/downloads/) installed
- `pip` (Python package manager)

---

## ⚙️ Setup Instructions

### 1. Clone the project and create a virtual environment

```bash
python -m venv venv
```

### 2. Activate the virtual environment

On **Linux/macOS**:
```bash
source venv/bin/activate
```

On **Windows (CMD)**:
```cmd
venv\Scripts\activate
```

On **Windows (PowerShell)**:
```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install beautifulsoup4 requests python-dotenv
```

### 4. Set your API token

Create a `.env` file in the root of the project and add your token:

```
AXUR_API_TOKEN=your_api_token_here
```

---

## 🚀 Running the Script

With the virtual environment activated and the `.env` file set, run:

```bash
python main.py
```

This will:

1. Scrape all `<img>` elements from the specified page.
2. Save them in the `extracted_images/` directory.
3. Send the first image (base64) to the model `microsoft-florence-2-large` using the prompt `<DETAILED_CAPTION>`.
4. Submit the model's raw response to the validation endpoint.

---

## 📄 Notes

- The image sent to the model is encoded as base64 and embedded in the OpenAI-style payload.
- All requests follow the expected headers and structure for authorization and content-type.
- Make sure the token is valid; otherwise, the script will raise an authentication error.

---
