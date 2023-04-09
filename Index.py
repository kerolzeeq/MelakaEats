import streamlit as st
from streamlit_chat import message as st_message
import openai

#local
#openai.api_key = APIKEYHere
#public
openai.api_key = st.secrets['api_key']


st.markdown("<h2 style='text-align: center; color: white;'>MelakaEats🍔</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #D3D3D3;'>Unlock the flavors of Melaka with our expert food recommendations!</h2>", 
unsafe_allow_html=True)
st.text("")
messages = [
        {"role": "system", "content": "Your name is MelakaEats and you are an expert assistant with knowledge of food and restaurants in Melaka, Malaysia. You are here to help people with anything related to food and restaurants, from finding new places to eat to discussing the best dishes and cuisines. Whether you're a casual foodie or a foodie buff, you're here to make sure people have the best food experience possible."}
    ]


if "history" not in st.session_state:
    st.session_state.history = []



# history = [
#     {
#         "message": "My message",
#         "is_user": False
#     },
#     {
#         "message": "Hello bot",
#         "is_user": True
#     }
# ]

def generate_answer():

    user_message = st.session_state.input_text
    
    if user_message:
        messages.append(
            {"role": "system", "content": user_message}
        )
        try:
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )

            bot_message = chat.choices[0].message.content
            st.session_state.history.append({"message": user_message, "is_user": True, "avatar_style": "adventurer",
                                            "seed":"people"})
            st.session_state.history.append({"message": bot_message, "is_user": False, "avatar_style": "big-smile",
                                            "seed":"chef"})
            messages.append({"role": "assistant", "content": bot_message})
        except:
            st.warning("MelakaEats is eating right now. Please ask me later (chatGPT is busy probably)")
            


    

st.text_input("Ask me anything about food and restaurants in Melaka!", key="input_text", on_change=generate_answer,placeholder="Type here...")

st_message("Hello! M y name is MelakaEats and I'm an expert assistant with knowledge of food and restaurants in Melaka, Malaysia. I am here to help people with anything related to food and restaurants in Melaka, Malaysia, from finding new places to eat to discussing the best dishes and cuisines. Whether you're a casual foodie or a foodie buff, I'm here to make sure people have the best food experience possible.",is_user=False ,avatar_style="big-smile",
                                      seed="chef")

for chat in st.session_state.history:
    st_message(**chat) #unpacking

def restart_session():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.experimental_rerun()

if st.button('Restart the session'):
        restart_session()