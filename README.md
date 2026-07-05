# 🧠 AI Customer Persona Generator

An AI-powered web application that generates detailed customer personas using **Google Gemini AI**. This tool helps marketers, startups, and businesses better understand their target audience by creating realistic customer profiles along with behavioral insights and marketing recommendations.

---

## 🚀 Features

- 🤖 AI-generated customer personas using Google Gemini 2.5 Flash
- 👤 Customer profile generation
- 🎯 Personality traits and background
- 💡 Pain points and challenges
- 🛒 Buying behaviour analysis
- 📱 Preferred marketing platforms
- 📈 Marketing strategy suggestions
- 🛍️ Product recommendations
- 🎨 Modern responsive UI
- 🔒 Secure API key management using `.env`

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### AI
- Google Gemini 2.5 Flash API

### Tools
- Python Dotenv
- Git & GitHub
- Ngrok (for public demo)

---

## 📂 Project Structure

```
customer-persona-generator/
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── utils/
│   └── gemini.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/purvajoshi02/purvajoshi02-customer-persona-generator.git
```

### 2. Navigate to the project

```bash
cd purvajoshi02-customer-persona-generator
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

### 7. Run the application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 📝 How It Works

1. Enter customer information.
2. Click **Generate AI Persona**.
3. The application sends the data to the Google Gemini API.
4. Gemini generates a comprehensive customer persona.
5. The generated persona is displayed in the dashboard.

---

## 📸 Application Preview

The application contains:

- Customer Information Form
- AI Generated Persona Panel
- Marketing Insights
- Personality Analysis
- Buying Behaviour
- Product Recommendations

---

## 🔒 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

**Do not upload your `.env` file to GitHub.**

---

## 🎯 Future Enhancements

- Export persona as PDF
- Copy persona to clipboard
- Persona history
- Dark/Light mode
- Multiple persona comparison
- User authentication
- Database integration
- Dashboard analytics

---

## 👨‍💻 Author

Developed as an AI-powered marketing tool using **Flask** and **Google Gemini AI**.

---

## 📄 License

This project is created for educational and learning purposes.
