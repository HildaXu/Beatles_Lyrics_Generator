import streamlit as st
import json
import pytorch
from collections import Counter

import generate_text

#===========================================#
#        Loads Model and word_to_id         #
#===========================================#

with open('trained_model/word_to_id.json') as json_file:
    word_to_id = Counter(json.load(json_file))

with open('trained_model/always_capitalized.json') as json_file:
    always_capitalized = json.load(json_file)

id_to_word = ["<Unknown>"] + [word for word, index in word_to_id.items()]

net = torch.load('trained_model/trained_model.pt')
net.eval()



#===========================================#
#              Streamlit Layout             #
#===========================================#
backgroud_image = st.container()
with backgroud_image:
	st.markdown(
	    """
	    <style>
	    .reportview-container {
		background: url("https://media.vogue.fr/photos/5c4f0adebc36eb75cd6d6104/16:9/w_2112,h_1188,c_limit/91pNsAaJgxL.jpg")
	    }
	   #.sidebar .sidebar-content {
		#background: url("https://media.vogue.fr/photos/5c4f0adebc36eb75cd6d6104/16:9/w_2112,h_1188,c_limit/91pNsAaJgxL.jpg")
	   #}
	    </style>
	    """,
	    unsafe_allow_html=True
	)

header = st.container()

desc = "Sorry, this website is still under construction, shome features may not work. ::( "
desc2 ="Check out the code [here](https://github.com/HildaXu/Beatles_Lyrics_Generator)!"
with header:
	st.title("Welcome to the Beatles Lyrics Generator!❤️✌️")
	st.write(desc)
	st.write(desc2)

num_sentences = st.number_input('Number of words', min_value=1, max_value=50, value=5)
user_input = st.text_input('Seed Text (can leave blank)')

if st.button('Generate Text'):
    generated_text = generate_text.prediction(net, word_to_id, id_to_word, always_capitalized, user_input, 9, num_sentences)
    st.write(generated_text)

