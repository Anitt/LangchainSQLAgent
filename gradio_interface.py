# gradio_interface.py

import gradio as gr
from models.agent import LangchainAgent

def query_flask(user_input):
    try:
        agent = LangchainAgent()
        response = agent.get_response(user_input)
        return response['output']
    except Exception as e:
        return f"Error: {str(e)}"

iface = gr.Interface(fn=query_flask, inputs="text", outputs="text",title="Text to SQL HR DATABASE - Input your query in natural language")
iface.launch(share=True)
