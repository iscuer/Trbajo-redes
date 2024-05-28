from flask import Flask, render_template, request
from flask_mail import Mail
from flask_mail import Message  #error importando las librerias 
import sys                                                                      

#Crear app medante instancia
app = Flask(__name__,template_folder='html')


#Config mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'concesionariotruffade@gmail.com'
app.config['MAIL_PASSWORD'] = 'truffadeteorico'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

#Inicializamos aplicacion
mail=Mail(app)

@app.route("/")
def index():
    return render_template('citaprevia.html')

@app.route('/citaprevia', methods=['POST'])
def send_previa():
    email = request.form['email']
    msg = Message("Cita Previa Solicitada", sender="concesionariotruffade@gmail.com", recipients=[email])
    msg.body = "Su cita previa se ha registrado. Gracias por contactarnos"
    mail.send(msg)
    
    #Conexion a BD + insert en tabla
    return "Mensaje Enviado"

@app.route('/pedidos', methods=['POST'])
def send_pedidos():
    email = request.form['email']
    msg = Message("Pedido solicitado", sender="concesionariotruffade@gmail.com", recipients=[email])
    msg.body = "Su pedido se ha registrado correctamente. Gracias por contactarnos"
    mail.send(msg)
    return "Mensaje Enviado"
    
if __name__=="__main__":
    app.run(debug=True)