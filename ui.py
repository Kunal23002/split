import streamlit as st
from logic import add_person, add_food_item, update_list, delete_person, delete_food, calculate_prices

def ui_addperson():
    st.text_input('Enter name:', key='new_person')
    st.button('Add Person', on_click=add_person)

def ui_display_people():
    st.header('People Present')
    for person in st.session_state.people.keys():
        col1, col2 = st.columns([10,10])
        col1.write(person)
        col2.button('Delete this person', key=f'delete_{person}', on_click=delete_person, args=(person,))
    
def ui_fooditems():
    st.header('Food Items')
    st.text_input('Enter food item',key = 'new_food')
    st.number_input('Enter price:', key='new_price', min_value=0.0)
    st.button('Add Food Item',on_click=add_food_item)

def ui_display_fooditems():
    for food in st.session_state.food_prices.keys():
        col1, col2 , col3 ,col4, col5 = st.columns([10,10,10,20,15])
        col1.write(food)
        col2.button('Delete this Item', key=f'delete_{food}', on_click=delete_food, args=(food,))
        col3.write(st.session_state.food_prices[food])
        selected_people = col4.multiselect('Select People',st.session_state.people,key = f'{food}new_list') 
        col5.button('Add?',on_click=update_list,args=(food,selected_people),key=f'{food}_button')

def ui_calculate_prices():
    st.button('Calculate total',on_click=calculate_prices,key='calc_button')
