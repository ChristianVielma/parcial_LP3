from flask import Blueprint, render_template

cajmod = Blueprint('cajas', __name__, template_folder='templates')

@cajmod.route('/caja-index')
def cajaIndex():
    return render_template('caja-index.html')