import streamlit

streamlit.title('My Moms New Healthy Diner')

streamlit.header('Breakfast Favourites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + str(fruit_choice))
print(fruityvice_response)

# take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it on the screen as a table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ROLE(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_cur.execute('select * from pc_rivery_db.public.fruit_load_list')
# my_data_rows = my_cur.fetchall()
# streamlit.header('The fruit load list contains:')
# streamlit.dataframe(my_data_rows)


# Display input field for the fruit name
fruit_name = st.text_input("Enter the fruit name:")

# Add the fruit to the fruit load list if a name is provided
if fruit_name:
    cur.execute("INSERT INTO pc_rivery_db.public.fruit_load_list (fruit_name) VALUES (%s)", (fruit_name,))
    cnx.commit()
    st.success(f"Added {fruit_name} to the fruit load list.")

# Retrieve all rows from the fruit load list
cur.execute('SELECT * FROM pc_rivery_db.public.fruit_load_list')
data_rows = cur.fetchall()

# Display the fruit load list
st.header('The fruit load list contains:')
st.dataframe(data_rows)
