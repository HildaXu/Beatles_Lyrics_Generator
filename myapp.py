import streamlit as st
import json
from collections import Counter
#import torch

header = st.container()
#dateset = st.container()
#features = st.container()
#model_Training = st.container()

desc = "Check out the code [here](https://github.com/HildaXu/Beatles_Lyrics_Generator)!"
with header:
	st.title("Welcome to the Beatles Lyrics Generator!❤️✌️")
	st.write(desc)
	
#with dateset:
	#st.header('Dataset:')
	#st.text('The dataset is derived from kaggle. https://www.kaggle.com/jenlooper/beatles-lyrics')

#with features:
	#st.header('The features:')

#with model_Training:
	#st.header('Time to train model!')
	#st.text('Choose the number of words')

num_sentences = st.number_input('Number of words', min_value=1, max_value=20, value=5)
user_input = st.text_input('Seed Text (can leave blank)')

if st.button('Generate Text'):
    generated_text = generate_text.prediction(net, word_to_id, id_to_word, always_capitalized, user_input, 9, num_sentences)
    st.write(generated_text)

