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

-- Data exporting was unselected.

-- Dumping structure for table e_commerce.tbl_categoria
CREATE TABLE IF NOT EXISTS `tbl_categoria` (
  `id_Categoria` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`id_Categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table e_commerce.tbl_ciudad
CREATE TABLE IF NOT EXISTS `tbl_ciudad` (
  `id_ciudad` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(40) NOT NULL,
  PRIMARY KEY (`id_ciudad`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

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

-- Data exporting was unselected.

-- Dumping structure for table e_commerce.tbl_marca
CREATE TABLE IF NOT EXISTS `tbl_marca` (
  `id_Marca` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`id_Marca`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

-- Dumping structure for table e_commerce.tbl_methpago
CREATE TABLE IF NOT EXISTS `tbl_methpago` (
  `id_methpago` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(20) NOT NULL,
  PRIMARY KEY (`id_methpago`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

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

-- Data exporting was unselected.

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

-- Data exporting was unselected.

-- Dumping structure for table e_commerce.tbl_usuarios1
CREATE TABLE IF NOT EXISTS `tbl_usuarios1` (
  `id_user` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) NOT NULL,
  `apellido` varchar(20) NOT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `sexo` char(1) DEFAULT NULL,
  `telefono` int(11) DEFAULT NULL,
  `email` varchar(250) DEFAULT NULL,
  `ciudad` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_user`),
  UNIQUE KEY `email` (`email`),
  KEY `ciudad` (`ciudad`),
  CONSTRAINT `tbl_usuarios1_ibfk_1` FOREIGN KEY (`ciudad`) REFERENCES `tbl_ciudad` (`id_ciudad`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
