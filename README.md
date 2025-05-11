# 📝 Cohere AI Text Summarizer

This project is a simple web application built using **Streamlit** that leverages **Cohere’s Generative AI API** to summarize large text into short, readable summaries. It’s ideal for condensing articles, research papers, or any lengthy content into bite-sized insights.

---

## 🚀 Features

- ✂️ Summarizes large chunks of text quickly
- 🤖 Uses Cohere's `summarize-xlarge` model
- 📄 Output formats include paragraphs (default) or can be extended to bullet points
- 💡 Easy-to-use interface powered by Streamlit

---

## 🛠️ Tech Stack

| Technology | Description |
|------------|-------------|
| Python     | Programming language |
| Streamlit  | Web app framework for the frontend |
| Cohere API | Natural language processing model used for summarization |
| python-dotenv | Loads environment variables from `.env` file |

---

## 📁 Project Structure
cohere-text-summarizer/
├── app.py # Main Streamlit app
├── .env # Contains your Cohere API key (do not share!)
├── requirements.txt # List of Python dependencies
└── README.md # Project documentation


---

## 🧪 Example Usage

1. Paste any long paragraph or article into the text box.
2. Click **Summarize**.
3. The app will display a concise summary using Cohere's summarization model.

---

## 🧰 Setup Instructions

### 🔐 1. Get Your Cohere API Key

- Sign up at [https://dashboard.cohere.com](https://dashboard.cohere.com)
- Get your API key and store it in a `.env` file like so:

```bash
COHERE_API_KEY=your_api_key_here
```
# 💻 2. Install Dependencies

pip install -r requirements.txt

# ▶️ 3. Run the Streamlit App

streamlit run app.py

# 📄 Sample .env File

COHERE_API_KEY=your_actual_api_key_here
⚠️ Make sure not to share your API key publicly.

# 🔮 Future Improvements
Allow selection between paragraph and bullet-point summaries

Support for multiple summarization models

Add support for uploading text files (PDF, TXT)

Dark mode UI
