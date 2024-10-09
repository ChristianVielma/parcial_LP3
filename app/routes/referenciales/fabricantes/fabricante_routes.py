from flask import Blueprint, render_template

fabrmod = Blueprint('fabricantes', __name__, template_folder='templates')

@fabrmod.route('/fabricante-index')
def fabricanteIndex():
    return render_template('fabricante-index.html')