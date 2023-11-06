import streamlit as st
from streamlit_option_menu import option_menu
import openai
import streamlit.components.v1 as components
from streamlit_modal import Modal

openai.api_key = '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'
engine = "gpt-3.5-turbo"
max_tokens = 150

def chatbot(prompt):
    messages = [
        {"role": "system", "content": "You are a bot that ONLY gives information on breast cancer, breast cancer awareness, and prevention but DO NOT give medical advice."},
        {"role": "assistant", "content": prompt}]

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613",
                                               messages=messages)
    bot_response = response['choices'][0]['message']['content']
    return bot_response

def disclaimer():
    st.title("disclaimer")

def home():
    st.markdown(
        """<div style="display: flex; justify-content: center;">
            <h1>About Us</h1>
        </div>""", unsafe_allow_html=True)
    st.image('home.jpg')
    st.write("DETECT (Detection, Education, and Technology for Early Cancer Tracing) is a groundbreaking initiative focused on improving early detection of breast cancer, particularly in underserved and low-income communities. Our mission is to provide accessible, personalized, and cost-effective breast cancer screening and education to those who need it most.\n\nOur approach combines cutting-edge technology with extensive research and education to address the challenges associated with breast cancer. We have developed a machine learning model that analyzes various breast cancer traits, to provide real-time breast cancer detection. This technology is user-friendly and specifically designed for the elderly population, the population most susceptible to breast cancer, ensuring accessibility and ease of use.\n\nBy collaborating with nonprofits like Susan G. Komen, the American Cancer Society, and the Breast Cancer Research Foundation, we aim to offer discounted treatment rates and comprehensive support. We're committed to making our service accessible to a wide range of healthcare facilities and patients, regardless of their economic status.\n\nDETECT is not just a business; it\'s a social mission. We believe that by providing early cancer detection and education, we can make a significant impact on the lives of many, ultimately reducing the burden of breast cancer worldwide. Join us in our quest to save lives and improve the health of communities around the globe.")

def quiz():
    st.title("Breast Cancer Risk Assessment")

    sex = st.radio("What is your sex?", ("Male", "Female", "Non-Binary", "Prefer not to specify"))
    if sex == "Female":
        menopause = st.radio("Have you experienced menopause?", ("Yes", "No"))
        first_menstrual_cycle_age = st.slider("When was your first menstrual cycle?", min_value=1, max_value=50, value=12)
        pregnancy = st.radio("Have you ever been pregnant?", ("Yes", "No"))
        if pregnancy == "Yes":
            children = st.radio("Do you have any children?", ("Yes", "No"))
            if children == "Yes":
                num_children = st.slider("How many children do you have? Do 12 if 12+.", min_value=1, max_value=12, value=2)
                first_child_age = st.slider("What age were you when you had your first child", min_value=1, max_value=100, value=30)
                breastfeeding = st.radio("Do you breastfeed?", ("Yes", "No"))

    age = st.slider("How old are you?", min_value=1, max_value=100, value=30)

    breast_cancer_history = st.radio("Have you had breast cancer in the past?", ("Yes", "No"))

    breast_conditions = st.radio("Any history of other breast conditions?", ("Yes", "No"))

    dense_breasts = st.radio("Do you have dense breasts?", ("Yes", "No", "Unsure"))

    hormone_replacement_therapy = st.radio("Are you currently taking hormone replacement therapy?", ("Yes", "No"))

    birth_control_pills = st.radio("Are you taking birth control pills?", ("Yes", "No"))

    smoke = st.radio("Do you smoke?", ("Yes", "No"))

    live_with_smoker = st.radio("Do you live with someone who smokes?", ("Yes", "No"))

    frequently_around_smoker = st.radio("Are you frequently around someone who smokes?", ("Yes", "No"))

    drink_alcohol = st.radio("Do you drink alcoholic beverages?", ("Yes", "No"))
    if drink_alcohol == "Yes":
        frequency = st.selectbox("How often do you drink?", ("Daily", "Weekly", "Monthly", "Yearly"))
        if frequency == "Daily":
            glasses_per_day = st.number_input("How much alcohol do you consume per day (in grams)?")
        elif frequency == "Weekly":
            glasses_per_day = st.number_input("How much alcohol do you consume per week (in grams)?") / 12
        elif frequency == "Monthly":
            glasses_per_day = st.number_input("How much alcohol do you consume per month (in grams)?") / 30
        elif frequency == "Yearly":
            glasses_per_day = st.number_input("How much alcohol do you consume per year (in grams)?") / 365

    exercise = st.radio("Do you actively exercise?", ("Yes", "No"))

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
                st.markdown(
            """<div style="display: flex; justify-content: center;">
                <h1>There is a significant probability of breast cancer. Prompt consultation with a doctor is advised.</h1>
            </div>""", unsafe_allow_html=True)

def learnMore():
    st.markdown(
        """<div style="display: flex; justify-content: center;">
            <h1>Learn More!</h1>
        </div>""", unsafe_allow_html=True)
    prompt = st.text_input(
          f"2. Have a question about breast cancer? Ask it here!")
    if prompt:
        st.markdown(chatbot(prompt))

def support():
    st.title("Resources Page")
    # Add resource content here
    st.write("Welcome to the resources page! Here you can find valuable information, articles, and links related to breast cancer awareness and prevention.")
    st.write("1. [Connect with a Doctor](https://www.example.com/breast-cancer-guide)")
    st.write("2. [Breast Cancer Awareness Guide](https://www.example.com/breast-cancer-guide)")
    st.write("3. [Breast Cancer Prevention Tips](https://www.example.com/breast-cancer-prevention)")
    st.write("4. [Support Groups and Organizations](https://www.example.com/support-groups)")
    st.write("5. [Telehealth Resources](https://www.example.com/events)")
    st.write("6. [Affiliated Insurance Companies](https://www.example.com/events)")
    st.write("7. [Affiliated Mobile Clinics](https://www.example.com/events)")
    st.write("8. [Latest Research and Studies](https://www.example.com/research)")

def contact():
  st.header("Contact Us")

  user_name = st.text_input("Your Name", key="contact_name")
  user_email = st.text_input("Your Email", key="contact_email")
  user_message = st.text_area("Your Message", key="contact_message")

  if st.button("Submit", key="contact_submit"):
    st.success("Thank you for contacting us! We will get back to you soon.")

def main():
    st.image('DetectLogo.png', use_column_width = True)
    selected = option_menu(None, ["Home", "Quiz", "Learn", "Support", "Site Help"],
                        icons= ["house", "check-circle", "book", "link", "person"],
                        menu_icon="cast",
                        default_index=0,
                        orientation="horizontal")

    if selected == "Home":
        home()
    elif selected == "Quiz":
        quiz()
    elif selected == "Learn":
        learnMore()
    elif selected == "Support":
        support()
    elif selected == "Site Help":
        contact()

if __name__ == "__main__":
    main()


