from flask import Flask

app = Flask(__name__)
@app.route('/')
def inicio():
    return 'Welcome to real life, baby'

app.run()
