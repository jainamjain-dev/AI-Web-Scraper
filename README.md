# 🕸️ AI Web Scraper

An intelligent web scraping tool powered by **LLMs** (Locally hosted via Ollama) to extract meaningful and structured information from websites using natural language prompts.

---

## 🚀 Tech Stack

- [Streamlit](https://streamlit.io/) — Web frontend for user interaction  
- [LangChain](https://www.langchain.com/) — LLM orchestration  
- [langchain_ollama](https://python.langchain.com/docs/integrations/llms/ollama) — LLM integration via Ollama  
- [Selenium](https://www.selenium.dev/) — Web automation and scraping  
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) — DOM parsing  
- `lxml` and `html5lib` — HTML parsers  
- `python-dotenv` — Environment variable management

---

## 🧠 Why AI Web Scraping?

Traditional web scraping is fragile — HTML structure changes often, making hardcoded scrapers break easily. This project solves that by:

- Letting you **describe what you want in natural language**
- Parsing **complex or dynamic sites** using a real browser (Selenium)
- Using **LLMs (like LLaMA 3)** locally to extract content based on your prompt
- Handling **captcha/IP blocks** with optional **Bright Data's Scraping Browser**

This enables **flexible, adaptable scraping** even on JavaScript-heavy or protected websites.

---

## ⚙️ How It Works

1. User enters a URL into the **Streamlit UI**
2. The backend uses **Selenium + chromedriver** to scrape the site’s content
3. If blocked or facing captchas, **Bright Data's Scraping Browser** can be used
4. The raw HTML is cleaned with **BeautifulSoup**
5. The HTML is chunked and passed to a **local LLM via LangChain/Ollama**
6. The model extracts exactly what’s requested via prompt

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-web-scraper.git
cd ai-web-scraper
```
## 2 .Install Python Dependencies
Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```
## Install dependencies:
```bash
pip install -r requirements.txt
```

## 3. Install & Set Up Ollama
Download and install Ollama from: https://ollama.com
Then pull the LLaMA model (or another supported one):
```bash
ollama pull llama3
```

## 4. Add Environment Variables (Optional)
If using Bright Data, create a .env file:
```bash
SBR_WEBDRIVER=https://your-brightdata-webdriver-endpoint
```
## See their docs: https://brightdata.com/products/scraping-browser
## 5.  Run the Application
```bash
streamlit run app.py
```
## 💡 Features
# ✅ Works with both static & dynamic pages
# ✅ Robust against structural changes in websites
# ✅ Language-model-powered parsing
# ✅ Optional captcha/IP bypass with Bright Data
# ✅ Fully local — no API key needed if using Ollama

## 🔐 Handling Protected Sites
# If a website has strong anti-bot protections (e.g., captchas, IP bans), enable the Bright Data method (see commented code in scraper.py) and configure your credentials.

## 📁 Project Structure
```bash
ai-web-scraper/
├── app.py                # Streamlit frontend
├── scraper.py            # Web scraping and content extraction
├── parser.py             # LangChain + Ollama-based parser
├── requirements.txt
└── README.md
```

## ✨ Use Cases
# Market intelligence
# Data aggregation
# Real-time content extraction
# News/article parsing with LLM
# Research automation

# 📌 Notes
# Make sure chromedriver is in the project directory or PATH.
# Ollama must be running in the background for the LLM to work.
# Avoid overloading the model with huge pages — DOM chunking is built-in.
