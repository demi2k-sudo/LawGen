import streamlit as st


def chatbot(input_list):
    responses = {}
    st.write("Welcome to the Chatbot!")
    with st.form("chat_form"):
        submitted = st.form_submit_button("Submit")
        for key in input_list:
            # st.write(f"Question for '{key}':")
            value = st.text_input(f"Enter a value for '{key}':")
            responses[key] = value

        submitted = st.form_submit_button("Submit")

    if submitted:
        st.write("Here's the dictionary of values:")
        st.write(responses)
        return responses

def get(input_list):
    st.title("User details")

    # input_list = ['Effective Date', 'Service Provider', 'Service Provider Address', 'Client', 'Client Address', '_Service 1', 'Amount']


    st.write("Chatbot is ready to collect values.")
    res = chatbot(input_list)
    if(res):
        return res

if __name__ == "__main__":
    main()
