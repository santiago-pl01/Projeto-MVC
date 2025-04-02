from flask import Flask


#variavel para a declaração do flask
app = Flask(__name__)

#importa a pasta viewas 
from projeto1.views.views import *

#quando a variavel NAME for igual ao arquivo man, ela sera iniciada
if __name__ == '__main__':
    app.run()