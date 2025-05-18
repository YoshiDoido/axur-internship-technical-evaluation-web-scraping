
# Axur Internship Technical Evaluation

## 🕸️ Web Scraping with Python & BeautifulSoup

This project demonstrates a simple web scraping task using Python and the BeautifulSoup library. It was developed as part of the Axur internship technical evaluation.

---

## ✅ Prerequisites

- [Python 3](https://www.python.org/downloads/) installed
- `pip` (Python package manager)

---

## ⚙️ Setup Instructions

### 1. Create a virtual environment

Run this command in the root directory of the project:

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

With the virtual environment active, run:

```bash
pip install beautifulsoup4 requests
```

---

## 🚀 Running the Script

Make sure you're inside the virtual environment. Then run:

```bash
python main.py
```

The script will scrape the target web page and save the embedded image as a local file named `extracted_image.jpg`.

---

## 📄 Notes

- All scraping was done using the `requests` and `beautifulsoup4` libraries.
- The image is embedded in base64 format and is extracted directly from the `img` tag.

---
