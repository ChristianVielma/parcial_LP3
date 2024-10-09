from flask import Blueprint, render_template

sucumod = Blueprint('sucursales', __name__, template_folder='templates')

@sucumod.route('/sucursal-index')
def sucursalIndex():
    return render_template('sucursal-index.html')