#import
import streamlit as st
from streamlit_option_menu import option_menu
import home , media_literacy , sinfo , contact

#website
st.set_page_config(page_title="My Webpage" , page_icon=":tada:" , layout="wide")

#menu
class MultiApp:
    def _init_(self):
        self.app = []
    def add_app(self , title , function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run():
        with st.sidebar:
            app = option_menu(
                menu_title="Main Menu",
                options=["Home" , "Media Literacy" , "Symptom Information" , "Contact"],
                icons=["house" , "book" , "newspaper"],
                menu_icon="chat-text-fill" ,
                default_index=1
               )

        if app == "Home":
            home.app()
        if app == "Media Literacy":
            media_literacy.app()
        if app == "Symptom Information":
            sinfo.app()
        if app == "Contact":
            contact.app()

    run()


