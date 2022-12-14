import streamlit
import pandas

streamlit.title("My Parents Healthy Diner")
streamlit.markdown("**Have a happy day with tasty dishes !**")

streamlit.header("Today's Special")
streamlit.subheader("🍴 Breakfast Menu 🍽️")

streamlit.write("✨ Chappathi with dal")
streamlit.write("✨ Dosa with sambar")
streamlit.write("✨ Sambar Idli")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
