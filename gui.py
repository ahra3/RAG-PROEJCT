import streamlit as st

class AssistantGUI:
    def __init__(self, assistant):
        self.assistant = assistant
        self.messages = assistant.message_history
        self.employee_data = assistant.employee_data

    def get_response(self, user_input):
        return self.assistant.get_response(user_input)

    def render_messages(self):
        for msg in self.messages:
            role = msg["role"]
            content = msg["content"]

            if role == "user":
                st.chat_message("user").markdown(content)
            elif role == "assistant":
                st.chat_message("assistant").markdown(content)

    def set_state(self, key, value):
        st.session_state[key] = value

    def render_user_input(self):
        user_input = st.chat_input("Ask something...", key="user_input")

        if not user_input or user_input.strip() == "":
            return

        st.chat_message("user").markdown(user_input)

        try:
            response = self.get_response(user_input)
        except Exception as e:
            response = f"⚠️ Error while generating response: {e}"
            

        self.messages.append({"role": "user", "content": user_input})
        self.messages.append({"role": "assistant", "content": response})

        st.chat_message("assistant").markdown(response)

        self.set_state("message_history", self.messages)

    def render(self):
        with st.sidebar:
            st.logo("https://upload.wikimedia.org/wikipedia/commons/0/0e/Umbrella_Corporation_logo.svg")
            st.title("Umbrella Onboarding Assistant")
            st.subheader("Employee Info")
            st.write(self.employee_data)

        self.render_messages()
        self.render_user_input()
