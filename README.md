# 📧 Email Extractor API

A simple REST API built with **FastAPI** to extract email addresses from any public webpage URL using `requests`, `BeautifulSoup`, and regex. Deployed on [Render](https://render.com).

## 🚀 Live API Endpoint

GET https://email-extractor-0oyz.onrender.com/extract-emails?url=https://example.com

yaml
Copy
Edit

---

## 🔍 How It Works

This API accepts a webpage URL, scrapes its textual content, and extracts all valid email addresses using regex. It removes scripts and styles before parsing to avoid noise.

---

## 📦 Tech Stack

- **FastAPI** (Python)
- **BeautifulSoup4**
- **Regex (re module)**
- **CORS Middleware**
- **Hosted on Render**

---

## 📥 Installation & Local Development

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/email-extractor-api.git
cd email-extractor-api
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the FastAPI server locally:**

```bash
uvicorn main:app --reload
```

4. **Test the API locally:**

```bash
curl "http://127.0.0.1:8000/extract-emails?url=https://example.com"
```

## 🌐 CORS Configuration

The API allows frontend apps to make cross-origin requests from:

```python

allow_origins = [
"https://email-extractor-ui.vercel.app",
"http://localhost:3000"
]
```

Make sure your frontend is hosted on one of these origins.

## 🧪 Example Response

Request:

```http

GET /extract-emails?url=https://www.cogentlabs.co/
```

Response:

```json
{
  "emails": ["hello@cogentlabs.co", "contact@cogentlabs.co"]
}
```

## 📁 Project Structure

```bash

.
├── main.py # FastAPI app with email extraction logic
├── requirements.txt # Python dependencies
└── README.md # You're here :)
```

## 🛡️ Security & Limits

- ✅ URL validation using pydantic.HttpUrl

- ⚠️ Does not crawl beyond the provided URL (no deep scraping)

- ❌ Does not execute JavaScript (no JS-rendered emails)

## 📤 Deployment

This app is deployed via Render.com. Simply push updates to your GitHub repo, and Render will redeploy automatically.

## 🧠 Future Improvements

- Email deduplication across domains

- Support for mailto: links

- POST endpoint for raw HTML input

- Rate limiting & abuse protection

## 📄 License

MIT License. Feel free to use, modify, and deploy.

## 👨‍💻 Author

Developed by Muhammad Haris Ejaz

- GitHub: [@haris-75](https://github.com/haris-75)

- Frontend Repo: [email-extractor-ui](https://github.com/haris-75/email-extractor-ui)
