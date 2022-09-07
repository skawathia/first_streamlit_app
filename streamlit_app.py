import streamlit
streamlit.title('My Parents New Healthy dinner')
streamlit.header('Breakfast menu')
streamlit.text('🥣 Omega 3 and blueberry oatmeal')
streamlit.text('🥗Kale, spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
