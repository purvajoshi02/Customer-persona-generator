# 🧠 AI Customer Persona Generator

🌐 **Live Demo:** [https://customer-persona-generator.onrender.com/](https://customer-persona-generator-aszn.onrender.com)

> **Note:** This application is hosted on **Render's free tier**. If the application has been inactive for some time, the first request may take **30–60 seconds** to wake up. After that, it responds normally.

An AI-powered web application that generates detailed customer personas using **Google Gemini AI**. This tool helps marketers, startups, and businesses better understand their target audience by creating realistic customer profiles along with behavioral insights and marketing recommendations.

---

## 🚀 Features

- 🤖 AI-generated customer personas using Google Gemini 2.5 Flash
- 👤 Detailed customer profile generation
- 🎯 Personality traits and background analysis
- 💡 Pain points and customer challenges
- 🛒 Buying behaviour analysis
- 📱 Preferred marketing platforms
- 📈 AI-powered marketing strategy recommendations
- 🛍️ Product recommendations
- 🎨 Modern responsive user interface
- 🔒 Secure API key management using `.env`
- ☁️ Live deployment on Render

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
- Render
- Ngrok (for local public testing)

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
├── README.md
└── .env
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/purvajoshi02/Customer-persona-generator.git
```

### 2. Navigate to the project

```bash
cd Customer-persona-generator
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

### 5. Install the required packages

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

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📝 How It Works

1. Enter customer information into the form.
2. Click **Generate AI Persona**.
3. The application sends the customer details to the Google Gemini API.
4. Gemini generates a detailed customer persona with marketing insights.
5. The generated persona is displayed in a clean and responsive dashboard.

---

## 🌐 Live Demo

Visit the deployed application here:

**https://customer-persona-generator.onrender.com/**

---

## 📸 Application Preview

The application includes:

- Customer Information Form
- AI-Generated Customer Persona
- Personality Analysis
- Customer Background
- Pain Points
- Buying Behaviour
- Preferred Marketing Platforms
- Marketing Strategy Suggestions
- Product Recommendations

---

## 🔒 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

> **Important:** Never upload your `.env` file or API keys to GitHub.

---

## 🎯 Future Enhancements

- 📄 Export persona as PDF
- 📋 Copy persona to clipboard
- 🕒 Persona history
- 🌙 Dark/Light mode
- 📊 Persona comparison dashboard
- 👤 User authentication
- 🗄️ Database integration
- 📈 Analytics dashboard
- 🌍 Multi-language support

---

## 👨‍💻 Author

Developed as an AI-powered customer persona generation tool using **Flask** and **Google Gemini AI**.

---

## 📄 License

This project is created for educational and learning purposes.
