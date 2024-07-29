from flask import request, render_template, jsonify
from . import app  # Import the app instance from the current package
from models.agent import LangchainAgent

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    try:
        user_input = request.form['user_input']
        agents = LangchainAgent()
        response = agents.get_response(user_input)
        print(response)
        output = response['output']
        return jsonify({'response': output})
    except Exception as e:
        app.logger.error(f"Error in /query endpoint: {str(e)}")
        return jsonify({'error': str(e)}), 500
