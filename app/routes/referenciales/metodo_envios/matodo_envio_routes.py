from flask import Blueprint, render_template

envimod = Blueprint('metodo_envios', __name__, template_folder='templates')

@envimod.route('/metodo_envio-index')
def metodo_envioIndex():
    return render_template('metodo_envio-index.html')