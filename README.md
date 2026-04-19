# CineSage-Movie-Extractor
# 🎬 CineSage

**CineSage** is an AI-powered movie information extractor that transforms long, unstructured paragraphs into clean, structured insights.

It uses Large Language Models (LLMs) via LangChain to intelligently extract key details like title, cast, themes, and more — all in a readable format.

---

## 🚀 Features

* 🧠 Extract structured movie information from long text
* 🎬 Identifies title, cast, genre, themes, and key events
* 📄 Clean, readable output (non-JSON format)
* ⚡ Powered by LangChain + Mistral AI
* 🎨 Simple and elegant Streamlit UI
* 📥 Download extracted results

---

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **Mistral AI**
* **Streamlit**
* **dotenv**

---

## 📂 Project Structure

```
GenAi/
│
├── CineSage/
│   ├── core.py          # LLM logic & prompt handling
│   ├── CineSageUi.py   # Streamlit UI
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/CineSage.git
cd CineSage
```

### 2. Create virtual environment

```
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add environment variables

Create a `.env` file:

```
MISTRAL_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```
streamlit run CineSage/CineSageUi.py
```

Then open the URL shown in your browser.

---

## 💡 How It Works

1. User inputs a movie paragraph
2. Prompt template structures the extraction task
3. Mistral LLM processes the input
4. Output is formatted into readable sections

---

## 🧾 Example Output

```
Title: 3 Idiots
Type: Movie
Release Year: 2009
Director: Rajkumar Hirani

Main Cast:
- Aamir Khan
- R. Madhavan
- Sharman Joshi

Genre:
- Comedy
- Drama

Summary:
A story about friendship and the pressures of the Indian education system.

...
```

---

## 🔥 Future Improvements

* 🔍 Entity highlighting (actors, locations)
* 🌐 Multi-domain extraction (news, resumes, research papers)
* 🗂 History of extracted results
* 🚀 Deployment on Streamlit Cloud

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Shikhar Gupta**

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
