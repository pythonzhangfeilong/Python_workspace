from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/first_html')
def func_html():
    return render_template('first_html.html')

if __name__ == '__main__':
    app.run()
