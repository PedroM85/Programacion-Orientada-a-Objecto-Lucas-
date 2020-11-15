-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.7.24 - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             11.1.0.6116
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for e_commerce
CREATE DATABASE IF NOT EXISTS `e_commerce` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `e_commerce`;

-- Dumping structure for table e_commerce.tbl_almacen
CREATE TABLE IF NOT EXISTS `tbl_almacen` (
  `id_Almacen` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`id_Almacen`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- Dumping data for table e_commerce.tbl_almacen: ~3 rows (approximately)
/*!40000 ALTER TABLE `tbl_almacen` DISABLE KEYS */;
INSERT INTO `tbl_almacen` (`id_Almacen`, `tipo`) VALUES
	(1, 'Deposito1'),
	(2, 'Deposito2'),
	(3, 'Mostrador');
/*!40000 ALTER TABLE `tbl_almacen` ENABLE KEYS */;

-- Dumping structure for table e_commerce.tbl_categoria
CREATE TABLE IF NOT EXISTS `tbl_categoria` (
  `id_Categoria` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`id_Categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

-- Dumping data for table e_commerce.tbl_categoria: ~24 rows (approximately)
/*!40000 ALTER TABLE `tbl_categoria` DISABLE KEYS */;
INSERT INTO `tbl_categoria` (`id_Categoria`, `tipo`) VALUES
	(1, 'Electrodomesticos'),
	(2, 'Consolas y videojuegos'),
	(3, 'Celulares'),
	(4, 'Aires Acondicionados'),
	(5, 'Informatica'),
	(6, 'Comida'),
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
	(24, 'Televisores');
/*!40000 ALTER TABLE `tbl_categoria` ENABLE KEYS */;

-- Dumping structure for table e_commerce.tbl_ciudad
CREATE TABLE IF NOT EXISTS `tbl_ciudad` (
  `id_ciudad` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(40) NOT NULL,
  PRIMARY KEY (`id_ciudad`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

-- Dumping data for table e_commerce.tbl_ciudad: ~25 rows (approximately)
/*!40000 ALTER TABLE `tbl_ciudad` DISABLE KEYS */;
INSERT INTO `tbl_ciudad` (`id_ciudad`, `nombre`) VALUES
	(1, 'BUENOS AIRES'),
	(2, 'CAPITAL FEDERAL'),
	(3, 'CATAMARCA'),
	(4, 'CHACO'),
	(5, 'CHUBUT'),
	(6, 'CORDOBA'),
	(7, 'CORRIENTES'),
	(8, 'ENTRE RIOS'),
	(9, 'FORMOSA'),
	(10, 'JUJUY'),
	(11, 'LA PAMPA'),
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
	(25, 'TUCUMAN');
/*!40000 ALTER TABLE `tbl_ciudad` ENABLE KEYS */;

-- Dumping structure for table e_commerce.tbl_compra
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
  CONSTRAINT `tbl_compra_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `tbl_usuarios1` (`id_user`),
  CONSTRAINT `tbl_compra_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `tbl_producto` (`id_Producto`),
  CONSTRAINT `tbl_compra_ibfk_3` FOREIGN KEY (`id_methpago`) REFERENCES `tbl_methpago` (`id_methpago`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

-- Dumping data for table e_commerce.tbl_compra: ~20 rows (approximately)
/*!40000 ALTER TABLE `tbl_compra` DISABLE KEYS */;
INSERT INTO `tbl_compra` (`id_compra`, `id_user`, `id_producto`, `id_methpago`, `cantidad`, `subtotal`) VALUES
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
	(20, 21, 20, 5, 0.000, 16000.000);
/*!40000 ALTER TABLE `tbl_compra` ENABLE KEYS */;

-- Dumping structure for table e_commerce.tbl_marca
CREATE TABLE IF NOT EXISTS `tbl_marca` (
  `id_Marca` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`id_Marca`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

-- Dumping data for table e_commerce.tbl_marca: ~20 rows (approximately)
/*!40000 ALTER TABLE `tbl_marca` DISABLE KEYS */;
INSERT INTO `tbl_marca` (`id_Marca`, `nombre`) VALUES
	(1, 'HP'),
	(2, 'Samsung'),
	(3, 'Toshiba'),
	(4, 'TP Link'),
	(5, 'Sony'),
	(6, 'Nintendo'),
	(7, 'Microsoft'),
	(8, 'Apple'),
	(9, 'Motorola'),
	(10, 'Sanyo'),
	(11, 'Phillips'),
	(12, 'Philco'),
	(13, 'LG'),
	(14, 'Panasonic'),
	(15, 'Coca-Cola'),
	(16, 'Sprite'),
	(17, 'Ser'),
	(18, 'Quilmes'),
	(19, 'Stella Artois'),
	(20, 'Patagonia');
/*!40000 ALTER TABLE `tbl_marca` ENABLE KEYS */;

-- Dumping structure for table e_commerce.tbl_methpago
CREATE TABLE IF NOT EXISTS `tbl_methpago` (
  `id_methpago` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(20) NOT NULL,
  PRIMARY KEY (`id_methpago`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

-- Dumping data for table e_commerce.tbl_methpago: ~5 rows (approximately)
/*!40000 ALTER TABLE `tbl_methpago` DISABLE KEYS */;
INSERT INTO `tbl_methpago` (`id_methpago`, `tipo`) VALUES
	(1, 'EFECTIVO'),
	(2, 'DEBITO'),
	(3, 'CREDITO'),
	(4, 'GIFT CARD'),
	(5, 'MERCADOPAGO');
/*!40000 ALTER TABLE `tbl_methpago` ENABLE KEYS */;

-- Dumping structure for table e_commerce.tbl_producto
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
  KEY `idCategoria` (`idCategoria`),
  KEY `idAlmacen` (`idAlmacen`),
  KEY `idMarca` (`idMarca`),
  CONSTRAINT `tbl_producto_ibfk_1` FOREIGN KEY (`idCategoria`) REFERENCES `tbl_categoria` (`id_Categoria`),
  CONSTRAINT `tbl_producto_ibfk_2` FOREIGN KEY (`idAlmacen`) REFERENCES `tbl_almacen` (`id_Almacen`),
  CONSTRAINT `tbl_producto_ibfk_3` FOREIGN KEY (`idMarca`) REFERENCES `tbl_marca` (`id_Marca`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

-- Dumping data for table e_commerce.tbl_producto: ~30 rows (approximately)
/*!40000 ALTER TABLE `tbl_producto` DISABLE KEYS */;
INSERT INTO `tbl_producto` (`id_Producto`, `nombre`, `modelo`, `descripcion`, `precio`, `idCategoria`, `idAlmacen`, `idMarca`) VALUES
	(1, 'Iphone 7', '128gb', 'negro', 60000.000, 3, 3, 8),
	(2, 'Iphone 6s', '64 gb', 'Plateado', 35000.000, 3, 3, 8),
	(3, 'Laptop', 'K03SD3', '14 Pulgadas, i3, 4gb ram, ssd', 55000.000, 21, 3, 1),
	(4, 'Nintendo Swith', '3ADS323', 'Azul', 36000.000, 2, 3, 6),
	(5, 'PlayStation 4', '500gb', 'Slim', 40000.000, 2, 3, 5),
	(6, 'PlayStation 4', '1T', 'Negro', 42000.000, 2, 3, 5),
	(7, 'Wii', '250gb', 'Blanca', 35000.000, 2, 3, 6),
	(8, 'Tv Led 32', '41ASDF', '32 Pulgadas', 12000.000, 24, 3, 13),
	(9, 'Tv Smart 32', '5ASDD-A', '32 Pulgadas', 15000.000, 24, 3, 2),
	(10, 'Tv Led 52', '1CQ22', '52 pulgadas', 80000.000, 24, 3, 11),
	(11, 'Lavarropa', 'LG1698', 'Negro', 75000.000, 16, 2, 13),
	(12, 'Impresora', 'HP6698', 'Multifuncion', 25000.000, 21, 2, 1),
	(13, 'Aire Split', 'P45533', '33000 Frigorias', 26000.000, 4, 2, 10),
	(14, 'Aire Split', 'SA555S', '40000 Frigorias', 32000.000, 4, 2, 11),
	(15, 'Cocina', 'A455SSQ', 'A gas', 20000.000, 15, 1, 13),
	(16, 'Anafe', '466ssA', 'Electrico', 35000.000, 15, 3, 10),
	(17, 'Heladera No Frost', '41ASDF', '260 Lt', 28000.000, 17, 1, 12),
	(18, 'Heladera', 'HSAD99', '260 lt', 40000.000, 17, 1, 11),
	(19, 'Samsung A10', 'SAS9987', '64gb Negro', 26000.000, 3, 3, 2),
	(20, 'Samsung J7', 'J7SAAA', '32gb Blanco', 16000.000, 3, 3, 2),
	(21, 'Cerveza', 'cerveza', 'rubia 1L', 180.000, 7, 3, 20),
	(22, 'Cerveza', 'cerveza', 'negra 1L', 170.000, 7, 3, 20),
	(23, 'Cerveza', 'cerveza', 'rubia 1L', 180.000, 7, 3, 19),
	(24, 'Cola', 'Coca-Cola', '1,25L', 70.000, 10, 3, 15),
	(25, 'Cola', 'Coca-Cola', '2,25L', 125.000, 10, 3, 15),
	(26, 'Microondas', 'MS5556', 'Negro', 18000.000, 18, 1, 14),
	(27, 'Samsung Galaxy', 'A10SA', '32GB, Negro', 21000.000, 3, 3, 2),
	(28, 'Motorola E6', 'ES59998', '32GB, Negro', 17000.000, 3, 3, 9),
	(29, 'Motorola One', 'MOM598', '126GB, Macro', 30000.000, 3, 3, 9),
	(30, 'Motorola razr', 'MORAZ598', '126GB, plegable', 130000.000, 3, 3, 9);
/*!40000 ALTER TABLE `tbl_producto` ENABLE KEYS */;

-- Dumping structure for table e_commerce.tbl_usuarios
CREATE TABLE IF NOT EXISTS `tbl_usuarios` (
  `id_user` int(11) NOT NULL AUTO_INCREMENT,
  `nombrecom` varchar(50) NOT NULL,
  `fechanac` date DEFAULT NULL,
  `sexo` char(1) DEFAULT NULL,
  `telefono` int(11) DEFAULT NULL,
  `email` varchar(250) DEFAULT NULL,
  `ciudad` int(11) DEFAULT NULL,
  `password` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id_user`),
  UNIQUE KEY `email` (`email`),
  KEY `ciudad` (`ciudad`),
  CONSTRAINT `tbl_usuarios_ibfk_1` FOREIGN KEY (`ciudad`) REFERENCES `tbl_ciudad` (`id_ciudad`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;

-- Dumping data for table e_commerce.tbl_usuarios: ~28 rows (approximately)
/*!40000 ALTER TABLE `tbl_usuarios` DISABLE KEYS */;
INSERT INTO `tbl_usuarios` (`id_user`, `nombrecom`, `fechanac`, `sexo`, `telefono`, `email`, `ciudad`, `password`) VALUES
	(1, 'Nacho Perez', '1985-03-08', 'M', 1232342312, 'telecompra@gmail.com', 1, NULL),
	(2, 'Carmen Martinez', '1987-08-15', 'F', 1234123535, 'telecompra1@gmail.com', 2, NULL),
	(3, 'Anibal Paniagua', '1946-04-14', 'M', 1234423535, 'telecompra2@gmail.com', 3, NULL),
	(4, 'Carina Paez', '1975-09-25', 'F', 1235443535, 'telecompra3@gmail.com', 1, NULL),
	(5, 'Andrea Casanay', '1999-06-01', 'F', 1245243535, 'telecompra4@gmail.com', 4, NULL),
	(6, 'Romina Palermo', '1965-04-18', 'F', 1232342316, 'compras@gmail.com', 1, NULL),
	(7, 'Lucas Mendoza', '1974-10-10', 'M', 1234123545, 'compras1@gmail.com', 2, NULL),
	(8, 'Pablo Calvo', '1996-11-02', 'M', 1234423568, 'compras2@gmail.com', 3, NULL),
	(9, 'Cristian Dominguez', '1985-09-15', 'M', 1235443599, 'compras3@gmail.com', 4, NULL),
	(10, 'Anibal Diaz', '1982-01-02', 'M', 1245243598, 'compras4@gmail.com', 5, NULL),
	(11, 'Ricardo Piedra', '1975-06-18', 'M', 1232342376, 'compras5@gmail.com', 1, NULL),
	(12, 'Maria Ruiz', '1993-12-10', 'F', 1234123522, 'compras6@gmail.com', 15, NULL),
	(13, 'Guillermo Pilo', '1986-06-24', 'M', 1234423558, 'compras7@gmail.com', 14, NULL),
	(14, 'Cristina Peralta', '1975-09-25', 'F', 1235443519, 'compras8@gmail.com', 12, NULL),
	(15, 'Anabel Carra', '1980-10-04', 'F', 1245241198, 'compras9@gmail.com', 6, NULL),
	(16, 'Raul Todetti', '1955-03-17', 'M', 1231142316, 'compras10@gmail.com', 1, NULL),
	(17, 'Rebecca Tarrima', '1992-11-02', 'F', 1234123506, 'compras11@gmail.com', 10, NULL),
	(18, 'Paulina Cocina', '1967-12-13', 'F', 1234421168, 'compras12@gmail.com', 14, NULL),
	(19, 'Dwight Schrute', '1969-06-10', 'M', 1235111599, 'compras13@gmail.com', 24, NULL),
	(20, 'Angela Martin', '1972-03-12', 'F', 1245241198, 'compras14@gmail.com', 20, NULL),
	(21, 'Oscar Martinez', '1971-08-18', 'M', 1232342303, 'compras15@gmail.com', 19, NULL),
	(22, 'Ciro Persa', '1990-02-26', 'M', 1234161422, 'compras16@gmail.com', 8, NULL),
	(23, 'Romina Gorritti', '1980-07-22', 'F', 1232523558, 'compras17@gmail.com', 12, NULL),
	(24, 'Sabrina Lee', '1969-03-13', 'F', 1235136519, 'compras18@gmail.com', 6, NULL),
	(25, 'Debora Lima', '1980-03-19', 'F', 1245241698, 'compras19@gmail.com', 22, NULL),
	(26, 'Pedro Maneiro', '1985-09-10', 'M', 1121651051, 'pedromaneiro@gmail.com', 1, 'pedro1985'),
	(27, 'Pedro Maneiro', '1985-09-10', 'M', 1121651051, 'pedromaneirgo@gmail.com', 1, 'pedro1985'),
	(29, 'Pedro Maneiro', '1985-09-10', 'M', 1121651051, 'pedromane3irgo@gmail.com', 1, 'cGVkcm8xOTg1\n');
/*!40000 ALTER TABLE `tbl_usuarios` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
