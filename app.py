import streamlit as st

st.title("Unit Converter")
st.markdown("### Converts Length, Weight, Time")

category = st.selectbox("Choose type:", ['Length', 'Weight', 'Time'])

# Dropdown for selecting conversion unit based on category
if category == 'Length':
    unit = st.selectbox("Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == 'Weight':
    unit = st.selectbox("Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == 'Time':
    unit = st.selectbox("Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Hours to Minutes", "Hours to Days", "Days to Hours"])

# Input for value
value = st.number_input("Enter the value to convert")

# Conversion function
def convert_units(category, value, unit):
    if category == 'Length':
        if unit == 'Kilometers to Miles':
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

# Button and result
if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")
