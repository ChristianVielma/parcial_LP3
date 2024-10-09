from flask import Blueprint, render_template

exismod = Blueprint('existencias', __name__, template_folder='templates')

@exismod.route('/existencia-index')
def existenciaIndex():
    return render_template('existencia-index.html')