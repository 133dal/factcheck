#import
import streamlit as st
import streamlit_option_menu
from streamlit_option_menu import option_menu

def app():
    #CSS
    with open("wave.css.py") as f:
        css = f.read()

    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
        
    #website
    st.title("Symptom Information 📝")
    st.subheader("What to do?")
    st.write("According to [Upstate Medical University](https://www.upstate.edu/whatsup/2020/0515-how-to-feel-better-tips-for-self-care-when-sick.php#:~:text=It's%20time%20to%20call%20your,for%20more%20than%20three%20days.), some tips for self-care are getting lots of rest, drinking lots of water, eating well, and taking over-the-counter medications if symptoms feel critical. It's also highly advised to call the doctor when symptoms worsen/don't alleviate and your fever lasts more than 3 days.")
    st.write("However, if you prefer to search your symptoms regardless, here are some steps you can take!")

    
    st.subheader("Steps to Take:")
    st.write("(1) Check for author affiliations, conflicts of interest, commissioning and funding info, citations from other studies, and publication date")
    st.write("(2) Check for quotes from experts or topic area experts, check that it's been reviewed by an appropriate health professional, and search the health editorial policy")
    st.write("(3) If it feels really serious, see a real doctor! Getting help early can be crucial for dire illnesses")

    st.write("-----")

    st.subheader("For more detailed tips, check out these articles! ->")
    st.write("[Stop Googling your medical symptoms and do this instead](https://www.cnet.com/health/medical/google-medical-symptoms/)")
    st.write("[Harvard study: Internet searches sometimes lead to the right diagnosis](https://www.health.harvard.edu/staying-healthy/harvard-study-internet-searches-sometimes-lead-to-the-right-diagnosis)")

    #input
    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""

    my_input = st.text_input("Have any questions? Ask here!" , st.session_state["my_input"])
    submit = st.button("Submit")
    if submit:
        st.session_state["my_input"] = my_input
        st.write("You have entered:" , my_input)

