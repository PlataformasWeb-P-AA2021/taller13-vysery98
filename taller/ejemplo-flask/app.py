from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Welcome!<br>Administración E.D.</p>"


@app.route("/losedificios")
def los_edificios():
    r = requests.get("http://127.0.0.1:8000/api/edificios/", auth=('admin', 'admin'))
    edificios = json.loads(r.content)['results']
    numero_edificios = json.loads(r.content)['count']
    return render_template("losedificios.html", edificios=edificios,
    numero_edificios=numero_edificios)

@app.route("/losdepartamentos")
def los_departamentos():
    r = requests.get("http://127.0.0.1:8000/api/departamentos/", auth=('admin', 'admin'))
    datos = json.loads(r.content)['results']
    numero_departamentos = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append({'propietario':d['propietario'], 'costo':d['costo'], 'num_cuartos': d['num_cuartos'], 'edificio':d['edificio'], 'edificio':obtener_edificio(d['edificio'])})
    return render_template("losdepartamentos.html", datos=datos2,
    numero_departamentos=numero_departamentos)

# funciones ayuda

def obtener_edificio(url):
    """
    """
    r = requests.get(url, auth=('admin', 'admin'))
    edificios = json.loads(r.content)['nombre'] + " | " + json.loads(r.content)['ciudad']
    return edificios
