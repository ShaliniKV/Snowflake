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
streamlit.dataframe(my_fruit_list)
