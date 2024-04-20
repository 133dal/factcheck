#import
import streamlit as st
from streamlit_option_menu import option_menu

def app():
    #CSS
    with open("wave.css.py") as f:
        css = f.read()
        
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    
    #website
    st.title("Fact-Checking Your Symptoms 👨‍💻")
    st.subheader("Passion Project Introduction:")
    st.write("Symptom Fact-Checker is dedicated to improving media literacy, particularly for those who wish to independently search how to treat their symptoms. It can be costly to get the doctor's professional diagnosis, and it can feel unnecessary especially when symptoms aren't severe and seem treatable at home. As a result, this website has been created with the intention of enabling such people to better recognize which sites are reliable to use.")

    img = "https://www.theodysseyonline.com/media-library/image.jpg?id=10443618&width=980&quality=85"

    st.image (
        img ,
        caption = "What You're Sick With, According to WebMD (Lauren Hall, Pennsylvania State University)"
        )

    st.write("Presently, it is very easy to find matches for your symptoms online, but matching symptoms doesn't necessarily mean that you have what the website says you have. According to [PBS](https://www.pbs.org/newshour/health/just-doctor-ordered-study-reveals-accuracy-self-diagnosing-online#:~:text=In%20the%20first%20large%2Dscale,one%2Dthird%20of%20the%20time.), WebMD and other symptom checkers using a computer algorithm were only effective about one-third of the time.")
    
    st.write("-----")
    st.write("Using Python and Streamlit, I hope to create a webpage where I can recommend reliable sources and help determine the accuracy of a source for those who like to search up their symptoms.")
    st.write("[Learn More >](https://www.youtube.com/watch?v=VqgUkExPvLY&ab_channel=CodingIsFun)")

