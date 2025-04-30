from flask import Flask, request, render_template
from operaciones import sumar
from operaciones import restar
from operaciones import multiplicar
from operaciones import dividir 
import random 
from livereload import Server
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/suma")
def ruta_suma():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 20)
    if num1 is None or num2 is None:
        return "faltan datos"

    return f"la suma de num1 y num2 es {sumar(num1, num2) }"

@app.route("/resta")
def ruta_restar():
    num1 = request.args.get(1,20)
    num2 = request.args.get(1,20)
    if num1 is None or num2 is None:
        return "faltan datos"

    return f"la suma de num1 y num2 es {restar(num1, num2) }"


if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve()
