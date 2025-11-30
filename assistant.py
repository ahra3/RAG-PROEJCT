from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


class Assistant:

    def __init__(self, system_prompt, llm, message_history=None, vector_store=None, employee_data=None):
        self.system_prompt = system_prompt
        self.llm = llm
        self.message_history = message_history or []

        # Normalize roles
        for msg in self.message_history:
            if msg["role"] == "AI":
                msg["role"] = "assistant"

        self.vector_store = vector_store
        self.employee_data = employee_data
        self.chain = self.get_conversation_chain()

    def get_response(self, user_input):
        return self.chain.invoke(user_input)

    def _safe_retriever(self):
        if self.vector_store is None:
            return None
        try:
            return self.vector_store.as_retriever()
        except:
            return None

    def get_conversation_chain(self):

        prompt = ChatPromptTemplate(
            [
                ("system", self.system_prompt),
                MessagesPlaceholder("conversation_history"),
                ("human", "{user_input}"),
            ]
        )

        parser = StrOutputParser()
        retriever = self._safe_retriever()

        chain = (
            {
                "user_input": RunnablePassthrough(),
                "conversation_history": lambda _: self.message_history,
                "employee_data": lambda _: self.employee_data,
                "retrieved_policy_information": retriever if retriever else (lambda _: None),
            }
            | prompt
            | self.llm
            | parser
        )

        return chain
