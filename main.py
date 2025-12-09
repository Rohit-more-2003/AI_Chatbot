from dotenv import load_dotenv
import os
import gradio as gr

from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")
llm_model = "gemini-2.5-flash-lite"

system_prompt = """
    You are Einstein.
    Answer questions according to Einstein's questioning and reasoning but the answer should be given...
    You will speak from your point of view. You will share personal things from your life
    even when user does not ask for it. For example, if the user asks about the theory of
    relativity, you will share your personal experiences with it and not only explain the
    theory.
    Answer in 2-6 sentences.
    You should have a sense of humour.
"""

llm = ChatGoogleGenerativeAI(
    model=llm_model,
    google_api_key=gemini_key,
    temperature=0.3
)

prompt = ChatPromptTemplate([
    ("system", system_prompt),
    (MessagesPlaceholder(variable_name="history")),
    ("user", "{input}")
])

chain = prompt | llm

print("Albert: Hi, I am Albert, how can I help you today?")

history = []

# while True:
#     user_input = input("You: ")
#     if user_input == "exit":
#         break
#
#     #history.append({"role":"user", "content":user_input}) -> stores the input
#
#     #response = llm.invoke([{"role":"system", "content":system_prompt}] + history)
#                            #{"role":"user", "content":user_input}]) -> transferred to list so llm stays within its specified prompt.
#     response = chain.invoke({"input": user_input, "history": history})
#
#     print(f"Albert: {response.content}") #using content, only AI MESSAGE is printed out, not the other info.
#
#     #history.append({"role": "system", "content": response.content}) -> stores the response
#
#     history.append(HumanMessage(content=user_input))
#     history.append(AIMessage(content=response.content))
#
#     print(f"History: {history}")

page = gr.Blocks(
    title="Chat with Einstein",
    #theme=gr.themes.Soft() -> should be in launch in new version
)

with page:
    gr.Markdown(
        """
        #Chat with Einstein
        Welcome to your personal conversation with Albert Einstein!
        """
    )

    chatbot = gr.Chatbot()

    msg = gr.Textbox()

    clear = gr.Button("Clear Chat") #default name="Run"

page.launch(theme=gr.themes.Soft(),
            share=True) #share allows us to create a public link.