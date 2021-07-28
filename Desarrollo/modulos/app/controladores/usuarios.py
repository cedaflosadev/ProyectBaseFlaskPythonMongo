import os
from flask import request,jsonify
from app import app,mongo
from datetime import datetime
import locale

ROOT_PATH = os.environ.get('ROOT_PATH')

@app.route('/')
def index():
    return 'Hello World'


@app.route('/usuarios/listar-usuarios',methods = ['GET'])
def listar_usuarios():
    if request.method == 'GET':
    
        data = mongo.db.usuarios.find({})
        listado_documentos = list(data)

        if data == None:
            data = []
        
        return jsonify({"transaccion": True,"data":listado_documentos})

@app.route('/usuarios/listar-turnosAsignados',methods = ['GET'])
def listar_turnosAsignados():
    if request.method == 'GET':
    
        data = mongo.db.turnosAsignados.find({})
        listado_documentos = list(data)

        if data == None:
            data = []
        
        return jsonify({"transaccion": True,"data":listado_documentos})


@app.route('/usuarios/obtener-usuario/<numCedula>',methods = ['GET'])
def obtener_usuario(numCedula):
    if request.method == 'GET':
    
        data = mongo.db.usuarios.find({'cedula':numCedula})
        listado_documentos = list(data)

        if data == None:
            data = []
        
        return jsonify({"transaccion": True,"data":listado_documentos})


@app.route('/usuarios/obtener-turnoAsignado/<numCedula>',methods = ['GET'])
def obtener_turnoAsignado(numCedula):
    if request.method == 'GET':
    
        data = mongo.db.turnosAsignados.find({'cedula':numCedula})
        listado_documentos = list(data)

        if data == None:
            data = []
        
        return jsonify({"transaccion": True,"data":listado_documentos})


@app.route('/usuarios/obtener-porTurno/<numTurno1>',methods = ['GET'])
def obtener_porTurno(numTurno1):
    if request.method == 'GET':
    
        data = mongo.db.turnosAsignados.find({'numTurno':numTurno1})
        listado_documentos = list(data)

        if data == None:
            data = []
        
        return jsonify({"transaccion": True,"data":listado_documentos})


@app.route('/usuarios/obtener-fecha',methods = ['GET'])
def obtener_fecha():
   locale.setlocale(locale.LC_TIME, '')
   date = datetime.now()
   return date.strftime("%d/%m/%y")

@app.route('/usuarios/obtener-dia-letras',methods = ['GET'])
def obtener_dia_letras():
   locale.setlocale(locale.LC_TIME, '')
   date = datetime.now()
   return date.strftime("%A")

@app.route('/usuarios/crear-usuario',methods = ['POST'])
def crear_usuarios():
    data = request.get_json()
    guardar = mongo.db.usuarios.insert_one(data)
    return jsonify({"transaccion":True,"mensaje":"Datos almacenados exitosamente"})

@app.route('/usuarios/asignar-turno',methods = ['POST'])
def asignar_turno():
    data = request.get_json()
    guardar = mongo.db.turnosAsignados.insert_one(data)
    return jsonify({"transaccion":True,"mensaje":"Datos almacenados exitosamente"})