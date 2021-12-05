import streamlit as st

header = st.container()
dateset = st.container()
features = st.container()
model_Training = st.container()

with header:
	st.title("Welcome to the Beatles Lyrics Generator!")

with dateset:
	st.header('Dataset:')
	st.text('The dataset is derived from kaggle. https://www.kaggle.com/jenlooper/beatles-lyrics')

with features:
	st.header('The features:')

with model_Training:
	st.header('Time to train model!')
	st.text('Choose the number of words')


