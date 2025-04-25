from flask import Flask, request
from operaciones import sumar

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <h1> APLICACION DE CALCULADORA </h1>
    <a href="/suma?num1=5&num2=4">ir a pagina de suma </a>
    



'''

@app.route("/suma")
def ruta_suma():
    num1 = request.args.get("num1", type=float)
    num2 = request.args.get("num2", type=float)
    if num1 is None or num2 is None:
        return "faltan datos"

    return f"la suma de num1 y num2 es {sumar(num1, num2)}"