from flask import Flask, render_template,request,redirect,url_for,flash,abort,session,jsonify
import json
import os.path
from werkzeug.utils import secure_filename
import numpy as np
import pickle
#carregando o modelo
#model = pickle.load(open('models\Modelo_treinado_RefriS.pkl', 'rb'))




app = Flask(__name__)
app.secret_key = 'asdfghjk'



@app.route('/')
def inicio():
    return render_template('tte.html', codes = session.keys())
    #return redirect(url_for('comentario'))


@app.route('/adicionar', methods =['GET','POST'])
def adc():
    if request.method == 'POST':
        coment = {'Brassagem': 0, 'Centrifuga':0, 'Filtração':0, 'L_501':0, 'L_503':0, 'L_511':0,'L_511_Refri':0,'L_512':0,'L_521':0,'L_551':0,'L_561':0,'L_562':0}
        
        coment['Brassagem'] = request.form['Brassagem']
        coment['Centrifuga'] = request.form['Centrifuga']
        coment['Filtração'] = request.form['Filtracao']
        coment['L_501'] = request.form['L_501']
        coment['L_503'] = request.form['L_503']
        coment['L_511'] = request.form['L_511']
        coment['L_511_Refri'] = request.form['L_511_Refri']
        coment['L_512'] = request.form['L_512']
        coment['L_521'] = request.form['L_521']
        coment['L_551'] = request.form['L_551']
        coment['L_561'] = request.form['L_561']
        coment['L_562'] = request.form['L_562']
  
        #==================================================================================
      
        teste = np.array([[coment['Brassagem'],coment['Centrifuga'],coment['Filtração'],coment['L_501'],
                            coment['L_503'],coment['L_511'],coment['L_511_Refri'],coment['L_512'],coment['L_521'],coment['L_551'],coment['L_561'],coment['L_562']]]) 

        #Predizendo o valor do BS 
        classe = model.predict(teste)[0]
        print("O valor predito da nota do BS é: {}" .format(str(classe)))

        
        
        return render_template("pg_inicial.html",teste=f'O valor predito do BS é {classe:.2f}')

@app.route('/pg_inicial')
def index():
    return redirect(url_for('inicio'))       
 
    

app.run(debug=True, host='0.0.0.0')