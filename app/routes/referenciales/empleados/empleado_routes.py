from flask import Blueprint, render_template

empmod = Blueprint('empleados', __name__, template_folder='templates')

@empmod.route('/empleado-index')
def empleadoIndex():
    return render_template('empleado-index.html')