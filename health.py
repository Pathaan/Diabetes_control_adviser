import os
import streamlit as st
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
load_dotenv()

# | Feature          | Description                                                                     |
# | ---------------- | ------------------------------------------------------------------------------- |
# | 👥 AI Agents     | 3 AI agents using Google Gemini: meal planner, fitness trainer, and integrator. |
# | 🎛️ UI Inputs    | Collect age, weight, height, diet, activity, and fitness goals.                 |
# | 🧠 AI Output     | Personalized meal and workout plans.                                            |
# | 🧾 Combined Plan | Integrated strategy from both agents.                                           |
# | 📦 Tools Used    | Streamlit for UI, Gemini for LLM, DuckDuckGo for search.                        |
# | 🎨 UI Styling    | Custom CSS for a modern, fitness-themed design.                                 |


# GOOGLE_API_KEY = "AIzaSyCr35hxFrpVsbNWgqOwU6PwmkpwLmO2dJA"
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Dietary Planner Agent
# Uses Gemini model to create personalized diet plans.
# Responds to prompts about diet preferences, nutrition, hydration, etc.
# Can optionally use DuckDuckGo for web searches.

diabetes_risk_assessor = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    description="Assesses diabetes risk and provides personalized recommendations.",
    instructions=[
        "Analyze input for diabetes risk or existing diabetic condition.",
        "If diagnosed, provide dietary and lifestyle suggestions for managing diabetes.",
        "Suggest when to consult a doctor and possible lab tests.",
        "Explain what HbA1c and glucose levels mean.",
        "Use clear medical explanation but in user-friendly language.",
        "If needed, search the web for latest diabetes management guidelines.",
    ],
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)

# Function to get a personalized meal plan
# Uses Gemini to create workout routines based on the user's fitness goal and level.
# Includes warm-up, main workout, and cool-down.
def get_diabetes_risk_assessor_plan(age, weight, height, glucose_level, hba1c, blood_pressure, family_history, 
                  activity_level, symptoms, diagnosis):
    prompt = ( f"Assess the diabetes risk or provide diabetes management suggestions for a {age}-year-old patient. "
    f"The patient weighs {weight}kg, is {height}cm tall. "
    f"Recent blood glucose: {glucose_level} mg/dL. HbA1c: {hba1c}%. "
    f"Blood pressure: {blood_pressure}. Family history of diabetes: {family_history}. "
    f"Activity level: {activity_level}. "
    f"Symptoms (if any): {', '.join(symptoms)}. "
    f"Diagnosed condition: {diagnosis}.\n"
    f"Give a detailed response with diet, lifestyle, monitoring tips, and explain the medical implications."
)
    return diabetes_risk_assessor.run(prompt)

# Fitness Trainer Agent
diabetes_fitness_trainer = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    description="Creates personalized fitness routines tailored for individuals with diabetes.",
    instructions=[
        "Design safe and effective workout plans for people with Type 1 or Type 2 diabetes.",
        "Include warm-ups, aerobic/cardio, resistance training, and cool-down sessions.",
        "Customize plans based on fitness levels: Beginner, Intermediate, Advanced.",
        "Adapt workouts based on goals: blood sugar control, weight loss, muscle toning, or energy improvement.",
        "Highlight timing of exercise in relation to insulin or food intake.",
        "Include warnings for hypoglycemia, hydration tips, and safe blood glucose ranges for exercise.",
        "Recommend how to track exercise progress and monitor glucose before and after workouts.",
        "If necessary, search the web using DuckDuckGo for updated diabetes fitness guidelines.",
    ],
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True
)
# Function to get a personalized fitness plan
def get_diabetes_fitness_plan(age, weight, height, activity_level, fitness_goal, diabetes_type):
    prompt = (
        f"Generate a safe and effective workout plan for a {age}-year-old person with {diabetes_type} diabetes, "
        f"weighing {weight}kg, {height}cm tall, and having an activity level of '{activity_level}'. "
        f"The person’s fitness goal is '{fitness_goal}'.\n\n"
        f"Include:\n"
        f"- Suitable warm-ups, aerobic/cardio and strength training, and cool-down exercises.\n"
        f"- Adjust intensity based on Beginner, Intermediate, or Advanced levels.\n"
        f"- Guidelines on exercising safely with diabetes, including insulin/meal timing.\n"
        f"- Tips for avoiding hypoglycemia and staying hydrated.\n"
        f"- Recommendations for monitoring blood glucose before, during, and after workouts.\n"
        f"- How to track fitness progress and stay motivated over time.\n"
    )
    return diabetes_fitness_trainer.run(prompt)




# === Team Lead Agent for Diabetes Management ===
team_lead = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    description="Combines diabetes-specific diet and workout plans into a safe and holistic health strategy.",
    instructions=[
        "Merge personalized diabetes-friendly diet and fitness plans for an integrated care approach. Use tables if possible.",
        "Ensure the meal and exercise recommendations support blood sugar control, weight management, and energy stability.",
        "Suggest practical lifestyle changes for motivation, glucose monitoring, and consistency.",
        "Include safety considerations such as insulin timing, hypoglycemia prevention, hydration, and rest.",
        "Provide guidance on tracking health markers (e.g., glucose, HbA1c, weight) and how to adjust the plan accordingly."
    ],
    tools=[DuckDuckGoTools()],
    markdown=True
)

# === Function to Get Full Diabetes Health Plan ===
def get_full_diabetes_health_plan(
    name, age, weight, height, activity_level, dietary_preference, fitness_goal,
    glucose_level, hba1c, blood_pressure, family_history, symptoms, diagnosis
):
    # Generate diabetes risk mitigation advice
    dia_reduce_plan = get_diabetes_risk_assessor_plan(
        age, weight, height, glucose_level, hba1c, blood_pressure,
        family_history, activity_level, symptoms, diagnosis
    )
    
    # Generate fitness plan (diabetes specific)
    fitness_plan = get_diabetes_fitness_plan(
        age, weight, height, activity_level, fitness_goal, diagnosis
    )
    

    

    # Run team lead agent to combine all
    return team_lead.run(
        f"Greet the user named {name} and generate a complete health strategy.\n\n"
        f"User Information:\n"
        f"- Age: {age} years\n"
        f"- Weight: {weight}kg\n"
        f"- Height: {height}cm\n"
        f"- Activity Level: {activity_level}\n"
        f"- Dietary Preference: {dietary_preference}\n"
        f"- Fitness Goal: {fitness_goal}\n"
        f"- Diabetes Diagnosis: {diagnosis}\n"
        f"- Glucose Level: {glucose_level} mg/dL\n"
        f"- HbA1c: {hba1c}%\n"
        f"- Blood Pressure: {blood_pressure} mmHg\n"
        f"- Family History: {family_history}\n"
        f"- Symptoms: {symptoms}\n\n"
        f"Provide a holistic diabetes health strategy integrating all elements. Include tips for consistency, glucose monitoring, motivation, and safe living."
    )



# Set up Streamlit UI with a fitness theme
st.set_page_config(page_title="Diabetes Control Advisor", page_icon="🩺", layout="wide")

# Custom Styles for a Fitness and Health Theme
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 48px;
            font-weight: bold;
            color: #FF6347;
        }
        .subtitle {
            text-align: center;
            font-size: 24px;
            color: #4CAF50;
        }
        .sidebar {
            background-color: #F5F5F5;
            padding: 20px;
            border-radius: 10px;
        }
        .content {
            padding: 20px;
            background-color: #E0F7FA;
            border-radius: 10px;
            margin-top: 20px;
        }
        .btn {
            display: inline-block;
            background-color: #FF6347;
            color: white;
            padding: 10px 20px;
            text-align: center;
            border-radius: 5px;
            font-weight: bold;
            text-decoration: none;
            margin-top: 10px;
        }
        .goal-card {
            padding: 20px;
            margin: 10px;
            background-color: #FFF;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Title and Subtitle


st.markdown('<h1 class="title">🩺 AI Diabetes Health & Fitness Plan Generator</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Personalized fitness, meal, and risk-reduction plans for people managing diabetes.</p>', unsafe_allow_html=True)

# Sidebar Inputs
st.sidebar.header("⚙️ Diabetes Health Inputs")
st.sidebar.subheader("Customize Your Health Plan")

# General Health Inputs
name = st.text_input("What's your name?", "Jethalal")
age = st.sidebar.number_input("Age (in years)", min_value=10, max_value=100, value=30)
weight = st.sidebar.number_input("Weight (in kg)", min_value=30, max_value=200, value=70)
height = st.sidebar.number_input("Height (in cm)", min_value=100, max_value=250, value=170)
activity_level = st.sidebar.selectbox("Activity Level", ["Low", "Moderate", "High"])
dietary_preference = st.sidebar.selectbox("Dietary Preference", ["Balanced", "Low Carb", "Vegetarian", "Diabetic Friendly"])
fitness_goal = st.sidebar.selectbox("Fitness Goal", ["Blood Sugar Control", "Weight Loss", "Energy Boost", "General Fitness"])

# Diabetes-specific inputs
st.sidebar.subheader("🩸 Diabetes Profile")
diagnosis = st.sidebar.selectbox("Diabetes Type", ["Type 1", "Type 2", "Pre-diabetes"])
glucose_level = st.sidebar.number_input("Fasting Glucose Level (mg/dL)", min_value=60, max_value=400, value=120)
hba1c = st.sidebar.number_input("HbA1c (%)", min_value=4.0, max_value=15.0, value=6.5)
blood_pressure = st.sidebar.text_input("Blood Pressure (e.g., 120/80)", "130/85")
family_history = st.sidebar.selectbox("Family History of Diabetes?", ["Yes", "No"])
symptoms = st.sidebar.text_area("Current Symptoms (if any)", "Fatigue, frequent urination")

# Divider
st.markdown("---")
# st.markdown("### 🧾 Your Diabetes Fitness Profile")

# Button to Generate Plan
if st.sidebar.button("Generate Diabetes Health Plan"):
    if not age or not weight or not height or not glucose_level or not hba1c:
        st.sidebar.warning("Please fill in all required fields.")
    else:
        with st.spinner("🔄 Generating your personalized diabetes health strategy..."):
            full_plan = get_full_diabetes_health_plan(
                name=name,
                age=age,
                weight=weight,
                height=height,
                activity_level=activity_level,
                dietary_preference=dietary_preference,
                fitness_goal=fitness_goal,
                glucose_level=glucose_level,
                hba1c=hba1c,
                blood_pressure=blood_pressure,
                family_history=family_history,
                symptoms=symptoms,
                diagnosis=diagnosis
            )

            # Show Result
            st.subheader("📋 Your Personalized Diabetes Health Plan")
            st.markdown(full_plan.content)

            st.success("✅ This plan is tailored to help manage your diabetes effectively through fitness, diet, and lifestyle.")

      # Motivational Footer with Background Styling
# Motivational Footer with Dark Theme
st.markdown("""
    <style>
        /* Set the entire page background to black */
        .stApp {
            background-color: #000000;
            color: #ffffff;
        }

        /* Style for the motivational footer card */
        .goal-card {
            background-color: #1a1a1a;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
            margin-top: 40px;
        }

        .goal-card h4 {
            color: #00ffcc;
            margin-bottom: 10px;
        }

        .goal-card p {
            font-size: 16px;
            color: #cccccc;
        }
    </style>

    <div class="goal-card">
        <h4>💪 You're Taking Charge of Your Health!</h4>
        <p>With the right plan, diabetes can be managed. Stay consistent, monitor your levels, and stay active!</p>
    </div>
""", unsafe_allow_html=True)
