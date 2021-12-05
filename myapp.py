import streamlit as st
import json
from collections import Counter
#import torch




#===========================================#
#              Streamlit Layout             #
#===========================================#
header = st.container()

desc = "Check out the code [here](https://github.com/HildaXu/Beatles_Lyrics_Generator)!"
with header:
	st.title("Welcome to the Beatles Lyrics Generator!❤️✌️")
	st.write(desc)

num_sentences = st.number_input('Number of words', min_value=1, max_value=20, value=5)
user_input = st.text_input('Seed Text (can leave blank)')

if st.button('Generate Text'):
    generated_text = generate_text.prediction(net, word_to_id, id_to_word, always_capitalized, user_input, 9, num_sentences)
    st.write(generated_text)

