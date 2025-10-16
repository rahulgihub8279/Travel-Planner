# 🧭 AI Travel Planner for Students ✈️  
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit) 

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
```
Travel-Planner/
├── main.py 
├── requirements.txt 
├── .env 
├── my_env/ 
├── Project_ai_travel.pptx 
└── .devcontainer/ 

```


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/rahulghub8279/Travel-Planner.git
cd Travel-Planner
```

2️⃣ Create Virtual Environment
```
python -m venv my_env
source my_env/bin/activate    # For Mac/Linux
my_env\Scripts\activate       # For Windows
```

3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
4️⃣ Add API Key

Create a .env file and add:

GEMINI_API_KEY=your_api_key_here

5️⃣ Run the App
```
streamlit run main.py
```
