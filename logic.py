import streamlit as st
def initialize_session_state():
    if 'people' not in st.session_state:
        st.session_state.people = {}
    if 'food_prices' not in st.session_state:
        st.session_state.food_prices = {}
    if 'prices_list' not in st.session_state:
        st.session_state.prices_list = {}


def add_person():
    try:
        if st.session_state.new_person:
            # Add the new person to the people dictionary with an initial value of 0
            st.session_state.people[st.session_state.new_person] = 0

            # Clear the new_person input field
            st.session_state.new_person = ''
    except KeyError as e:
        st.error(f"A KeyError occurred: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

def add_food_item():
    try:
        food_item = st.session_state.new_food
        price = st.session_state.new_price
        if food_item and price:
            st.session_state.food_prices[food_item]=price

            st.session_state.new_food = ''
            st.session_state.new_price = 0.0
    except KeyError as e:
        st.error(f"A Keyerror occured: {e}")
    except Exception as e:
        st.error(f"An unexpected error occured: {e}")


def update_list(food_item,selected_people):
    try:
        if selected_people:
            st.session_state.prices_list[food_item] = selected_people
            st.session_state.new_list=[]
    except KeyError as e:
        st.error(f"A Keyerror occured: {e}")
    except Exception as e:
        st.error(f"An unexpected error occured: {e}")


# Function to delete a person from the list
def delete_person(person):
    try:
        # Attempt to delete the person from the people dictionary
        del st.session_state.people[person]
    except KeyError:
        st.warning(f"Person '{person}' not found in the list.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

def delete_food(food_item):
    try:
        del st.session_state.food_prices[food_item]
    except KeyError:
        st.warning(f"Person '{food_item}' not found in the list.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")


def calculate_prices():
    try:
        for food in st.session_state.prices_list:
            # Ensure the food exists in food_prices
            if food in st.session_state.food_prices:
                price = st.session_state.food_prices[food] / len(st.session_state.prices_list[food])
                for person in st.session_state.prices_list[food]:
                    # Ensure the person exists in people
                    if person in st.session_state.people:
                        st.session_state.people[person] += price
                    else:
                        st.warning(f"Person {person} not found in people.")
            else:
                st.warning(f"Food item {food} not found in food prices.")
    except KeyError as e:
        st.error(f"A KeyError occurred: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
    finally:
        st.write(st.session_state.people)
        for person in st.session_state.people.keys():
            st.session_state.people[person]=0


