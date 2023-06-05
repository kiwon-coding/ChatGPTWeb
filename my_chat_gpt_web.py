from flask import Flask, render_template, request, session
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
app.secret_key = 'my_secret_key_haha'

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

@app.route('/', methods=['POST'])
def send():
    user_input = request.form['input_text']
    messages = []
    if 'all_msg' in session:
        messages = session['all_msg']
    
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [{"role": "user", "content": user_input}]
    )
    ai_answer = response.choices[0].message["content"]
    messages.append(ai_answer)
    session['all_msg'] = messages
    return render_template('index.html', result=messages)

if __name__ == '__main__':
    app.run(debug=True)