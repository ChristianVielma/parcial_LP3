from flask import Flask

app = Flask(__name__)

# importar referenciales
from app.routes.referenciales.categorias.categoria_routes import catmod
from app.routes.referenciales.cajas.caja_routes import cajmod
from app.routes.referenciales.depositos.deposito_routes import depomod
from app.routes.referenciales.descuentos.descuento_routes import descmod
from app.routes.referenciales.empleados.empleado_routes import empmod
from app.routes.referenciales.existencias.existencia_routes import exismod
from app.routes.referenciales.fabricantes.fabricante_routes import fabrmod
from app.routes.referenciales.impuestos.impuesto_routes import impumod
from app.routes.referenciales.marcas.marca_routes import marcmod
from app.routes.referenciales.metodo_envios.matodo_envio_routes import envimod
from app.routes.referenciales.metodo_pagos.matodo_pago_routes import pagomod
from app.routes.referenciales.personas.persona_routes import persmod
from app.routes.referenciales.productos.producto_routes import prodmod
from app.routes.referenciales.proveedores.proveedor_routes import provmod
from app.routes.referenciales.sucursales.sucursal_routes import sucumod

# registrar referenciales
modulo0 = '/referenciales'
app.register_blueprint(catmod, url_prefix=f'{modulo0}/categorias')
app.register_blueprint(cajmod, url_prefix=f'{modulo0}/cajas')
app.register_blueprint(depomod, url_prefix=f'{modulo0}/depositos')
app.register_blueprint(descmod, url_prefix=f'{modulo0}/descuentos')
app.register_blueprint(empmod, url_prefix=f'{modulo0}/empleados')
app.register_blueprint(exismod, url_prefix=f'{modulo0}/existencias')
app.register_blueprint(fabrmod, url_prefix=f'{modulo0}/fabricantes')
app.register_blueprint(impumod, url_prefix=f'{modulo0}/impuestos')
app.register_blueprint(marcmod, url_prefix=f'{modulo0}/marcas')
app.register_blueprint(envimod, url_prefix=f'{modulo0}/metodo_envios')
app.register_blueprint(pagomod, url_prefix=f'{modulo0}/metodo_pagos')
app.register_blueprint(persmod, url_prefix=f'{modulo0}/personas')
app.register_blueprint(prodmod, url_prefix=f'{modulo0}/productos')
app.register_blueprint(provmod, url_prefix=f'{modulo0}/proveedores')
app.register_blueprint(sucumod, url_prefix=f'{modulo0}/sucursales')

from app.routes.referenciales.categorias.categoria_api import catapi
from app.routes.referenciales.cajas.caja_api import cajapi
from app.routes.referenciales.depositos.deposito_api import depoapi 
from app.routes.referenciales.descuentos.descuento_api import descapi
from app.routes.referenciales.empleados.empleado_api import empapi
from app.routes.referenciales.existencias.existencia_api import exisapi
from app.routes.referenciales.fabricantes.fabricante_api import fabrapi
from app.routes.referenciales.impuestos.impuesto_api import impuapi
from app.routes.referenciales.marcas.marca_api import marcapi
from app.routes.referenciales.metodo_envios.metodo_envio_api import enviapi
from app.routes.referenciales.metodo_pagos.metodo_pago_api import pagoapi
from app.routes.referenciales.personas.persona_api import personaapi
from app.routes.referenciales.productos.producto_api import productoapi
from app.routes.referenciales.proveedores.proveedor_api import proveedorapi
from app.routes.referenciales.sucursales.sucursal_api import sucursalapi

# APIS v1
version1 = '/api/v1'
app.register_blueprint(catapi, url_prefix=version1)
app.register_blueprint(cajapi, url_prefix=version1)
app.register_blueprint(depoapi, url_prefix=version1)
app.register_blueprint(descapi, url_prefix=version1)
app.register_blueprint(empapi, url_prefix=version1)
app.register_blueprint(exisapi, url_prefix=version1)
app.register_blueprint(fabrapi, url_prefix=version1)
app.register_blueprint(impuapi, url_prefix=version1)
app.register_blueprint(marcapi, url_prefix=version1)
app.register_blueprint(enviapi, url_prefix=version1)
app.register_blueprint(pagoapi, url_prefix=version1)
app.register_blueprint(personaapi, url_prefix=version1)
app.register_blueprint(productoapi, url_prefix=version1)
app.register_blueprint(proveedorapi, url_prefix=version1)
app.register_blueprint(sucursalapi, url_prefix=version1)