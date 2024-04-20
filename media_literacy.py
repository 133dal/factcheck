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
    st.title("Media Literacy & Others 📚")
    st.subheader("Reliable sources →")
    st.write("[(1) Basic tips for a quick read on media literacy >](https://www.unc.edu/discover/how-to-improve-your-media-literacy-skills/)")
    st.write("[(2) The WHAT/WHY/HOW of media literacy>](https://www.pbs.org/education/blog/what-is-media-literacy-and-how-can-simple-shifts-center-it)")
    st.write("[(3) NAMLE: get involved in advancing media literacy education!>](https://www.forbes.com/sites/meimeifox/2022/12/05/4-tools-for-developing-critical-media-literacy-skills-from-namle/?sh=668d530867ae)")

    st.write("-----")
    st.write("[(1) WebMD >](https://www.webmd.com/)")
    st.write("WebMD is a site that focuses on providing news and information about health and mental wellbeing. It's good for finding general information, but it's less credible for details.")
    st.write("[(2) Mayo Clinic >](https://www.mayoclinic.org/)")
    st.write("Mayo Clinic is a nonprofit academical medical center that provides detailed information on a variety of health topics. Most notably, it's known for specializing in cancer, cardiology, and endocrinology.")
    st.write("-----")

    #input
    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""

    my_input = st.text_input("Write here!" , st.session_state["my_input"])
    submit = st.button("Submit")
    if submit:
        st.session_state["my_input"] = my_input
        st.write("You have entered:" , my_input)

