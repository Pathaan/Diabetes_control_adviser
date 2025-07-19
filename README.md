
# 🩺 AI Diabetes Health & Fitness Plan Generator

A modern, AI-powered application designed to assist individuals with **diabetes management** through **personalized health insights**, **safe exercise routines**, and **targeted nutrition plans**. Built using **Google Gemini**, **DuckDuckGoTools**, and **Streamlit**, this project demonstrates the synergy between LLMs and healthcare intelligence.



## 🔗 Live Demo



---

## 🌟 Features

- 🔍 **Diabetes Risk Assessment**
  - Uses blood glucose, symptoms, age, and family history to assess Type 1, Type 2, or Prediabetes risk.

- 🏃‍♂️ **AI-Generated Fitness Plan**
  - Personalised workouts considering the user’s age, weight, height, lifestyle, and diabetic type.

- 🍱 **Diabetic-Friendly Meal Suggestions**
  - Balanced diet plans with macronutrient splits, sugar control meals, and vegetarian options.

- 🧠 **LLM-Powered Coaching Agents**
  - 3 specialised agents coordinate responses with precision and empathy.

- 🔗 **DuckDuckGo Integration**
  - Pulls real-time health and medical data via web search tools to improve contextual accuracy.

- 🎨 **Beautiful, Responsive UI**
  - Intuitive and clean interface using Streamlit with logo and wellness-themed design.

---

## 🖼️ Screenshots

| User Input Form | Diabetes Plan Output |
| --------------- | -------------------- |
|<img width="1879" height="921" alt="image" src="https://github.com/user-attachments/assets/2b68c6e3-9898-44fa-b223-fe0792652b63" />
<img width="1895" height="833" alt="image" src="https://github.com/user-attachments/assets/0bc04af2-3676-4e4e-bf3f-aae2bd6793bc" />


---

## 🧠 Agents Overview

| Agent | Purpose |
|-------|---------|
| **Diabetes Risk Assessor** | Diagnoses diabetes type based on inputs (e.g., glucose, age, family history). |
| **Fitness Trainer** | Creates a detailed workout plan adjusted to diabetic restrictions. |
| **Health Planner (Integrator)** | Merges diagnosis + fitness to produce a final wellness strategy. |

All agents are orchestrated using the **Agno** framework and run on **Google Gemini Pro**.

---

## 🧪 Technologies Used

| Layer | Tech |
|------|------|
| 🧠 AI Models | Google Gemini Pro |
| 🛠 AI Agent Orchestration | Agno |
| 🔍 Web Search Tools | DuckDuckGoTools |
| 🖥 Interface | Streamlit |
| 🔐 Secrets Management | python-dotenv |
| 📦 Language | Python 3.10+ |

---

## 📁 Folder Structure

```

📦 diabetes-health-fitness-app/
│
├── app.py                   # Streamlit main application
├── .env                     # Stores API keys securely
├── requirements.txt         # Project dependencies
├── assets/                  # Logos, icons, and visuals
├── screenshots/             # Images used in README
└── README.md                # Full documentation

````

---

## ⚙️ Installation & Setup

Follow the steps below to get this project running on your machine:

### 🔁 1. Clone the Repo

```bash
git clone https://github.com/yourusername/diabetes-health-fitness-app.git
cd diabetes-health-fitness-app
````

### 🧪 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔐 4. Configure API Keys

Create a `.env` file and add your Gemini API key:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

### ▶️ 5. Run the App

```bash
streamlit run app.py
```

---

## 🧑‍💻 Usage

1. Launch the app.
2. Enter patient details like:

   * Age, Weight, Height
   * Activity level
   * Blood Glucose & BP
   * Diabetes symptoms (if any)
3. Choose `Get Plan`
4. Receive:

   * Diagnosis (Type 1/Type 2/Prediabetes/Normal)
   * Tailored Meal Plan
   * Fitness Routine
   * General Health Tips

---

## 🗂 Example Input Prompt to Fitness Agent

```python
prompt = (
  f"Generate a workout plan for a 45-year-old diabetic, 75kg weight, "
  f"170cm tall, low activity level, aiming for sugar control. Include warm-ups, "
  f"light cardio, strength training (if safe), and cool-downs. Focus on diabetes safety."
)
```

---

## 🧾 Sample `.env`

```env
GOOGLE_API_KEY=your_actual_google_gemini_key_here
```

---


## 🤝 Contributing

We welcome your contributions!

### 🔧 Steps to Contribute

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request ✅

---

## 📄 License

Distributed under the **MIT License**.

---

## 📬 Contact

**Author:** Md Shahrukh
📍 Kolkata, India
📧 Email: \[[Email](mdshahrukhbme@gmail.com)]
🔗 LinkedIn: [[linkedin](https://www.linkedin.com/in/md-shahrukh-locky/)]

---

> Made with ❤️ for healthcare and machine learning!

