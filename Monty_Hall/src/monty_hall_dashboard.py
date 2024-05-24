import streamlit as st
from src.monty_hall import simulate_games
import time

#Title of the application
st.title("Monty Hall Simulation")

num_of_games = st.number_input("number of games",min_value=1, max_value=1000,value=100)

#Create tow lists to hold win percentages for both cases
wins_switch = 0
wins_not_switch = 0


col1, col2 = st.columns(2)

col1.subheader("wins percentage with switching")
chart1 = col1.line_chart(x=None, y=None, height=400)

col2.subheader("wins percentage without switching")
chart2 = col2.line_chart(x=None, y=None, height=400)

for i in range(num_of_games):
    # simulate one game at a time
    num_wins_with_switching, num_wins_without_switching = simulate_games(1)

    # Calculate win percentages for both cases and add to lists 
    wins_switch += num_wins_with_switching
    wins_not_switch += num_wins_without_switching
    st.write(wins_switch)

    # Display the current percentages after each game
    chart1.add_rows([wins_switch/(i+1)])
    chart2.add_rows([wins_not_switch/(i+1)])

    # Add a delay to create a slow loop effect
    time.sleep(.01)
    


