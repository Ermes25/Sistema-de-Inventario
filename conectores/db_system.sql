CREATE TABLE Productos(
	id_producto INT AUTO_INCREMENT PRIMARY KEY,
	nombre_producto VARCHAR(255) NOT NULL,
	categoria VARCHAR(255) NOT NULL,
	fecha_ingreso TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	fecha_vencimiento DATE,
	cantidad INT NOT NULL,
	precio DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Proveedores(
	id_proveedor INT AUTO_INCREMENT PRIMARY KEY,
	nombre_proveedor VARCHAR(255) NOT NULL,
	numero_proveedor VARCHAR(15), 
	direccion VARCHAR(255) NOT NULL
);

CREATE TABLE Pedidos(
	id_pedido INT AUTO_INCREMENT PRIMARY KEY,
	nombre_cliente VARCHAR(255) NOT NULL,
	id_producto INT,
	id_proveedor INT,
	fecha_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	cantidad_pedido INT NOT NULL,
	FOREIGN KEY(id_producto) REFERENCES Productos(id_producto),
	FOREIGN KEY(id_proveedor) REFERENCES Proveedores(id_proveedor)
);