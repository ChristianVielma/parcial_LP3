from flask import Blueprint, render_template

provmod = Blueprint('proveedores', __name__, template_folder='templates')

@provmod.route('/proveedor-index')
def proveedorIndex():
    return render_template('proveedor-index.html')