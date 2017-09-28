# encoding: utf-8

"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, redirect, url_for
from mercadorias3 import app,db
from flask.json import jsonify
import mercadorias3.models as models
import sys
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'register.html',
        title='Home Page'
    )

@app.route('/tables')
def tables():
    """Renders the tables page."""
    return render_template(
        'tables.html',
        title='Tabela'
    )

@app.route('/api/mercadorias',methods=['GET'])
def pegaMercadorias():
    '''
        Rotina que pega todas as linhas da tabela ProcessoSeletivo

        Entrada:
        ---- : Nenhum parametro
        
        Saida:
        Array JSON
    '''
    try:
        lista = []
        todos = models.ProcessoSeletivo.query.all()
        for i in todos:
            lista.append(i.toJSON())
    except:
        print("error ", sys.exc_info()[0])
    return jsonify(lista), 200

@app.route('/api/mercadoria',methods=['POST'])
def adicionaMercadoria():
    '''
        Rotina que adiciona um conjunto de dados na tabela mercadoria

        Entrada:
        ---- : Nenhum parametro
        
        Saida:
        Retorna para a rota /tables
    '''
    codMer = (request.form['codMer'])
    tipoMer = (request.form['tipoMer'])
    nomeMer = (request.form['nomeMer'])
    qtdMer = (request.form['qtdMer'])
    precoMer = (request.form['precoMer']).replace(',','.')
    try:
        float(precoMer)
    except ValueError:
        return jsonify({'ERRO': 'Campo \"Preco da Mercadoria\" precisa ser numerico'}), 400
    tNegocio = (request.form['tNegocio'])
    if(codMer == '' or codMer == None):
        return jsonify({'ERRO': 'Campo \"Codigo da Mercadoria\" obrigatorio'}), 400
    elif(tipoMer == '' or tipoMer == None):
        return jsonify({'ERRO': 'Campo \"Tipo da Mercadoria\" obrigatorio'}), 400
    elif(nomeMer == '' or nomeMer == None):
        return jsonify({'ERRO': 'Campo \"Nome da Mercadoria\" obrigatorio'}), 400
    elif(qtdMer == '' or qtdMer == None):
        return jsonify({'ERRO': 'Campo \"Quantidade da Mercadoria\" obrigatorio'}), 400
    elif(not qtdMer.isdigit() ):
        return jsonify({'ERRO': 'Campo \"Quantidade da Mercadoria\" precisa ser numerico.'}), 400
    elif(precoMer == '' or precoMer == None):
        return jsonify({'ERRO': 'Campo \"Preco da Mercadoria\" obrigatorio'}), 400
    elif(tNegocio == '' or tNegocio == None):
        return jsonify({'ERRO': 'Campo \"Tipo do Negocio\" obrigatorio'}), 400
    elif(not tNegocio.isdigit()):
        return jsonify({'ERRO': 'Campo \"Tipo do Negocio\" precisa ser numerico e booleano'}), 400
    todo = models.ProcessoSeletivo(codMer=codMer,tipoMer=tipoMer,nomeMer = nomeMer,qtdMer=qtdMer,preco=precoMer,tNegocio = tNegocio)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('tables')), 200
