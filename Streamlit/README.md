import streamlit as st
st.title("Simple Streamlit App")
st.write("Hey here we will practice Streamlit.")
st.write("Streamlit is an open-source app framework for Machine Learning and Data Science teams.")
st.markdown("Where actually we use streamlit?")
st.write("we use streamlit to create we apps to make our journey of data science and machine learning easy and interactive.")
st.header("Features of Streamlit")
st.subheader("1.Easy to use")
st.write("Streamlit is very easy to use and learn. You can create a web app with just a few lines of code.")
st.subheader("2.Fast Development")
st.write("Streamlit allows for rapid prototyping and development of web applications.")
st.subheader("3.Interactive Widgets")
st.write("Streamlit provides a variety of interactive widgets like sliders, buttons, and text inputs to enhance user interaction.")
st.subheader("4.Data Visualization")
st.write("Streamlit supports various data visualization libraries like Matplotlib, Plotly, and Altair.")
st.subheader("5.Integration with Machine Learning Libraries")
st.write("Streamlit seamlessly integrates with popular machine learning libraries like TensorFlow, PyTorch, and Scikit-learn.")
st.header("Using some interactive widgets")
st.subheader("Slider and input box example")
name=st.text_input("Enter your name:")
age=st.slider("select you age:",1,100,25)
if name:
    st.write(f"Hey supper cool to met you{name},welcome to Streamlit practicer app!")
    st.write(f"Your age is {age} years.")

checkbox=st.checkbox("Do you like Streamlit?")
if checkbox:
    st.write("Yay! Streamlit is awesome!").........hey create a read me for this thing till now and tix box the features i have explored yet and untick the features i have explored yet
