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
st.divider()
st.header("Using some interactive widgets")
st.subheader("Slider and input box example")
name=st.text_input("Enter your name:")
age=st.slider("select you age:",1,100,25)
if name:
    st.write(f"Hey supper cool to met you{name},welcome to Streamlit practicer app!")
    st.write(f"Your age is {age} years.")

checkbox=st.checkbox("Do you like Streamlit?")
if checkbox:
    st.write("Yay! Streamlit is awesomes!")

st.divider()
st.subheader(("Alert and info message example"))
st.subheader("This is an info message")
st.info("This is an info message example in Streamlit.")
st.subheader("This is a warning message")
st.warning("This is a warning message example in Streamlit")
st.subheader("This is an error message")
st.error("This is an error message example in Streamlit.")
st.subheader("This is a success message")
st.success("This is a success message example in Streamlit.")
st.divider()
st.header("Expanders and Collapsibles demo")
with st.expander("CLICK HERE TO EXPAND"):
    st.write("This is an example of expanders in Streamlit.You can put any content and it will give a dropdown animation to show or hide the content.")
    st.write("Cool right?")

st.subheader("Multiple expanders example")
with st.expander("CLICK TO KNOW SOME FACTS ABOUT STREAMLIT"):
    st.write("Can i deploy my Streamlit apps for free?")
    st.info("Yes, you can deploy your Streamlit apps for free using Streamlit Community Cloud.")

    st.write("Do i need to know web development to use Streamlit")
    st.info("No, you don't need to know web development to use Streamlit. It is designed to be easy for data scientists and machine learning engineers.")

st.subheader("Multi-level expander example")

col1,col2=st.columns(2)

with col1:
    with st.expander("Lets learn pyth.on"):
        st.write("Pythom is a high level programmimg language use for data science,machine learning,web development and many more.")
        st.write("It is easy to learn and has a large community support.")

with col2:
    with st.expander("Lets learn Data Science"):
        st.write("Learn libraries like pandas for data manipularion")
        st.write("Learn numpy for numerical computing")

st.divider()
st.header("We will now learn about buttons in Streamlit")
if st.button("CLICK HERE"):
    st.write("You clicked the button made by me!")
    st.balloons()


st.divider

st.subheader("Creating calculator using buttons")
num1=st.number_input("Enter first number:")
num2=st.number_input("Enter second number:")
col1,col2,col3,col4=st.columns(4)
with col1:
    if st.button("ADD"):
        st.write(f"The sum of {num1} and {num2} is {num1+num2}")
with col2:
    if st.button("Subtract"):
        st.write(f"The difference of {num1} and {num2} is {num1-num2}")
with col3:
    if st.button("Product"):
        st.write(f"The product of {num1} and {num2} is {num1*num2}")
with col4:
    if st.button("Divide"):
        if num2!=0:
            st.write(f"The division of {num1} by {num2} is {num1/num2}")
        else:
            st.error("Division by zero is not allowed.")
st.divider()
st.highlight("st.button has lots of use cases in creating interactive web apps using Streamlit like games,calendars etc.")



    



