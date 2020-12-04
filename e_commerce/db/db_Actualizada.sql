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

-- Volcando datos para la tabla e_commerce.tbl_almacen: ~7 rows (aproximadamente)
/*!40000 ALTER TABLE `tbl_almacen` DISABLE KEYS */;
INSERT IGNORE INTO `tbl_almacen` (`id_Almacen`, `tipo`) VALUES
	(1, 'Deposito1'),
	(2, 'Deposito2'),
	(3, 'Mostrador'),
	(5, 'Exhibidor'),
	(6, 'Deposito2'),
	(7, 'sd2s'),
	(8, 'Pruebadevenano');
/*!40000 ALTER TABLE `tbl_almacen` ENABLE KEYS */;

-- Volcando estructura para tabla e_commerce.tbl_categoria
CREATE TABLE IF NOT EXISTS `tbl_categoria` (
  `id_Categoria` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`id_Categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla e_commerce.tbl_categoria: ~27 rows (aproximadamente)
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
	(29, 'disco externo');
/*!40000 ALTER TABLE `tbl_categoria` ENABLE KEYS */;

-- Volcando estructura para tabla e_commerce.tbl_ciudad
CREATE TABLE IF NOT EXISTS `tbl_ciudad` (
  `id_ciudad` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(40) NOT NULL,
  PRIMARY KEY (`id_ciudad`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla e_commerce.tbl_ciudad: ~27 rows (aproximadamente)
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
	(1, '95784324', 'Nacho Perez', '1985-03-08', 'M', '1232342312', 'telecompra@gmail.com', 1),
	(2, '95784325', 'Carmen Martinez', '1987-08-15', 'F', '1234123535', 'telecompra1@gmail.com', 2),
	(3, '95784326', 'Anibal Paniagua', '1946-04-14', 'M', '1234423535', 'telecompra2@gmail.com', 3),
	(4, '95784327', 'Carina Paez', '1975-09-25', 'F', '1235443535', 'telecompra3@gmail.com', 1),
	(5, '95784328', 'Andrea Casanay', '1999-06-01', 'F', '1245243535', 'telecompra4@gmail.com', 4),
	(6, '95784329', 'Romina Palermo', '1965-04-18', 'F', '1232342316', 'compras@gmail.com', 1),
	(7, '95784321', 'Lucas Mendoza', '1974-10-10', 'M', '1234123545', 'compras1@gmail.com', 2),
	(8, '95784322', 'Pablo Calvo', '1996-11-02', 'M', '1234423568', 'compras2@gmail.com', 3),
	(9, '95784323', 'Cristian Dominguez', '1985-09-15', 'M', '1235443599', 'compras3@gmail.com', 4),
	(10, '95784450', 'Anibal Diaz', '1982-01-02', 'M', '1245243598', 'compras4@gmail.com', 5),
	(11, '95784451', 'Ricardo Piedra', '1975-06-18', 'M', '1232342376', 'compras5@gmail.com', 1),
	(12, '95784452', 'Maria Ruiz', '1993-12-10', 'F', '1234123522', 'compras6@gmail.com', 10),
	(13, '95784453', 'Guillermo Pilo', '1986-06-24', 'M', '1234423558', 'compras7@gmail.com', 3),
	(14, '95784454', 'Cristina Peralta', '1975-09-25', 'F', '1235443519', 'compras8@gmail.com', 2),
	(15, '95784455', 'Anabel Carra', '1980-10-04', 'F', '1245241198', 'compras9@gmail.com', 6),
	(16, '95784456', 'Raul Todetti', '1955-03-17', 'M', '1231142316', 'compras10@gmail.com', 1),
	(17, '95784457', 'Rebecca Tarrima', '1992-11-02', 'F', '1234123506', 'compras11@gmail.com', 10),
	(18, '95784458', 'Paulina Cocina', '1967-12-13', 'F', '1234421168', 'compras12@gmail.com', 4),
	(19, '95784459', 'Dwight Schrute', '1969-06-10', 'M', '1235111599', 'compras13@gmail.com', 5),
	(20, '95784460', 'Angela Martin', '1972-03-12', 'F', '1245241198', 'compras14@gmail.com', 6),
	(21, '95784461', 'Oscar Martinez', '1971-08-18', 'M', '1232342303', 'compras15@gmail.com', 7),
	(22, '95784462', 'Ciro Persa', '1990-02-26', 'M', '1234161422', 'compras16@gmail.com', 8),
	(23, '95784463', 'Romina Gorritti', '1980-07-22', 'F', '1232523558', 'compras17@gmail.com', 9),
	(24, '95784464', 'Sabrina Lee', '1969-03-13', 'F', '1235136519', 'compras18@gmail.com', 6),
	(25, '95784465', 'Debora Lima', '1980-03-19', 'F', '1245241698', 'compras19@gmail.com', 2),
	(26, '95896376', 'Pedro Maneiro', '1985-09-10', 'M', '1121651051', 'pedromaneiro@gmail.com', 1),
	(27, '95784466', 'Pedro Maneiro', '1985-09-10', 'M', '1121651051', 'pedromaneirgo@gmail.com', 1),
	(29, '12345', 'Pedro Maneiro', '1985-09-10', 'M', '1121651051', 'pedromane3irgo@gmail.com', 1),
	(30, '123455', 'Anita', '2020-11-21', 'F', '12345123', 'aquica@gmail.com', 2),
	(32, '95784467', 'Pedrito ito tio', '2020-11-20', 'M', '11234132', 'pedrito@gmail.com', 2),
	(33, '95784468', 'Karina', '2020-11-17', 'F', '1122334411', 'karina@gmail.com', 1),
	(34, '95896377', 'Prueba1204', '2020-12-04', 'F', '1122334455', 'test@test.com', 14),
	(40, '95896375', 'Vanessa', '2020-11-23', 'F', '112233112', 'vane@vane.com', 1);
/*!40000 ALTER TABLE `tbl_clientes` ENABLE KEYS */;

-- Volcando estructura para tabla e_commerce.tbl_compra
CREATE TABLE IF NOT EXISTS `tbl_compra` (
  `id_compra` int(3) DEFAULT NULL,
  `id_compra_cant` int(5) NOT NULL AUTO_INCREMENT,
  `id_user` int(11) DEFAULT NULL,
  `id_producto` int(11) DEFAULT NULL,
  `id_methpago` int(11) DEFAULT NULL,
  `cantidad` decimal(10,3) DEFAULT NULL,
  `subtotal` decimal(10,3) DEFAULT NULL,
  PRIMARY KEY (`id_compra_cant`) USING BTREE,
  KEY `id_user` (`id_user`),
  KEY `id_producto` (`id_producto`),
  KEY `id_methpago` (`id_methpago`),
  CONSTRAINT `FK_tbl_compra_tbl_clientes` FOREIGN KEY (`id_user`) REFERENCES `tbl_clientes` (`id_user`) ON UPDATE NO ACTION,
  CONSTRAINT `tbl_compra_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `tbl_producto` (`id_Producto`),
  CONSTRAINT `tbl_compra_ibfk_3` FOREIGN KEY (`id_methpago`) REFERENCES `tbl_methpago` (`id_methpago`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla e_commerce.tbl_compra: ~86 rows (aproximadamente)
/*!40000 ALTER TABLE `tbl_compra` DISABLE KEYS */;
INSERT IGNORE INTO `tbl_compra` (`id_compra`, `id_compra_cant`, `id_user`, `id_producto`, `id_methpago`, `cantidad`, `subtotal`) VALUES
	(1, 1, 2, 3, 3, 1.000, 55000.000),
	(2, 2, 5, 2, 2, 1.000, 35000.000),
	(3, 3, 4, 17, 1, 1.000, 28000.000),
	(4, 4, 9, 26, 2, 1.000, 18000.000),
	(5, 5, 18, 27, 3, 1.000, 21000.000),
	(6, 6, 12, 16, 2, 1.000, 35000.000),
	(7, 7, 25, 11, 3, 1.000, 75000.000),
	(8, 8, 13, 15, 3, 1.000, 20000.000),
	(9, 9, 16, 21, 1, 1.000, 180.000),
	(10, 10, 23, 18, 4, 1.000, 40000.000),
	(11, 11, 15, 19, 2, 1.000, 26000.000),
	(12, 12, 7, 30, 3, 1.000, 130000.000),
	(13, 13, 10, 13, 4, 1.000, 26000.000),
	(14, 14, 22, 25, 1, 1.000, 125.000),
	(15, 15, 6, 29, 2, 1.000, 30000.000),
	(16, 16, 14, 23, 1, 3.000, 540.000),
	(17, 17, 8, 27, 2, 1.000, 21000.000),
	(18, 18, 13, 24, 1, 4.000, 280.000),
	(19, 19, 19, 22, 1, 1.000, 170.000),
	(20, 20, 21, 20, 5, 0.000, 16000.000),
	(21, 22, 3, 3, 3, 1.000, 44000.000),
	(22, 23, 32, 2, 4, 2.000, 3.000),
	(23, 29, 3, 2, 4, 1.000, 2.000),
	(24, 30, 32, 2, 2, 145.000, 23.000),
	(25, 31, 23, 1, 2, 1.000, 180000.000),
	(26, 32, 40, 25, 1, 1.000, 120.000),
	(27, 41, 1, 1, 1, 1.000, 90.000),
	(27, 42, 1, 2, 1, 1.000, 91.000),
	(28, 43, 2, 3, 1, 1.000, 98.000),
	(28, 44, 2, 5, 2, 1.000, 234.000),
	(29, 45, 12, 25, 1, 1.000, 234.000),
	(30, 46, 11, 23, 1, 2.000, 123.000),
	(31, 47, 9, 8, 1, 1.000, 2300.000),
	(31, 48, 9, 17, 1, 1.000, 2342.000),
	(32, 49, 33, 30, 1, 1.000, 123.000),
	(32, 50, 33, 33, 3, 1.000, 32.000),
	(33, 51, 24, 15, 1, 1.000, 234.000),
	(33, 52, 24, 20, 1, 1.000, 300.000),
	(33, 53, 24, 7, 1, 1.000, 18.000),
	(33, 54, 24, 23, 1, 1.000, 23.000),
	(34, 55, 1, 4, 1, 1.000, 900.000),
	(34, 56, 1, 8, 1, 1.000, 759.000),
	(34, 57, 1, 23, 1, 1.000, 234.000),
	(34, 58, 1, 29, 1, 1.000, 1750.000),
	(35, 59, 1, 2, 1, 1.000, 23.000),
	(36, 60, 1, 2, 1, 1.000, 1.000),
	(37, 61, 1, 1, 1, 1.000, 1.000),
	(38, 62, 1, 1, 1, 1.000, 1.000),
	(39, 63, 1, 1, 1, 1.000, 1.000),
	(40, 64, 1, 1, 1, 1.000, 1.000),
	(41, 65, 11, 1, 1, 1.000, 1.000),
	(42, 66, 1, 1, 1, 1.000, 1.000),
	(43, 67, 1, 1, 1, 1.000, 1.000),
	(44, 68, 1, 2, 1, 1.000, 1.000),
	(45, 69, 1, 1, 1, 1.000, 1.000),
	(46, 70, 1, 2, 1, 1.000, 1.000),
	(46, 71, 1, 1, 2, 3.000, 1.000),
	(47, 72, 1, 1, 1, 1.000, 1.000),
	(48, 73, 1, 1, 1, 1.000, 1.000),
	(49, 74, 1, 1, 1, 1.000, 1.000),
	(50, 75, 1, 1, 1, 1.000, 1.000),
	(51, 76, 1, 1, 1, 1.000, 1.000),
	(52, 77, 1, 1, 1, 1.000, 1.000),
	(53, 78, 1, 1, 1, 1.000, 1.000),
	(54, 79, 1, 1, 1, 1.000, 1.000),
	(55, 80, 1, 1, 1, 1.000, 1.000),
	(56, 81, 1, 1, 1, 1.000, 1.000),
	(57, 82, 1, 2, 2, 2.000, 2.000),
	(57, 83, 3, 3, 1, 3.000, 3.000),
	(58, 84, 1, 2, 3, 4.000, 5.000),
	(59, 85, 1, 2, 3, 4.000, 5.000),
	(60, 86, 4, 4, 4, 4.000, 4.000),
	(61, 87, 1, 2, 3, 4.000, 1.000),
	(62, 88, 1, 1, 1, 1.000, 1.000),
	(63, 89, 2, 3, 1, 2.000, 3.000),
	(64, 90, 1, 2, 3, 4.000, 1.000),
	(65, 91, 1, 2, 3, 1.000, 2.000),
	(66, 92, 1, 2, 3, 4.000, 5.000),
	(66, 93, 1, 2, 3, 4.000, 5.000),
	(67, 94, 1, 2, 2, 1.000, 1.000),
	(67, 95, 1, 4, 3, 3.000, 2.000),
	(68, 96, 1, 2, 3, 4.000, 99.000),
	(68, 97, 1, 2, 3, 4.000, 5.000),
	(69, 98, 1, 2, 3, 4.000, 5.000),
	(69, 99, 1, 2, 3, 4.000, 234.000),
	(69, 100, 5, 4, 3, 2.000, 233.000);
/*!40000 ALTER TABLE `tbl_compra` ENABLE KEYS */;

-- Volcando estructura para tabla e_commerce.tbl_marca
CREATE TABLE IF NOT EXISTS `tbl_marca` (
  `id_Marca` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(80) DEFAULT NULL,
  `activo` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id_Marca`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla e_commerce.tbl_marca: ~11 rows (aproximadamente)
/*!40000 ALTER TABLE `tbl_marca` DISABLE KEYS */;
INSERT IGNORE INTO `tbl_marca` (`id_Marca`, `nombre`, `activo`) VALUES
	(1, 'CANON', 0),
	(2, 'Samsung', 0),
	(3, 'Toshiba', 0),
	(4, 'TP Link', 0),
	(5, 'Sony', 0),
	(6, 'Nintendo', 0),
	(7, 'Microsoft', 0),
	(8, 'Apple', 0),
	(9, 'Motorola', 0),
	(10, 'Sanyo', 0),
	(12, 'd', 0);
/*!40000 ALTER TABLE `tbl_marca` ENABLE KEYS */;

-- Volcando estructura para tabla e_commerce.tbl_methpago
CREATE TABLE IF NOT EXISTS `tbl_methpago` (
  `id_methpago` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(20) NOT NULL,
  PRIMARY KEY (`id_methpago`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla e_commerce.tbl_methpago: ~7 rows (aproximadamente)
/*!40000 ALTER TABLE `tbl_methpago` DISABLE KEYS */;
INSERT IGNORE INTO `tbl_methpago` (`id_methpago`, `tipo`) VALUES
	(1, 'EFECTIVO'),
	(2, 'DEBITO'),
	(3, 'CREDITO'),
	(4, 'GIFT CARD'),
	(5, 'MERCADOPAGO'),
	(7, 'pagofacil'),
	(8, 'Rapipago');
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
  `activo` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id_Producto`),
  UNIQUE KEY `modelo` (`modelo`),
  KEY `idCategoria` (`idCategoria`),
  KEY `idAlmacen` (`idAlmacen`),
  KEY `idMarca` (`idMarca`),
  CONSTRAINT `tbl_producto_ibfk_1` FOREIGN KEY (`idCategoria`) REFERENCES `tbl_categoria` (`id_Categoria`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tbl_producto_ibfk_2` FOREIGN KEY (`idAlmacen`) REFERENCES `tbl_almacen` (`id_Almacen`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tbl_producto_ibfk_3` FOREIGN KEY (`idMarca`) REFERENCES `tbl_marca` (`id_Marca`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla e_commerce.tbl_producto: ~31 rows (aproximadamente)
/*!40000 ALTER TABLE `tbl_producto` DISABLE KEYS */;
INSERT IGNORE INTO `tbl_producto` (`id_Producto`, `nombre`, `modelo`, `descripcion`, `precio`, `idCategoria`, `idAlmacen`, `idMarca`, `activo`) VALUES
	(1, 'Iphone 7', '128gb', 'negro', 60000.000, 3, 3, 8, 0),
	(2, 'Iphone 6s', '64 gb', 'Plateado', 35000.000, 3, 3, 8, 0),
	(3, 'Laptop', 'K03SD3', '14 Pulgadas, i3, 4gb ram, ssd', 55000.000, 21, 3, 1, 0),
	(4, 'Nintendo Swith', '3ADS323', 'Azul', 36000.000, 2, 3, 6, 0),
	(5, 'PlayStation 4', '500gb', 'Slim', 40000.000, 2, 3, 5, 0),
	(6, 'PlayStation 4', '1T', 'Negro', 42000.000, 2, 3, 5, 0),
	(7, 'Wii', '250gb', 'Blanca', 35000.000, 2, 3, 6, 0),
	(8, 'Tv Led 32', '41ASDF', '32 Pulgadas', 12000.000, 24, 3, 3, 0),
	(9, 'Tv Smart 32', '5ASDD-A', '32 Pulgadas', 15000.000, 24, 3, 2, 0),
	(11, 'Lavarropa', 'LG1698', 'Negro', 75000.000, 16, 2, 3, 0),
	(12, 'Impresora', 'HP6698', 'Multifuncion', 25000.000, 21, 2, 1, 0),
	(13, 'Aire Split', 'P45533', '33000 Frigorias', 26000.000, 4, 2, 10, 0),
	(15, 'Cocina', 'A455SSQ', 'A gas', 20000.000, 15, 1, 3, 0),
	(16, 'Anafe', '466ssA', 'Electrico', 35000.000, 15, 3, 10, 0),
	(17, 'Heladera No Frost', '41ASDFA', '260 Lt', 28000.000, 17, 1, 5, 0),
	(18, 'Heladera', 'HSAD99', '260 lt', 40000.000, 17, 1, 6, 0),
	(19, 'Samsung A10', 'SAS9987', '64gb Negro', 26000.000, 3, 3, 2, 0),
	(20, 'Samsung J7', 'J7SAAA', '32gb Blanco', 16000.000, 3, 3, 2, 0),
	(21, 'Cerveza', 'cerveza', 'rubia 1L', 180.000, 7, 3, 3, 0),
	(22, 'Cerveza', 'Rubia', 'Rubia 1l', 175.000, 7, 3, 9, 1),
	(23, 'Cerveza', 'pinta', 'rubia 1L', 180.000, 7, 3, 5, 0),
	(24, 'Cola', 'Coca-Cola', '1,25L', 70.000, 10, 3, 1, 0),
	(25, 'Cola', 'Coca-ColaA', '2,25L', 125.000, 10, 3, 2, 0),
	(26, 'Microondas', 'MS5556', 'Negro', 18000.000, 18, 1, 3, 0),
	(27, 'Samsung Galaxy', 'A10SA', '32GB, Negro', 21000.000, 3, 3, 2, 0),
	(28, 'Motorola E6', 'ES59998', '32GB, Negro', 17000.000, 3, 3, 9, 0),
	(29, 'Motorola One', 'MOM598', '126GB, Macro', 30000.000, 3, 3, 9, 0),
	(30, 'Motorola razr', 'MORAZ598', '126GB, plegable', 130000.000, 3, 3, 9, 0),
	(31, 'Coca', 'cola', '3L', 200.000, 10, 3, 1, 0),
	(32, 'agua clara', '32', '3L', 43.000, 7, 3, 8, 0),
	(33, 'Monitor', '1439', '20", agregar y modificar', 4500.000, 24, 1, 5, 1);
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

-- Volcando datos para la tabla e_commerce.tbl_usuarios: ~8 rows (aproximadamente)
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
