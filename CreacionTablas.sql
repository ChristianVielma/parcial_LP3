-- Tabla Personas 
CREATE TABLE personas (  
    id_persona SERIAL PRIMARY KEY,  
    pers_nombre VARCHAR(100) NOT NULL,  
    pers_apellido VARCHAR(100),  
    pers_direccion TEXT,  
    pers_telefono VARCHAR(15),  
    pers_email VARCHAR(100),  
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  
    fecha_modificacion TIMESTAMP  
);

-- Tabla Usuarios 
CREATE TABLE usuarios (  
    id_usuario SERIAL PRIMARY KEY,  
    password VARCHAR(255) NOT NULL,  
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  
    fecha_modificacion TIMESTAMP  
);

/* Insertar una columna id_persona en la tabla usuarios
 * Esto es para luego crear una referencia con la tabla personas*/
ALTER TABLE usuarios ADD COLUMN id_persona INT;

-- Agregar la restricción de clave foránea
ALTER TABLE usuarios 
ADD CONSTRAINT fk_id_persona 
FOREIGN KEY (id_persona) REFERENCES personas(id_persona) ON DELETE CASCADE;

-- Añadir la columna de referencia en la tabla Personas
ALTER TABLE personas ADD COLUMN usuario_creacion INT;

-- Agregar la restricción de clave foránea
ALTER TABLE personas 
ADD CONSTRAINT fk_usuario_creacion 
FOREIGN KEY (usuario_creacion) REFERENCES usuarios(id_usuario) ON DELETE CASCADE;


-- Tabla Sucursales
CREATE TABLE sucursales (  
    id_sucursal SERIAL PRIMARY KEY,  
    sucu_descripcion VARCHAR(100) NOT NULL,  
    sucu_direccion TEXT NOT NULL,  
    sucu_telefono VARCHAR(15),  
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  
    usuario_creacion INT REFERENCES usuarios(id_usuario),  
    fecha_modificacion TIMESTAMP,  
    usuario_modificacion INT REFERENCES usuarios(id_usuario)  
);

-- Tabla Empleados
CREATE TABLE empleados (  
    id_empleado SERIAL PRIMARY KEY,  
    id_persona INT REFERENCES personas(id_persona) ON DELETE CASCADE,
    id_sucursal INT REFERENCES sucursales(id_sucursal),  
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  
    usuario_creacion INT REFERENCES usuarios(id_usuario),  
    fecha_modificacion TIMESTAMP,  
    usuario_modificacion INT REFERENCES usuarios(id_usuario)  
);

-- Crear el tipo enum para usar en la columna de caja_estado  
CREATE TYPE tipo_evento AS ENUM ('abierto', 'cerrado');  

-- Tabla Cajas
CREATE TABLE cajas (  
    id_caja SERIAL PRIMARY KEY,  
    id_sucursal INT REFERENCES sucursales(id_sucursal) ON DELETE CASCADE,  
    fecha_apertura TIMESTAMP NOT NULL,  
    fecha_cierre TIMESTAMP,  
    monto_apertura DECIMAL(10, 2),  
    monto_cierre DECIMAL(10, 2),  
    id_empleado_abre INT REFERENCES empleados(id_empleado),  
    id_empleado_cierra INT REFERENCES empleados(id_empleado),  
    estado caja_estado not null,  
    observaciones TEXT,  
    creado_el TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
    modificado_el TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
);

-- Tabla Proveedores
CREATE TABLE proveedores (  
    id_proveedor SERIAL PRIMARY KEY,  
    prov_nombre VARCHAR(100) NOT NULL,    
    prov_telefono VARCHAR(15),  
    prov_email VARCHAR(100),  
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  
    usuario_creacion INT REFERENCES usuarios(id_usuario),  
    fecha_modificacion TIMESTAMP,  
    usuario_modificacion INT REFERENCES usuarios(id_usuario)  
);

-- Tabla Metodo Envio
CREATE TABLE metodo_envios (  
    id_metodo_envio SERIAL PRIMARY KEY,  
    meen_envio VARCHAR(100) NOT NULL,  
    meen_descripcion TEXT,  
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  
    usuario_creacion INT REFERENCES usuarios(id_usuario),  
    fecha_modificacion TIMESTAMP,  
    usuario_modificacion INT REFERENCES usuarios(id_usuario)  
);

-- Tabla Metodo Pago
CREATE TABLE metodo_pagos (  
    id_metodo_pago SERIAL PRIMARY KEY,    
    mepa_descripcion varchar(100) not null,  
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  
    usuario_creacion INT REFERENCES usuarios(id_usuario),  
    fecha_modificacion TIMESTAMP,  
    usuario_modificacion INT REFERENCES usuarios(id_usuario)  
);

-- Tabla Impuestos
CREATE TABLE impuestos (  
    id_impuesto SERIAL PRIMARY KEY,  
    impu_descripcion VARCHAR(100) NOT NULL,  
    impu_porcentaje DECIMAL(5, 2) NOT NULL,  
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  
    usuario_creacion INT REFERENCES usuarios(id_usuario),  
    fecha_modificacion TIMESTAMP,  
    usuario_modificacion INT REFERENCES usuarios(id_usuario)  
);

-- Tabla descuentos
CREATE TABLE descuentos (  
    id_descuento SERIAL PRIMARY KEY,  
    desc_descripcion VARCHAR(100) NOT NULL,  
    desc_porcentaje DECIMAL(5, 2) NOT NULL,  
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  
    usuario_creacion INT REFERENCES usuarios(id_usuario),  
    fecha_modificacion TIMESTAMP,  
    usuario_modificacion INT REFERENCES usuarios(id_usuario)  
);

-- Tabla Categorias 
CREATE TABLE categorias (  
    id_categoria SERIAL PRIMARY KEY,  
    cat_descripcion VARCHAR(100) NOT NULL,
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  
    usuario_creacion INT REFERENCES usuarios(id_usuario),  
    fecha_modificacion TIMESTAMP,  
    usuario_modificacion INT REFERENCES usuarios(id_usuario)  
);

-- Tabla Marcas
CREATE TABLE marcas (  
    id_marca SERIAL PRIMARY KEY,  
    marc_descripcion VARCHAR(100) NOT NULL,  
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  
    usuario_creacion INT REFERENCES usuarios(id_usuario),  
    fecha_modificacion TIMESTAMP,  
    usuario_modificacion INT REFERENCES usuarios(id_usuario)  
);

-- Tabla Fabricantes
CREATE TABLE fabricantes (  
    id_fabricante SERIAL PRIMARY KEY,  
    fabr_nombre VARCHAR(100) NOT NULL,  
    fabr_direccion TEXT,  
    fabr_telefono VARCHAR(15),  
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  
    usuario_creacion INT REFERENCES usuarios(id_usuario),  
    fecha_modificacion TIMESTAMP,  
    usuario_modificacion INT REFERENCES usuarios(id_usuario)  
);

-- Tabla Productos
CREATE TABLE productos (  
    id_producto SERIAL PRIMARY KEY,  
    prod_descripcion VARCHAR(100) NOT NULL,    
    prod_precio DECIMAL(10, 2) NOT NULL,  
    id_categoria INT REFERENCES categorias(id_categoria) ON DELETE SET NULL,  
    id_marca INT REFERENCES marcas(id_marca) ON DELETE SET NULL,  
    id_fabricante INT REFERENCES fabricantes(id_fabricante) ON DELETE SET NULL,  
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  
    usuario_creacion INT REFERENCES usuarios(id_usuario),  
    fecha_modificacion TIMESTAMP,  
    usuario_modificacion INT REFERENCES usuarios(id_usuario)  
);

-- Tabla Ventas
CREATE TABLE ventas (  
    id_venta SERIAL PRIMARY KEY,  
    id_persona INT REFERENCES personas(id_persona),  
    id_empleado INT REFERENCES empleados(id_empleado),  
    id_caja INT REFERENCES cajas(id_caja),  
    id_metodo_pago INT REFERENCES metodo_pagos(id_metodo_pago),  
    fecha_venta TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  
    total DECIMAL(10, 2) NOT NULL,  
    id_descuento INT REFERENCES descuentos(id_descuento),  
    id_impuesto INT REFERENCES impuestos(id_impuesto),  
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  
    usuario_creacion INT REFERENCES usuarios(id_usuario),  
    fecha_modificacion TIMESTAMP,  
    usuario_modificacion INT REFERENCES usuarios(id_usuario)  
);

-- Tabla Ventas Detalles
CREATE TABLE detalle_ventas (  
    id_detalle_venta SERIAL PRIMARY KEY,  
    id_venta INT REFERENCES ventas(id_venta) ON DELETE CASCADE,  
    id_producto INT REFERENCES productos(id_producto),  
    cantidad INT NOT NULL,  
    precio_unitario DECIMAL(10, 2) NOT NULL,  
    fecha_creacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  
    usuario_creacion INT REFERENCES usuarios(id_usuario),  
    fecha_modificacion TIMESTAMP,  
    usuario_modificacion INT REFERENCES usuarios(id_usuario)  
);

-- Tabla de Depósitos (almacenes)
CREATE TABLE depositos (
    id_deposito SERIAL PRIMARY KEY,
    depo_descripcion VARCHAR(100) NOT NULL,
    id_sucursal INT REFERENCES sucursales(id_sucursal)
);

-- Tabla Exitencias
CREATE TABLE existencias (  
    id_producto INT REFERENCES productos(id_producto),  
    id_deposito INT REFERENCES depositos(id_deposito),  -- Asegúrate de que la tabla depositos existe  
    exis_cantidad INT NOT NULL DEFAULT 0,   
    fecha_actualizacion TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  
    PRIMARY KEY (id_producto, id_deposito)  
);

-- Crear el tipo enum para usar en la columna de tipo_evento  
CREATE TYPE tipo_evento AS ENUM ('apertura', 'cierre');  

-- Tabla Eventos Cajas
CREATE TABLE eventos_caja (  
    id_evento SERIAL PRIMARY KEY,  
    id_caja INT REFERENCES cajas(id_caja) ON DELETE CASCADE,  
    tipo_evento tipo_evento NOT NULL,  
    id_empleado INT REFERENCES empleados(id_empleado),  -- Quién lo realizó  
    fecha_evento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
    observaciones TEXT  
);
