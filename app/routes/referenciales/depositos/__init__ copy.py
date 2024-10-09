from flask import Flask

app = Flask(__name__)

# importar referenciales
from app.routes.referenciales.categorias.categoria_routes import catmod
from app.routes.referenciales.cajas.caja_routes import cajmod

# registrar referenciales
modulo0 = '/referenciales'
app.register_blueprint(catmod, url_prefix=f'{modulo0}/categorias')
app.register_blueprint(cajmod, url_prefix=f'{modulo0}/cajas')

from app.routes.referenciales.categorias.categoria_api import catapi
from app.routes.referenciales.cajas.caja_api import cajapi

# APIS v1
version1 = '/api/v1'
app.register_blueprint(catapi, url_prefix=version1)
app.register_blueprint(cajapi, url_prefix=version1)