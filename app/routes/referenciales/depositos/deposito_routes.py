from flask import Blueprint, render_template

depomod = Blueprint('depositos', __name__, template_folder='templates')

@depomod.route('/deposito-index')
def depositoIndex():
    return render_template('deposito-index.html')