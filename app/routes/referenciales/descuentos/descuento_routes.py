from flask import Blueprint, render_template

descmod = Blueprint('descuentos', __name__, template_folder='templates')

@descmod.route('/descuento-index')
def descuentoIndex():
    return render_template('descuento-index.html')