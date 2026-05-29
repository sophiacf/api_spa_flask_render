
from flask import Flask

from flask import jsonify

from flask_cors import CORS

app = Flask(__name__)

CORS(app)

usuarios = [

    {
        "nome": "Sophia",
        "email": "sophia@email.com",
        "telefone": "(14) 99999-1111"
    },

    {
        "nome": "Lucas",
        "email": "lucas@email.com",
        "telefone": "(14) 98888-2222"
    },

    {
        "nome": "Marina",
        "email": "marina@email.com",
        "telefone": "(14) 97777-3333"
    }

]

@app.route("/usuarios")

def buscarUsuarios():

    return jsonify(usuarios)

app.run(debug=True)
