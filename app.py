import streamlit as st
from logic import initialize_session_state
from ui import ui_addperson, ui_fooditems, ui_display_people, ui_display_fooditems, ui_calculate_prices


def main():
    st.title('SPLIT CALCULATOR')
    initialize_session_state()

    ui_addperson()
    ui_display_people()
    
    ui_fooditems()
    ui_display_fooditems()
    
    ui_calculate_prices()

if __name__ == "__main__":
    main()