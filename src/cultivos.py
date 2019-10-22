from flask import Flask, request, render_template
from flask_cors import CORS
from datetime import datetime
import json
from coneccion import db_find,db_save

app = Flask(__name__, template_folder='../templates/')
#CORS(app)

cultivos_list = []

productos_list = ["Leche", "Cacao", "Carne", "Flores","Hortaliza"]

@app.route('/createCultivo/', methods=['GET'])
def addCultivo():
    return render_template('createCultivo.html', productos= productos_list)

@app.route('/listaCultivos', methods=['GET'])
def listaCultivo():
    find_response = find_cultivos()
    cultivos_list.clear()
    for x in find_response:
        cultivos_list.append(x)
    return render_template('listCultivos.html', cultivos= cultivos_list)

@app.route('/addCultivo', methods=['POST'])
def pushOne():
    vals = request.values
    if float(vals['area']) > 0 and float(vals['area']) <100:

        data = {'codigo':vals['codigo'],'latitud':vals['latitud'],'producto':vals['producto'],'longitud':vals['longitud'],'area':vals['area'],'imagen':vals['imagen']}
        db_save("cultivos", data)
        #---------------------------------------------------------------------
        find_response = find_cultivos()
        cultivos_list.clear()
        for v in find_response:
            cultivos_list.append(v)
        
        return render_template('listaCultivos.html', cultivos= cultivos_list)
    else:
        return 'El area debe ser un valor positivo y menor 100!'

def find_cultivos():
    find_response = db_find("cultivos")
    return(find_response)

app.run(port=5555, debug=True)