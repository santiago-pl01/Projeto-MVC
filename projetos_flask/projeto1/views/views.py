#aquei serão declaras as rotas/caminhos que são usados nos APIS
from projeto1.views.main import app

from flask import render_template

#referencia a variavel  nome
@app.route("/")

#inicia a função homepage e retorna o templete, da pasta templete e inicia o ae
def homepage():
    return render_template("index.html")