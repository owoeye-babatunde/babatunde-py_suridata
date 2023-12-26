import streamlit as st
import json
import random

from main import remove_duplicates_by_all_values, listify, dwarf_giant

#a more visually pleasing theme
st.set_page_config(page_title="Dwarf-Giant Pair Finder",
                   layout="wide",  # Expand to full width
                   initial_sidebar_state="expanded")  # Keep sidebar open

#Apply a custom theme
st.markdown("""
<style>
body {
  background-color: #f5f5f5;
  color: #333;
}
.st-ab {
  background-color: #4CAF50;
  color: white;
}
.st-at {
  background-color: #F4D03F;
  color: #333;
}
.st-ag {
  background-color: #009688;
}
</style>
""", unsafe_allow_html=True)

st.title(" Find the Dwarf-Giant Pair ‍♂️ ‍♂️")


st.write("**Upload a JSON file containing employee data:**")
uploaded_file = st.file_uploader("Choose a JSON file", type=["json"])

employee_list = []
if uploaded_file:
    try:
        employee_list = json.load(uploaded_file)
    except json.JSONDecodeError:
        st.error("Invalid JSON format. Please upload a valid JSON file.")

# a sample list if no file is uploaded
if not employee_list:
    st.caption("**Sample Data:**")
    employee_list = [
	{
		"department": "R&D",
		"name": "emp1",
		"age": 46
	},
	{
		"department": "Sales",
		"name": "emp2",
		"age": 28
	},
	{
		"department": "R&D",
		"name": "emp3",
		"age": 33
	},
	{
		"department": "R&D",
		"name": "emp4",
		"age": 29
	}
				
    ]
    st.json(employee_list)  # Display sample data in a JSON viewer

if employee_list:
    try:
        # Check for required key ("name") in each dictionary
        if not all(d.get("name") for d in employee_list):
            st.error("Missing 'name' key in one or more employees!")
        else:
            # Calculate dwarf-giant pair
                employees = remove_duplicates_by_all_values(employee_list)
                outer_list =listify(employees) 
                random.shuffle(outer_list) 
                pairs = dwarf_giant(outer_list)
            #dwarf_giant = run(employee_list)

            # Display results in a visually appealing format
                st.success(" Dwarf-Giant Pair Revealed! ")
                st.write(f"{pairs}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

       
       
