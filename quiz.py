from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from ucimlrepo import fetch_ucirepo
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd
import openai
import streamlit as st

openai.api_key = "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"

def quiz():
    st.title("Breast Cancer Risk Assessment")
    user_responses = []

    # For 'st.radio', 'st.selectbox', 'index=0' will select the first option as default.
    # For 'st.slider', 'value=' will set the default value.
    # Default values are set as Male, 1, Yes, 1 child, 1 year old, No for breastfeeding, etc.

    sex = st.radio("What is your sex?", ("Male", "Female", "Non-Binary", "Prefer not to specify"), index=0)
    user_responses.append(f"What is your sex?,{sex}")

    if sex == "Female":
        menopause = st.radio("Have you experienced menopause?", ("Yes", "No"), index=0)
        user_responses.append(f"Have you experienced menopause?,{menopause}")

        first_menstrual_cycle_age = st.slider("When was your first menstrual cycle?", min_value=1, max_value=50, value=1)
        user_responses.append(f"When was your first menstrual cycle?,{first_menstrual_cycle_age}")

        pregnancy = st.radio("Have you ever been pregnant?", ("Yes", "No"), index=0)
        user_responses.append(f"Have you ever been pregnant?,{pregnancy}")

        if pregnancy == "Yes":
            children = st.radio("Do you have any children?", ("Yes", "No"), index=0)
            user_responses.append(f"Do you have any children?,{children}")

            if children == "Yes":
                num_children = st.slider("How many children do you have? Use 12 if 12+.", min_value=1, max_value=12, value=1)
                user_responses.append(f"How many children do you have?,{num_children}")

                first_child_age = st.slider("What age were you when you had your first child?", min_value=1, max_value=50, value=1)
                user_responses.append(f"What age were you when you had your first child?,{first_child_age}")

                breastfeeding = st.radio("Do you breastfeed?", ("Yes", "No"), index=0)
                user_responses.append(f"Do you breastfeed?,{breastfeeding}")

    age = st.slider("How old are you?", min_value=1, max_value=100, value=1)
    user_responses.append(f"How old are you?,{age}")

    breast_cancer_history = st.radio("Have you had breast cancer in the past?", ("Yes", "No"), index=0)
    user_responses.append(f"Have you had breast cancer in the past?,{breast_cancer_history}")

    breast_conditions = st.radio("Any history of other breast conditions?", ("Yes", "No"), index=0)
    user_responses.append(f"Any history of other breast conditions?,{breast_conditions}")

    dense_breasts = st.radio("Do you have dense breasts?", ("Yes", "No", "Unsure"), index=0)
    user_responses.append(f"Do you have dense breasts?,{dense_breasts}")

    hormone_replacement_therapy = st.radio("Are you currently taking hormone replacement therapy?", ("Yes", "No"), index=0)
    user_responses.append(f"Are you currently taking hormone replacement therapy?,{hormone_replacement_therapy}")

    birth_control_pills = st.radio("Are you taking birth control pills?", ("Yes", "No"), index=0)
    user_responses.append(f"Are you taking birth control pills?,{birth_control_pills}")

    smoke = st.radio("Do you smoke?", ("Yes", "No"), index=0)
    user_responses.append(f"Do you smoke?,{smoke}")

    live_with_smoker = st.radio("Do you live with someone who smokes?", ("Yes", "No"), index=0)
    user_responses.append(f"Do you live with someone who smokes?,{live_with_smoker}")

    frequently_around_smoker = st.radio("Are you frequently around someone who smokes?", ("Yes", "No"), index=0)
    user_responses.append(f"Are you frequently around someone who smokes?,{frequently_around_smoker}")

    drink_alcohol = st.radio("Do you drink alcoholic beverages?", ("Yes", "No"), index=0)
    user_responses.append(f"Do you drink alcoholic beverages?,{drink_alcohol}")

    if drink_alcohol == "Yes":
        frequency = st.selectbox("How often do you drink?", ("Daily", "Weekly", "Monthly", "Yearly"), index=0)
        user_responses.append(f"How often do you drink?,{frequency}")

        # Assuming an arbitrary default consumption value
        alcohol_consumption_default = 10  # This is an example value for grams of alcohol
        if frequency == "Daily":
            glasses_per_day = st.number_input("How much alcohol do you consume per day (in grams)?", value=alcohol_consumption_default)
        elif frequency == "Weekly":
            glasses_per_week = st.number_input("How much alcohol do you consume per week (in grams)?", value=alcohol_consumption_default)
            glasses_per_day = glasses_per_week / 7
        elif frequency == "Monthly":
            glasses_per_month = st.number_input("How much alcohol do you consume per month (in grams)?", value=alcohol_consumption_default)
            glasses_per_day = glasses_per_month / 30
        elif frequency == "Yearly":
            glasses_per_year = st.number_input("How much alcohol do you consume per year (in grams)?", value=alcohol_consumption_default)
            glasses_per_day = glasses_per_year / 365
        user_responses.append(f"Alcohol consumption (grams per day),{glasses_per_day}")

    exercise = st.radio("Do you actively exercise?", ("Yes", "No"), index=0)
    user_responses.append(f"Do you actively exercise?,{exercise}")

    # The following creates a CSV string from the user responses
    user_responses_csv = ','.join(map(str, user_responses))
    return user_responses_csv


csv_output = quiz()

messages = [{
      "role":
      "system",
      "content": "Pretend that you are a breast cancer AI bot by Detect. Based on this input, you will generate one different statements. Determine a confidence percentage that will determine if the user has no chance, a small chance, a likely chance, and a certain chance."  }, {
      "role": "user",
      "content": csv_output
  }]

gptResponse = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613",
                                             messages=messages)

testResponse = gptResponse["choices"][0]["message"]["content"]

disclaimerMD = ("""**Disclaimer:**

**Important Notice - This Program is Not a Substitute for Medical Advice**

This program is designed for informational and educational purposes only. We are not medical professionals, and the information provided by this program should not be considered a substitute for professional medical advice, diagnosis, or treatment. 

Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition. Never disregard professional medical advice or delay in seeking it because of something you have read or learned from this program.

The content provided by this program is intended to be general in nature and may not be suitable for every individual's specific health needs. The information presented here may not always reflect the most current research or medical guidelines.

If you are experiencing a medical emergency, call your local emergency number immediately or go to the nearest emergency room.

By using this program, you acknowledge and agree that you understand the limitations of the information provided and that you will not use it as a substitute for professional medical advice. We disclaim any liability for any action or inaction taken based on the information provided by this program.

Please consult with a qualified healthcare professional for personalized medical guidance, diagnosis, and treatment recommendations.

**Click on this disclaimer and type YES into the text box below to get your results.**""")
disclaimer = st.checkbox(disclaimerMD)
agreement = st.text_input("")
if disclaimer and (agreement == "YES"):
    calculate_button = st.button("Calculate Risk")
    if calculate_button:
            st.write(f'{testResponse}')
