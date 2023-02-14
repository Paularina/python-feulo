from flask import Flask

app = Flask("Hello")


@app.route('/')
def Ola():
    return "Hello Mundo!"
