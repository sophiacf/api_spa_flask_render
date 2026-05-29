
from flask import Flask

from flask import jsonify

from flask_cors import CORS

app = Flask(__name__)

CORS(app)
   
usuarios = [

    {
        "name": "Sophia",
        "email": "sophia@email.com",
        "phone": "(14) 99999-1111"
    },

    {
        "name": "Lucas",
        "email": "lucas@email.com",
        "phone": "(14) 98888-2222"
    },

    {
        "name": "Marina",
        "email": "marina@email.com",
        "phone": "(14) 97777-3333"
    }
    
]

@app.route("/usuarios")

def buscarUsuarios():

    return jsonify(usuarios)

app.run(debug=True)
