from flask import Blueprint, render_template

pagomod = Blueprint('metodo_pagos', __name__, template_folder='templates')

@pagomod.route('/metodo_pago-index')
def metodo_pagoIndex():
    return render_template('metodo_pago-index.html')