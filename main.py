from dotenv import load_dotenv
import os
import gradio as gr

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

def chat(user_in, hist):
	print(user_in, hist)
	
	langchain_history = []
	for item in hist:
		if item["role"] == "user":
			langchain_history.append(HumanMessage(content=item["content"]))
		elif item["role"] == "assistant":
			langchain_history.append(AIMessage(content=item["content"]))
		
	response = chain.invoke({"input": user_in, "history": langchain_history})
		
	return "", hist + [{"role": "user", "content": user_in},
	                   {"role": "assistant", "content": response.content}]



page = gr.Blocks(
    title="Chat with Einstein",
)

with page:
	gr.Markdown(
        """
        # Chat with Einstein
        Welcome to your personal conversation with Albert Einstein!
        """
    )

	chatbot = gr.Chatbot(avatar_images=(None, "/home/rohit-m/PycharmProjects/AI_Chatbot/einstein.png"),
	                     show_label=False)  #show_label used to show/ not show the label

	msg = gr.Textbox()
	msg.submit(chat, [msg, chatbot], [msg, chatbot])

	clear = gr.Button("Clear Chat") #default name="Run"

page.launch(theme=gr.themes.Soft(),
            share=True) #share allows us to create a public link.