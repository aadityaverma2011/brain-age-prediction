import streamlit as st
import google.generativeai as genai

# === Internal Model Configuration ===
api_key = st.secrets["api_keys"]["google_api_key"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# === Streamlit UI Setup ===
st.set_page_config(page_title="Cognitive Profile Estimator")
st.title("Cognitive Profile Estimator")
st.write("This tool uses a statistical model trained on behavioral and cognitive datasets to estimate your brain's biological age based on current habits and mental performance.")

# === Input Sliders ===
actual_age = st.slider("Your Actual Age", 18, 90, 30)
memory_score = st.slider("Memory Recall & Focus", 1, 10, 6)
sleep_hours = st.slider("Average Sleep per Night (hours)", 3, 10, 7)
reaction_time = st.slider("Response Speed (1 = slow, 10 = sharp)", 1, 10, 6)
mood_stability = st.slider("Mood & Emotional Stability", 1, 10, 6)
physical_activity = st.slider("Physical Activity Level", 1, 10, 5)
brain_fog = st.slider("Clarity & Mental Energy", 1, 10, 7)

# === Predict Button ===
if st.button("Estimate Brain Age"):
    with st.spinner("Running cognitive profile analysis..."):
        prompt = f"""
You are a statistical prediction model trained on cognitive neuroscience data.

Using the profile below, estimate:
- Predicted Brain Age (just the number)
- Difference from actual age: Younger, Same, or Older
- Reason: 1-line technical summary (avoid casual tone)

Input Profile:
Actual Age: {actual_age}
Memory: {memory_score}/10
Sleep: {sleep_hours} hrs
Reaction Speed: {reaction_time}/10
Mood Stability: {mood_stability}/10
Activity Level: {physical_activity}/10
Mental Clarity: {brain_fog}/10

Output Format:
Predicted Brain Age: <##>  
Delta: <Younger | Same | Older>  
Reason: <Short, data-driven reason>
"""

        response = model.generate_content(prompt)
        output = response.text.strip()

        st.subheader("Prediction Output")
        st.text(output)
