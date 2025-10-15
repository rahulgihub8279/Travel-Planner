# 🧭 AI Travel Planner for Students ✈️  
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub Stars](https://img.shields.io/github/stars/rahulghub8279/Travel-Planner?style=social)

---

## 🎯 Overview
**AI Travel Planner** is an intelligent web app built using **Streamlit** and **Google Gemini API** that helps students plan budget-friendly and efficient trips.  
It provides **personalized itineraries**, **budget recommendations**, and **smart travel insights** — all with a clean, interactive interface.  

---

## 🚀 Features
✅ **AI-powered itinerary generation**  
💸 **Budget-friendly travel suggestions**  
📅 **Customizable travel dates and number of travelers**  
🏨 **Accommodation, food & activity recommendations**  
🧭 **Easy-to-use Streamlit interface**

---

## 🛠️ Tech Stack
| Component | Technology |
|------------|-------------|
| 🖥️ **Frontend** | Streamlit |
| ⚙️ **Backend** | Python |
| 🤖 **AI Model** | Google Gemini API |
| 🔐 **Environment Management** | python-dotenv |
| 🧾 **Version Control** | GitHub |

---

## 📂 Project Structure
Travel-Planner/
├── main.py # Main Streamlit app
├── requirements.txt # Dependencies
├── .env # Environment variables (API key)
├── my_env/ # Optional virtual environment
├── Project_ai_travel.pptx # Presentation file
└── .devcontainer/ # Dev container setup

---


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/rahulghub8279/Travel-Planner.git
cd Travel-Planner


2️⃣ Create Virtual Environment
python -m venv my_env
source my_env/bin/activate    # For Mac/Linux
my_env\Scripts\activate       # For Windows


3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add API Key

Create a .env file and add:

GEMINI_API_KEY=your_api_key_here

5️⃣ Run the App
streamlit run main.py
