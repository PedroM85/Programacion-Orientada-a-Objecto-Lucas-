-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         5.7.24 - MySQL Community Server (GPL)
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.1.0.6116
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para e_commerce
CREATE DATABASE IF NOT EXISTS `e_commerce` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `e_commerce`;

-- Volcando estructura para tabla e_commerce.tbl_almacen
CREATE TABLE IF NOT EXISTS `tbl_almacen` (
  `id_Almacen` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`id_Almacen`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla e_commerce.tbl_almacen: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `tbl_almacen` DISABLE KEYS */;
INSERT IGNORE INTO `tbl_almacen` (`id_Almacen`, `tipo`) VALUES
	(1, 'Deposito1'),
	(2, 'Deposito2'),
	(3, 'Mostrador'),
	(5, 'Exhibidor'),
	(6, 'asd'),
	(7, 'sd2s'),
	(8, 'Pruebadevenano');
/*!40000 ALTER TABLE `tbl_almacen` ENABLE KEYS */;

-- Volcando estructura para tabla e_commerce.tbl_categoria
CREATE TABLE IF NOT EXISTS `tbl_categoria` (
  `id_Categoria` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`id_Categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla e_commerce.tbl_categoria: ~24 rows (aproximadamente)
/*!40000 ALTER TABLE `tbl_categoria` DISABLE KEYS */;
INSERT IGNORE INTO `tbl_categoria` (`id_Categoria`, `tipo`) VALUES
	(1, 'Electrodomesticos'),
	(2, 'Consolas y videojuegos'),
	(3, 'Celulares'),
	(4, 'Aires Acondicionados'),
	(5, 'Informatica'),
	(6, 'Comida 2.0'),
	(7, 'Bebida'),
	(8, 'Fruta'),
	(9, 'Carnes'),
	(10, 'Gaseosa'),
	(11, 'Bebidas Alcoholicas'),
	(12, 'Aguas saborizadas'),
	(13, 'Aguas'),
	(14, 'Portatiles'),
	(15, 'Hornos'),
	(16, 'Lavarropas'),
	(17, 'Heladeras'),
	(18, 'Microndas'),
	(19, 'Aires Acondicionados frio'),
	(20, 'Aires acondicionados frio/calor'),
	(21, 'Computadoras'),
	(22, 'Impresoras'),
	(23, 'Notebooks'),
	(24, 'Televisores'),
	(26, 'casa'),
	(27, 'Alquiler'),
	(28, 'Prueba agregar y editar');
/*!40000 ALTER TABLE `tbl_categoria` ENABLE KEYS */;

-- Volcando estructura para tabla e_commerce.tbl_ciudad
CREATE TABLE IF NOT EXISTS `tbl_ciudad` (
  `id_ciudad` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(40) NOT NULL,
  PRIMARY KEY (`id_ciudad`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla e_commerce.tbl_ciudad: ~25 rows (aproximadamente)
/*!40000 ALTER TABLE `tbl_ciudad` DISABLE KEYS */;
INSERT IGNORE INTO `tbl_ciudad` (`id_ciudad`, `nombre`) VALUES
	(1, 'CABA'),
	(2, 'CAPITAL FEDERAL'),
	(3, 'CATAMARCA'),
	(4, 'CHACO'),
	(5, 'CHUBUT'),
	(6, 'CORDOBA'),
	(7, 'CORRIENTES'),
	(8, 'ENTRE RIOS'),
	(9, 'FORMOSA'),
	(10, 'JUJUY'),
	(12, 'LA RIOJA'),
	(13, 'MENDOZA'),
	(14, 'MISIONES'),
	(15, 'NACIONES'),
	(16, 'NEUQUEN'),
	(17, 'RIO NEGRO'),
	(18, 'SALTA'),
	(19, 'SAN JUAN'),
	(20, 'SAN LUIS'),
	(21, 'SANTA CRUZ'),
	(22, 'SANTA FE'),
	(23, 'SANTIAGO DEL ESTERO'),
	(24, 'TIERRA DE FUEGO'),
	(25, 'TUCUMAN'),
	(31, 'Caba 2.1'),
	(32, '123'),
	(33, 'Prueba agregar y editar');
/*!40000 ALTER TABLE `tbl_ciudad` ENABLE KEYS */;

-- Volcando estructura para tabla e_commerce.tbl_clientes
CREATE TABLE IF NOT EXISTS `tbl_clientes` (
  `id_user` int(11) NOT NULL AUTO_INCREMENT,
  `dni` varchar(11) DEFAULT NULL,
  `nombrecom` varchar(50) NOT NULL,
  `fechanac` date DEFAULT NULL,
  `sexo` char(1) DEFAULT NULL,
  `telefono` varchar(11) DEFAULT NULL,
  `email` varchar(250) DEFAULT NULL,
  `ciudad` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_user`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `dni` (`dni`),
  KEY `ciudad` (`ciudad`),
  CONSTRAINT `tbl_clientes_ibfk_1` FOREIGN KEY (`ciudad`) REFERENCES `tbl_ciudad` (`id_ciudad`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla e_commerce.tbl_clientes: ~33 rows (aproximadamente)
/*!40000 ALTER TABLE `tbl_clientes` DISABLE KEYS */;
INSERT IGNORE INTO `tbl_clientes` (`id_user`, `dni`, `nombrecom`, `fechanac`, `sexo`, `telefono`, `email`, `ciudad`) VALUES
	(1, NULL, 'Nacho Perez', '1985-03-08', 'M', '1232342312', 'telecompra@gmail.com', 1),
	(2, NULL, 'Carmen Martinez', '1987-08-15', 'F', '1234123535', 'telecompra1@gmail.com', 2),
	(3, NULL, 'Anibal Paniagua', '1946-04-14', 'M', '1234423535', 'telecompra2@gmail.com', 3),
	(4, NULL, 'Carina Paez', '1975-09-25', 'F', '1235443535', 'telecompra3@gmail.com', 1),
	(5, NULL, 'Andrea Casanay', '1999-06-01', 'F', '1245243535', 'telecompra4@gmail.com', 4),
	(6, NULL, 'Romina Palermo', '1965-04-18', 'F', '1232342316', 'compras@gmail.com', 1),
	(7, NULL, 'Lucas Mendoza', '1974-10-10', 'M', '1234123545', 'compras1@gmail.com', 2),
	(8, NULL, 'Pablo Calvo', '1996-11-02', 'M', '1234423568', 'compras2@gmail.com', 3),
	(9, NULL, 'Cristian Dominguez', '1985-09-15', 'M', '1235443599', 'compras3@gmail.com', 4),
	(10, NULL, 'Anibal Diaz', '1982-01-02', 'M', '1245243598', 'compras4@gmail.com', 5),
	(11, NULL, 'Ricardo Piedra', '1975-06-18', 'M', '1232342376', 'compras5@gmail.com', 1),
	(12, NULL, 'Maria Ruiz', '1993-12-10', 'F', '1234123522', 'compras6@gmail.com', 10),
	(13, NULL, 'Guillermo Pilo', '1986-06-24', 'M', '1234423558', 'compras7@gmail.com', 3),
	(14, NULL, 'Cristina Peralta', '1975-09-25', 'F', '1235443519', 'compras8@gmail.com', 2),
	(15, NULL, 'Anabel Carra', '1980-10-04', 'F', '1245241198', 'compras9@gmail.com', 6),
	(16, NULL, 'Raul Todetti', '1955-03-17', 'M', '1231142316', 'compras10@gmail.com', 1),
	(17, NULL, 'Rebecca Tarrima', '1992-11-02', 'F', '1234123506', 'compras11@gmail.com', 10),
	(18, NULL, 'Paulina Cocina', '1967-12-13', 'F', '1234421168', 'compras12@gmail.com', 4),
	(19, NULL, 'Dwight Schrute', '1969-06-10', 'M', '1235111599', 'compras13@gmail.com', 5),
	(20, NULL, 'Angela Martin', '1972-03-12', 'F', '1245241198', 'compras14@gmail.com', 6),
	(21, NULL, 'Oscar Martinez', '1971-08-18', 'M', '1232342303', 'compras15@gmail.com', 7),
	(22, NULL, 'Ciro Persa', '1990-02-26', 'M', '1234161422', 'compras16@gmail.com', 8),
	(23, NULL, 'Romina Gorritti', '1980-07-22', 'F', '1232523558', 'compras17@gmail.com', 9),
	(24, NULL, 'Sabrina Lee', '1969-03-13', 'F', '1235136519', 'compras18@gmail.com', 6),
	(25, NULL, 'Debora Lima', '1980-03-19', 'F', '1245241698', 'compras19@gmail.com', 2),
	(26, '95896376', 'Pedro Maneiro', '1985-09-10', 'M', '1121651051', 'pedromaneiro@gmail.com', 1),
	(27, NULL, 'Pedro Maneiro', '1985-09-10', 'M', '1121651051', 'pedromaneirgo@gmail.com', 1),
	(29, NULL, 'Pedro Maneiro', '1985-09-10', 'M', '1121651051', 'pedromane3irgo@gmail.com', 1),
	(30, NULL, 'Anita', '2020-11-21', 'F', '12345123', 'aquica@gmail.com', 2),
	(31, NULL, 'asd2', '2020-11-22', 'F', '1234567', '1234@gmail.com', 2),
	(32, NULL, 'Pedrito ito tio', '2020-11-20', 'M', '11234132', 'pedrito@gmail.com', 2),
	(33, NULL, 'Karina', '2020-11-17', 'F', '1122334411', 'karina@gmail.com', 1),
	(34, '95896377', 'Prueba Menu', '2020-11-20', 'F', '1122334455', 'test@test.com', 2),
	(40, '95896375', 'Vanessa', '2020-11-23', 'F', '112233112', 'vane@vane.com', 1);
/*!40000 ALTER TABLE `tbl_clientes` ENABLE KEYS */;

-- Volcando estructura para tabla e_commerce.tbl_compra
CREATE TABLE IF NOT EXISTS `tbl_compra` (
  `id_compra` int(11) NOT NULL AUTO_INCREMENT,
  `id_user` int(11) DEFAULT NULL,
  `id_producto` int(11) DEFAULT NULL,
  `id_methpago` int(11) DEFAULT NULL,
  `cantidad` decimal(10,3) DEFAULT NULL,
  `subtotal` decimal(10,3) DEFAULT NULL,
  PRIMARY KEY (`id_compra`),
  KEY `id_user` (`id_user`),
  KEY `id_producto` (`id_producto`),
  KEY `id_methpago` (`id_methpago`),
  CONSTRAINT `FK_tbl_compra_tbl_clientes` FOREIGN KEY (`id_user`) REFERENCES `tbl_clientes` (`id_user`) ON UPDATE NO ACTION,
  CONSTRAINT `tbl_compra_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `tbl_producto` (`id_Producto`),
  CONSTRAINT `tbl_compra_ibfk_3` FOREIGN KEY (`id_methpago`) REFERENCES `tbl_methpago` (`id_methpago`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla e_commerce.tbl_compra: ~23 rows (aproximadamente)
/*!40000 ALTER TABLE `tbl_compra` DISABLE KEYS */;
INSERT IGNORE INTO `tbl_compra` (`id_compra`, `id_user`, `id_producto`, `id_methpago`, `cantidad`, `subtotal`) VALUES
	(1, 2, 3, 3, 1.000, 55000.000),
	(2, 5, 2, 2, 1.000, 35000.000),
	(3, 4, 17, 1, 1.000, 28000.000),
	(4, 9, 26, 2, 1.000, 18000.000),
	(5, 18, 27, 3, 1.000, 21000.000),
	(6, 12, 16, 2, 1.000, 35000.000),
	(7, 25, 11, 3, 1.000, 75000.000),
	(8, 13, 15, 3, 1.000, 20000.000),
	(9, 16, 21, 1, 1.000, 180.000),
	(10, 23, 18, 4, 1.000, 40000.000),
	(11, 15, 19, 2, 1.000, 26000.000),
	(12, 7, 30, 3, 1.000, 130000.000),
	(13, 10, 13, 4, 1.000, 26000.000),
	(14, 22, 25, 1, 1.000, 125.000),
	(15, 6, 29, 2, 1.000, 30000.000),
	(16, 14, 23, 1, 3.000, 540.000),
	(17, 8, 27, 2, 1.000, 21000.000),
	(18, 13, 24, 1, 4.000, 280.000),
	(19, 19, 22, 1, 1.000, 170.000),
	(20, 21, 20, 5, 0.000, 16000.000),
	(22, 3, 3, 3, 1.000, 44000.000),
	(23, 32, 2, 4, 2.000, 3.000),
	(29, 3, 2, 4, 1.000, 2.000),
	(30, 32, 2, 2, 145.000, 23.000);
/*!40000 ALTER TABLE `tbl_compra` ENABLE KEYS */;

-- Volcando estructura para tabla e_commerce.tbl_marca
CREATE TABLE IF NOT EXISTS `tbl_marca` (
  `id_Marca` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`id_Marca`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla e_commerce.tbl_marca: ~10 rows (aproximadamente)
/*!40000 ALTER TABLE `tbl_marca` DISABLE KEYS */;
INSERT IGNORE INTO `tbl_marca` (`id_Marca`, `nombre`) VALUES
	(1, 'CANON'),
	(2, 'Samsung'),
	(3, 'Toshiba'),
	(4, 'TP Link'),
	(5, 'Sony'),
	(6, 'Nintendo'),
	(7, 'Microsoft'),
	(8, 'Apple'),
	(9, 'Motorola'),
	(10, 'Sanyo');
/*!40000 ALTER TABLE `tbl_marca` ENABLE KEYS */;

-- Volcando estructura para tabla e_commerce.tbl_methpago
CREATE TABLE IF NOT EXISTS `tbl_methpago` (
  `id_methpago` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(20) NOT NULL,
  PRIMARY KEY (`id_methpago`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla e_commerce.tbl_methpago: ~6 rows (aproximadamente)
/*!40000 ALTER TABLE `tbl_methpago` DISABLE KEYS */;
INSERT IGNORE INTO `tbl_methpago` (`id_methpago`, `tipo`) VALUES
	(1, 'EFECTIVO'),
	(2, 'DEBITO'),
	(3, 'CREDITO'),
	(4, 'GIFT CARD'),
	(5, 'MERCADOPAGO'),
	(7, 'pagofacil'),
	(8, 'Rapipago'),
	(9, 'Especio once');
/*!40000 ALTER TABLE `tbl_methpago` ENABLE KEYS */;

-- Volcando estructura para tabla e_commerce.tbl_producto
CREATE TABLE IF NOT EXISTS `tbl_producto` (
  `id_Producto` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(80) DEFAULT NULL,
  `modelo` varchar(50) DEFAULT NULL,
  `descripcion` varchar(50) DEFAULT NULL,
  `precio` decimal(10,3) DEFAULT NULL,
  `idCategoria` int(11) DEFAULT NULL,
  `idAlmacen` int(11) DEFAULT NULL,
  `idMarca` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_Producto`),
  UNIQUE KEY `modelo` (`modelo`),
  KEY `idCategoria` (`idCategoria`),
  KEY `idAlmacen` (`idAlmacen`),
  KEY `idMarca` (`idMarca`),
  CONSTRAINT `tbl_producto_ibfk_1` FOREIGN KEY (`idCategoria`) REFERENCES `tbl_categoria` (`id_Categoria`),
  CONSTRAINT `tbl_producto_ibfk_2` FOREIGN KEY (`idAlmacen`) REFERENCES `tbl_almacen` (`id_Almacen`),
  CONSTRAINT `tbl_producto_ibfk_3` FOREIGN KEY (`idMarca`) REFERENCES `tbl_marca` (`id_Marca`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla e_commerce.tbl_producto: ~29 rows (aproximadamente)
/*!40000 ALTER TABLE `tbl_producto` DISABLE KEYS */;
INSERT IGNORE INTO `tbl_producto` (`id_Producto`, `nombre`, `modelo`, `descripcion`, `precio`, `idCategoria`, `idAlmacen`, `idMarca`) VALUES
	(1, 'Iphone 7', '128gb', 'negro', 60000.000, 3, 3, 8),
	(2, 'Iphone 6s', '64 gb', 'Plateado', 35000.000, 3, 3, 8),
	(3, 'Laptop', 'K03SD3', '14 Pulgadas, i3, 4gb ram, ssd', 55000.000, 21, 3, 1),
	(4, 'Nintendo Swith', '3ADS323', 'Azul', 36000.000, 2, 3, 6),
	(5, 'PlayStation 4', '500gb', 'Slim', 40000.000, 2, 3, 5),
	(6, 'PlayStation 4', '1T', 'Negro', 42000.000, 2, 3, 5),
	(7, 'Wii', '250gb', 'Blanca', 35000.000, 2, 3, 6),
	(8, 'Tv Led 32', '41ASDF', '32 Pulgadas', 12000.000, 24, 3, 3),
	(9, 'Tv Smart 32', '5ASDD-A', '32 Pulgadas', 15000.000, 24, 3, 2),
	(11, 'Lavarropa', 'LG1698', 'Negro', 75000.000, 16, 2, 3),
	(12, 'Impresora', 'HP6698', 'Multifuncion', 25000.000, 21, 2, 1),
	(13, 'Aire Split', 'P45533', '33000 Frigorias', 26000.000, 4, 2, 10),
	(15, 'Cocina', 'A455SSQ', 'A gas', 20000.000, 15, 1, 3),
	(16, 'Anafe', '466ssA', 'Electrico', 35000.000, 15, 3, 10),
	(17, 'Heladera No Frost', '41ASDFA', '260 Lt', 28000.000, 17, 1, 5),
	(18, 'Heladera', 'HSAD99', '260 lt', 40000.000, 17, 1, 6),
	(19, 'Samsung A10', 'SAS9987', '64gb Negro', 26000.000, 3, 3, 2),
	(20, 'Samsung J7', 'J7SAAA', '32gb Blanco', 16000.000, 3, 3, 2),
	(21, 'Cerveza', 'cerveza', 'rubia 1L', 180.000, 7, 3, 3),
	(22, 'Cerveza', 'Rubia', 'Rubia 1l', 175.000, 7, 3, 9),
	(23, 'Cerveza', 'pinta', 'rubia 1L', 180.000, 7, 3, 5),
	(24, 'Cola', 'Coca-Cola', '1,25L', 70.000, 10, 3, 1),
	(25, 'Cola', 'Coca-ColaA', '2,25L', 125.000, 10, 3, 2),
	(26, 'Microondas', 'MS5556', 'Negro', 18000.000, 18, 1, 3),
	(27, 'Samsung Galaxy', 'A10SA', '32GB, Negro', 21000.000, 3, 3, 2),
	(28, 'Motorola E6', 'ES59998', '32GB, Negro', 17000.000, 3, 3, 9),
	(29, 'Motorola One', 'MOM598', '126GB, Macro', 30000.000, 3, 3, 9),
	(30, 'Motorola razr', 'MORAZ598', '126GB, plegable', 130000.000, 3, 3, 9),
	(31, 'Coca', 'cola', '3L', 200.000, 10, 3, 1),
	(32, 'agua clara', '32', '3L', 43.000, 7, 3, 8),
	(33, 'Monitor', '1439', '20", agregar y modificar', 4500.000, 24, 1, 5);
/*!40000 ALTER TABLE `tbl_producto` ENABLE KEYS */;

-- Volcando estructura para tabla e_commerce.tbl_usuarios
CREATE TABLE IF NOT EXISTS `tbl_usuarios` (
  `id_user` int(11) NOT NULL AUTO_INCREMENT,
  `nombrecom` varchar(50) NOT NULL,
  `telefono` varchar(11) DEFAULT NULL,
  `email` varchar(250) DEFAULT NULL,
  `password` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id_user`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla e_commerce.tbl_usuarios: ~7 rows (aproximadamente)
/*!40000 ALTER TABLE `tbl_usuarios` DISABLE KEYS */;
INSERT IGNORE INTO `tbl_usuarios` (`id_user`, `nombrecom`, `telefono`, `email`, `password`) VALUES
	(26, 'Pedro Maneiro', '1121651051', 'pedromaneiro@gmail.com', 'pedro1985'),
	(27, 'Pedro Maneiro', '1121651051', 'pedromaneirgo@gmail.com', 'pedro1985'),
	(29, 'Pedro Maneiro', '1121651051', 'pedromane3irgo@gmail.com', 'cGVkcm8xOTg1\n'),
	(30, 'Anita', '12345123', 'aquica@gmail.com', 'MTIzNDU2\n'),
	(31, 'asd2', '1234567', '1234@gmail.com', 'MTIzNDU2\n'),
	(32, 'Pedrito ito tio', '11234132', 'pedrito@gmail.com', 'MTIzNDU2\n'),
	(33, 'Pedro MAneiro en Alta', '1122334455', 'admin@admin.com', 'cGVkcm8xMjM=\n'),
	(34, 'Sofia Barbona', '112233112', 'sofi@sofi.com', 'MTIzNDU2\n');
/*!40000 ALTER TABLE `tbl_usuarios` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
