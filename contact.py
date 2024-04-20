#import
import streamlit as st
from streamlit_option_menu import option_menu

def app():
    #CSS
    with open("wave.css.py") as f:
        css = f.read()
        
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

    #website
    st.title("📬 Contact Me!")

    
    st.markdown("#### Want to report a bug, request a feature, or send some feedback? Be sure to send something below!")
    st.write("Media literacy is an ever-evolving skill, any help is appreciated!")

    contact_form = """
    <form action="https://formsubmit.co/dokyoungashley@gmail.com" method="POST" enctype="multipart/form-data">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <br>
         <input type="text" name="_subject" placeholder="Subject">
         <br>
         <input type="email" name="email" placeholder="Your email" required>
         <br>
         <textarea name="message" placeholder="Your message here"></textarea>
         <br>
         <input type="file" class="img_btn" name="Upload Image" accept="image/png, image/jpeg">
         <br>
         <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    st.markdown("## Thank you for your input! 💌")

    st.info("Your contributions are highly appreciated. We will review your ideas/address the bugs as soon as possible!")


