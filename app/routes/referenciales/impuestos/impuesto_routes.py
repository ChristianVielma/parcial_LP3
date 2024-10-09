from flask import Blueprint, render_template

impumod = Blueprint('impuestos', __name__, template_folder='templates')

@impumod.route('/impuesto-index')
def impuestoIndex():
    return render_template('impuesto-index.html')