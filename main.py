from flask import Flask

##crear una nueva instancia de flask
app = Flask(__name__)

##decorador de python
@app.route('/')

## crear la primera ruta
def hello():
    return 'Hello word'