from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def func_hello():
    return 'Hello Word!'

if __name__ == '__main__':
    app.run()
