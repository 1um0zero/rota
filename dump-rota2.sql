-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: rafapaz.mysql.pythonanywhere-services.com    Database: rafapaz$default
-- ------------------------------------------------------
-- Server version	5.7.21-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add contest',7,'add_contest'),(26,'Can change contest',7,'change_contest'),(27,'Can delete contest',7,'delete_contest'),(28,'Can view contest',7,'view_contest'),(29,'Can add curador group',8,'add_curadorgroup'),(30,'Can change curador group',8,'change_curadorgroup'),(31,'Can delete curador group',8,'delete_curadorgroup'),(32,'Can view curador group',8,'view_curadorgroup'),(33,'Can add folder',9,'add_folder'),(34,'Can change folder',9,'change_folder'),(35,'Can delete folder',9,'delete_folder'),(36,'Can view folder',9,'view_folder'),(37,'Can add page',10,'add_page'),(38,'Can change page',10,'change_page'),(39,'Can delete page',10,'delete_page'),(40,'Can view page',10,'view_page'),(41,'Can add product',11,'add_product'),(42,'Can change product',11,'change_product'),(43,'Can delete product',11,'delete_product'),(44,'Can view product',11,'view_product'),(45,'Can add role',12,'add_role'),(46,'Can change role',12,'change_role'),(47,'Can delete role',12,'delete_role'),(48,'Can view role',12,'view_role'),(49,'Can add user role',13,'add_userrole'),(50,'Can change user role',13,'change_userrole'),(51,'Can delete user role',13,'delete_userrole'),(52,'Can view user role',13,'view_userrole'),(53,'Can add user profile',14,'add_userprofile'),(54,'Can change user profile',14,'change_userprofile'),(55,'Can delete user profile',14,'delete_userprofile'),(56,'Can view user profile',14,'view_userprofile'),(57,'Can add subscription',15,'add_subscription'),(58,'Can change subscription',15,'change_subscription'),(59,'Can delete subscription',15,'delete_subscription'),(60,'Can view subscription',15,'view_subscription'),(61,'Can add short',16,'add_short'),(62,'Can change short',16,'change_short'),(63,'Can delete short',16,'delete_short'),(64,'Can view short',16,'view_short'),(65,'Can add script',17,'add_script'),(66,'Can change script',17,'change_script'),(67,'Can delete script',17,'delete_script'),(68,'Can view script',17,'view_script'),(69,'Can add password recovery token',18,'add_passwordrecoverytoken'),(70,'Can change password recovery token',18,'change_passwordrecoverytoken'),(71,'Can delete password recovery token',18,'delete_passwordrecoverytoken'),(72,'Can view password recovery token',18,'view_passwordrecoverytoken'),(73,'Can add order',19,'add_order'),(74,'Can change order',19,'change_order'),(75,'Can delete order',19,'delete_order'),(76,'Can view order',19,'view_order'),(77,'Can add curador',20,'add_curador'),(78,'Can change curador',20,'change_curador'),(79,'Can delete curador',20,'delete_curador'),(80,'Can view curador',20,'view_curador');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$150000$TZ1HxoiFMBtp$xHldtEMztvnkZB1WacMBLFp4dyTaBb/LfCnaJ0ZNXB0=','2020-07-11 20:48:41.008770',1,'rafapaz@gmail.com','','','rafapaz@gmail.com',1,1,'2020-07-11 00:58:45.310310'),(2,'pbkdf2_sha256$150000$As1cOjv9rXI9$TJf6IUJMzzuXLVEHTLMNA5Uu/cVQFnw1Y1P1gfRRX54=','2020-07-13 01:17:58.640404',0,'joao@gmail.com','João','','joao@gmail.com',0,1,'2020-07-12 14:43:14.016053'),(3,'pbkdf2_sha256$150000$jZ4x5b4CX1Po$c3aPd7PXuENDpcHSIU3a9X743TqEI2Hv+/7t6XcxreY=','2020-07-13 01:33:18.669795',0,'maria@gmail.com','Maria Eduarda','','maria@gmail.com',0,1,'2020-07-13 01:19:12.396260');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_contest`
--

DROP TABLE IF EXISTS `core_contest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_contest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` longtext,
  `regulation` longtext,
  `is_free` tinyint(1) NOT NULL,
  `subscription_limit` int(11) NOT NULL,
  `subscription_open` tinyint(1) NOT NULL,
  `url` varchar(200) NOT NULL,
  `image_url` varchar(200) DEFAULT NULL,
  `date` varchar(30) DEFAULT NULL,
  `display_on_site` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_contest`
--

LOCK TABLES `core_contest` WRITE;
/*!40000 ALTER TABLE `core_contest` DISABLE KEYS */;
INSERT INTO `core_contest` VALUES (1,'Concurso de roteiro de curtas','<p>APOKAPOK APOK apokapok poa kapokapok</p>','<p>oiaiajiajai jajiajiaji</p>',0,500,1,'concurso-de-roteiro-de-curtas','','',1);
/*!40000 ALTER TABLE `core_contest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_curador`
--

DROP TABLE IF EXISTS `core_curador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_curador` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(250) NOT NULL,
  `picture` varchar(250) DEFAULT NULL,
  `bio` longtext,
  `contest_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_curador_contest_id_31238bf7_fk_core_contest_id` (`contest_id`),
  CONSTRAINT `core_curador_contest_id_31238bf7_fk_core_contest_id` FOREIGN KEY (`contest_id`) REFERENCES `core_contest` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_curador`
--

LOCK TABLES `core_curador` WRITE;
/*!40000 ALTER TABLE `core_curador` DISABLE KEYS */;
INSERT INTO `core_curador` VALUES (2,'Fulano','8825fbe4-ee8d-46a4-a4fd-18ad29597b8d.png','kjbhnkjblijuhioh',NULL);
/*!40000 ALTER TABLE `core_curador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_curadorgroup`
--

DROP TABLE IF EXISTS `core_curadorgroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_curadorgroup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  `contest_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_curadorgroup_contest_id_dd24e92c_fk_core_contest_id` (`contest_id`),
  CONSTRAINT `core_curadorgroup_contest_id_dd24e92c_fk_core_contest_id` FOREIGN KEY (`contest_id`) REFERENCES `core_contest` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_curadorgroup`
--

LOCK TABLES `core_curadorgroup` WRITE;
/*!40000 ALTER TABLE `core_curadorgroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_curadorgroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_folder`
--

DROP TABLE IF EXISTS `core_folder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_folder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_folder_parent_id_8892d3fc_fk_core_folder_id` (`parent_id`),
  CONSTRAINT `core_folder_parent_id_8892d3fc_fk_core_folder_id` FOREIGN KEY (`parent_id`) REFERENCES `core_folder` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_folder`
--

LOCK TABLES `core_folder` WRITE;
/*!40000 ALTER TABLE `core_folder` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_folder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_order`
--

DROP TABLE IF EXISTS `core_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` double NOT NULL,
  `status` int(11) NOT NULL,
  `payment_method` int(11) NOT NULL,
  `error` varchar(250) DEFAULT NULL,
  `card_brand` varchar(20) DEFAULT NULL,
  `card_end` int(11) DEFAULT NULL,
  `link_boleto` varchar(250) DEFAULT NULL,
  `parcelas` int(11) DEFAULT NULL,
  `valor_parcela` double DEFAULT NULL,
  `total_prazo` double DEFAULT NULL,
  `data_desejada` varchar(10) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `product_id` int(11) NOT NULL,
  `subscription_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_order_product_id_0cbee06a_fk_core_product_id` (`product_id`),
  KEY `core_order_subscription_id_7cf67005_fk_core_subscription_id` (`subscription_id`),
  KEY `core_order_user_id_b03bbffd_fk_auth_user_id` (`user_id`),
  CONSTRAINT `core_order_product_id_0cbee06a_fk_core_product_id` FOREIGN KEY (`product_id`) REFERENCES `core_product` (`id`),
  CONSTRAINT `core_order_subscription_id_7cf67005_fk_core_subscription_id` FOREIGN KEY (`subscription_id`) REFERENCES `core_subscription` (`id`),
  CONSTRAINT `core_order_user_id_b03bbffd_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_order`
--

LOCK TABLES `core_order` WRITE;
/*!40000 ALTER TABLE `core_order` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_page`
--

DROP TABLE IF EXISTS `core_page`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_page` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `status` int(11) NOT NULL,
  `content` longtext,
  `url` varchar(200) NOT NULL,
  `order` int(11) NOT NULL,
  `display_on_menu` tinyint(1) NOT NULL,
  `fixed` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_page`
--

LOCK TABLES `core_page` WRITE;
/*!40000 ALTER TABLE `core_page` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_page` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_passwordrecoverytoken`
--

DROP TABLE IF EXISTS `core_passwordrecoverytoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_passwordrecoverytoken` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `token` varchar(32) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_passwordrecoverytoken_user_id_b498c85f_fk_auth_user_id` (`user_id`),
  CONSTRAINT `core_passwordrecoverytoken_user_id_b498c85f_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_passwordrecoverytoken`
--

LOCK TABLES `core_passwordrecoverytoken` WRITE;
/*!40000 ALTER TABLE `core_passwordrecoverytoken` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_passwordrecoverytoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_product`
--

DROP TABLE IF EXISTS `core_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `slug` varchar(10) DEFAULT NULL,
  `description` longtext NOT NULL,
  `price` double NOT NULL,
  `price2` double DEFAULT NULL,
  `price2_date` varchar(30) DEFAULT NULL,
  `is_enabled` tinyint(1) NOT NULL,
  `url` varchar(100) DEFAULT NULL,
  `position` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_product`
--

LOCK TABLES `core_product` WRITE;
/*!40000 ALTER TABLE `core_product` DISABLE KEYS */;
INSERT INTO `core_product` VALUES (1,'Pacote01','aaaa','Pacote para ao asdsadpoask',50,60,'20/07/2020',1,'pacote01',0),(2,'Pacote02','bbbb','oaisp oaispoaidpoaisdpoas asd',30,40,'20/07/2020',1,'pacote02',0);
/*!40000 ALTER TABLE `core_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_role`
--

DROP TABLE IF EXISTS `core_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_role`
--

LOCK TABLES `core_role` WRITE;
/*!40000 ALTER TABLE `core_role` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_script`
--

DROP TABLE IF EXISTS `core_script`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_script` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `original_filename` varchar(100) NOT NULL,
  `filename` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_script_user_id_b7a1c3f9_fk_auth_user_id` (`user_id`),
  CONSTRAINT `core_script_user_id_b7a1c3f9_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_script`
--

LOCK TABLES `core_script` WRITE;
/*!40000 ALTER TABLE `core_script` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_script` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_short`
--

DROP TABLE IF EXISTS `core_short`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_short` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(200) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_short_user_id_ba648c1e_fk_auth_user_id` (`user_id`),
  CONSTRAINT `core_short_user_id_ba648c1e_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_short`
--

LOCK TABLES `core_short` WRITE;
/*!40000 ALTER TABLE `core_short` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_short` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_subscription`
--

DROP TABLE IF EXISTS `core_subscription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_subscription` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data` longtext,
  `status` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `contest_id` int(11) NOT NULL,
  `folder_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_subscription_contest_id_cdc64232_fk_core_contest_id` (`contest_id`),
  KEY `core_subscription_folder_id_e12e24c2_fk_core_folder_id` (`folder_id`),
  KEY `core_subscription_group_id_87bdca7d_fk_core_curadorgroup_id` (`group_id`),
  KEY `core_subscription_user_id_47899df3_fk_auth_user_id` (`user_id`),
  CONSTRAINT `core_subscription_contest_id_cdc64232_fk_core_contest_id` FOREIGN KEY (`contest_id`) REFERENCES `core_contest` (`id`),
  CONSTRAINT `core_subscription_folder_id_e12e24c2_fk_core_folder_id` FOREIGN KEY (`folder_id`) REFERENCES `core_folder` (`id`),
  CONSTRAINT `core_subscription_group_id_87bdca7d_fk_core_curadorgroup_id` FOREIGN KEY (`group_id`) REFERENCES `core_curadorgroup` (`id`),
  CONSTRAINT `core_subscription_user_id_47899df3_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_subscription`
--

LOCK TABLES `core_subscription` WRITE;
/*!40000 ALTER TABLE `core_subscription` DISABLE KEYS */;
INSERT INTO `core_subscription` VALUES (1,'{\"nickname\": \"aloalo\", \"phone_home_ddd\": \"21\", \"phone_home\": \"2625-6115\", \"rg\": \"125658598\", \"cep\": \"24942-380\", \"address\": \"Estrada Velha De Maric\\u00e1\", \"address_number\": \"222\", \"address_complement\": \"hhh\", \"address_neighborhood\": \"oijuoi\", \"address_city\": \"Angra dos Reis\", \"address_state\": \"RJ\", \"title\": \"A volta dos que n\\u00e3o foram\", \"max_subscriptions\": \"sim\", \"max_pages\": \"sim\", \"is_student\": \"iniciante\", \"coauthors\": \"nao\", \"letter\": null, \"letter2\": null, \"is_original\": \"original\", \"authorize\": \"sim\", \"rg_front\": \"f11aa216-503e-4808-bf12-0c3d9e51158c.png\", \"rg_back\": \"e5110858-4ee3-462d-880d-a10e19df60c6.png\", \"script\": \"18246d3c-231a-49e6-a532-b4701c11d01c.pdf\", \"responsibility\": \"b1e3564f-b5eb-4ab6-bf9a-b9d878718623.pdf\"}',1,'2020-07-12 18:02:54.353227',1,NULL,NULL,2),(2,'{\"nickname\": \"ururur\", \"phone_home_ddd\": \"21\", \"phone_home\": \"9885-5888\", \"rg\": \"888555222\", \"cep\": \"24942-380\", \"address\": \"Estrada Velha De Maric\\u00e1 240\", \"address_number\": \"222\", \"address_complement\": \"hhh\", \"address_neighborhood\": \"oijuoi\", \"address_city\": \"Angra dos Reis\", \"address_state\": \"RJ\", \"title\": \"Entrega r\\u00e1pida!\", \"max_subscriptions\": \"sim\", \"max_pages\": \"sim\", \"is_student\": \"estudante\", \"coauthors\": \"nao\", \"letter\": null, \"letter2\": null, \"is_original\": \"adaptado\", \"authorize\": \"sim\", \"rg_front\": \"3b6772a4-a8e9-4ecd-b2c3-c9c5c9064369.png\", \"rg_back\": \"52f33b61-8923-48b6-af6b-96d5d3b8e7c4.png\", \"script\": \"cbfff511-3f9d-4c28-932c-9ed276116b51.pdf\", \"responsibility\": \"cd01f032-86fe-4d09-9a2d-95f55311cc01.pdf\"}',1,'2020-07-13 01:22:18.979427',1,NULL,NULL,3);
/*!40000 ALTER TABLE `core_subscription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_userprofile`
--

DROP TABLE IF EXISTS `core_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ddd` varchar(2) NOT NULL,
  `phone` varchar(30) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_userprofile_user_id_5141ad90_fk_auth_user_id` (`user_id`),
  CONSTRAINT `core_userprofile_user_id_5141ad90_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_userprofile`
--

LOCK TABLES `core_userprofile` WRITE;
/*!40000 ALTER TABLE `core_userprofile` DISABLE KEYS */;
INSERT INTO `core_userprofile` VALUES (1,'21','98786-7128',2),(2,'21','98786-7128',3);
/*!40000 ALTER TABLE `core_userprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_userrole`
--

DROP TABLE IF EXISTS `core_userrole`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_userrole` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `contest_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `role_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_userrole_contest_id_69290e7b_fk_core_contest_id` (`contest_id`),
  KEY `core_userrole_group_id_c7682516_fk_core_curadorgroup_id` (`group_id`),
  KEY `core_userrole_role_id_8272b20d_fk_core_role_id` (`role_id`),
  KEY `core_userrole_user_id_aca63c51_fk_auth_user_id` (`user_id`),
  CONSTRAINT `core_userrole_contest_id_69290e7b_fk_core_contest_id` FOREIGN KEY (`contest_id`) REFERENCES `core_contest` (`id`),
  CONSTRAINT `core_userrole_group_id_c7682516_fk_core_curadorgroup_id` FOREIGN KEY (`group_id`) REFERENCES `core_curadorgroup` (`id`),
  CONSTRAINT `core_userrole_role_id_8272b20d_fk_core_role_id` FOREIGN KEY (`role_id`) REFERENCES `core_role` (`id`),
  CONSTRAINT `core_userrole_user_id_aca63c51_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_userrole`
--

LOCK TABLES `core_userrole` WRITE;
/*!40000 ALTER TABLE `core_userrole` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_userrole` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'core','contest'),(20,'core','curador'),(8,'core','curadorgroup'),(9,'core','folder'),(19,'core','order'),(10,'core','page'),(18,'core','passwordrecoverytoken'),(11,'core','product'),(12,'core','role'),(17,'core','script'),(16,'core','short'),(15,'core','subscription'),(14,'core','userprofile'),(13,'core','userrole'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-07-11 00:46:03.987699'),(2,'auth','0001_initial','2020-07-11 00:46:04.145703'),(3,'admin','0001_initial','2020-07-11 00:46:04.704827'),(4,'admin','0002_logentry_remove_auto_add','2020-07-11 00:46:04.871865'),(5,'admin','0003_logentry_add_action_flag_choices','2020-07-11 00:46:04.879867'),(6,'contenttypes','0002_remove_content_type_name','2020-07-11 00:46:04.983890'),(7,'auth','0002_alter_permission_name_max_length','2020-07-11 00:46:05.046904'),(8,'auth','0003_alter_user_email_max_length','2020-07-11 00:46:05.069910'),(9,'auth','0004_alter_user_username_opts','2020-07-11 00:46:05.076911'),(10,'auth','0005_alter_user_last_login_null','2020-07-11 00:46:05.132923'),(11,'auth','0006_require_contenttypes_0002','2020-07-11 00:46:05.135924'),(12,'auth','0007_alter_validators_add_error_messages','2020-07-11 00:46:05.142926'),(13,'auth','0008_alter_user_username_max_length','2020-07-11 00:46:05.202939'),(14,'auth','0009_alter_user_last_name_max_length','2020-07-11 00:46:05.261952'),(15,'auth','0010_alter_group_name_max_length','2020-07-11 00:46:05.278956'),(16,'auth','0011_update_proxy_permissions','2020-07-11 00:46:05.285958'),(17,'core','0001_initial','2020-07-11 00:46:05.740059'),(18,'sessions','0001_initial','2020-07-11 00:46:07.036350'),(19,'core','0002_auto_20190601_1254','2020-07-11 00:56:01.554517'),(20,'core','0003_auto_20190601_1303','2020-07-11 00:56:01.557518'),(21,'core','0004_auto_20190601_1303','2020-07-11 00:56:01.559518'),(22,'core','0005_auto_20190601_1737','2020-07-11 00:56:01.562519'),(23,'core','0006_auto_20190605_1247','2020-07-11 00:56:01.564519'),(24,'core','0007_auto_20190605_1344','2020-07-11 00:56:01.567520'),(25,'core','0008_auto_20190605_1344','2020-07-11 00:56:01.570521'),(26,'core','0009_auto_20190605_1345','2020-07-11 00:56:01.572521'),(27,'core','0010_subscription_data','2020-07-11 00:56:01.574521'),(28,'core','0011_subscription_status','2020-07-11 00:56:01.576522'),(29,'core','0012_auto_20190621_2011','2020-07-11 00:56:01.579523'),(30,'core','0013_product_is_enabled','2020-07-11 00:56:01.582524'),(31,'core','0014_auto_20190622_0009','2020-07-11 00:56:01.584523'),(32,'core','0015_order_product','2020-07-11 00:56:01.586524'),(33,'core','0016_order_error','2020-07-11 00:56:01.588524'),(34,'core','0017_order_link_boleto','2020-07-11 00:56:01.591526'),(35,'core','0018_product_url','2020-07-11 00:56:01.593525'),(36,'core','0019_product_slug','2020-07-11 00:56:01.595526'),(37,'core','0020_product_position','2020-07-11 00:56:01.598527'),(38,'core','0021_product_price2','2020-07-11 00:56:01.600527'),(39,'core','0022_product_price2_date','2020-07-11 00:56:01.603528'),(40,'core','0023_auto_20190711_1733','2020-07-11 00:56:01.605529'),(41,'core','0024_curadorgroup','2020-07-11 00:56:01.607529'),(42,'core','0025_userrole_group','2020-07-11 00:56:01.610530'),(43,'core','0026_subscription_group','2020-07-11 00:56:01.612530'),(44,'core','0027_curadorgroup_contest','2020-07-11 00:56:01.614530'),(45,'core','0028_auto_20190717_0848','2020-07-11 00:56:01.617531'),(46,'core','0029_auto_20190717_0855','2020-07-11 00:56:01.619531'),(47,'core','0030_userrole_contest','2020-07-11 00:56:01.621532'),(48,'core','0031_auto_20190813_1418','2020-07-11 00:56:01.624532'),(49,'core','0032_auto_20190813_1420','2020-07-11 00:56:01.626533'),(50,'core','0033_order_data_desejada','2020-07-11 00:56:01.629534'),(51,'core','0034_order_total_prazo','2020-07-11 00:56:01.631535'),(52,'core','0035_folder','2020-07-11 00:56:01.634535'),(53,'core','0036_auto_20190911_0846','2020-07-11 00:56:01.636535'),(54,'core','0037_subscription_folder','2020-07-11 00:56:01.638535'),(55,'core','0038_curador','2020-07-11 00:56:01.640536'),(56,'core','0039_auto_20190924_1601','2020-07-11 00:56:01.643537'),(57,'core','0040_curador_contest','2020-07-11 00:56:01.645538');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('ecjyktvqj7jr7buhco7hsdyfrrumem71','OTI4MmI5YzYwNDEwYmQyOGEzNDkwYmEwMGI4MTU3NDljZDk0NWM2Yjp7Im1zZyI6IiIsIm1zZ19jbGFzcyI6IiIsInBhaW5lbCI6eyJpZCI6MSwiZW1haWwiOiJyYWZhcGF6QGdtYWlsLmNvbSIsIm5hbWUiOiIiLCJyb2xlIjpbMCwiQWRtaW5pc3RyYWRvcihhKSJdLCJpc19hZG1pbiI6dHJ1ZSwiaXNfY3VyYWRvciI6ZmFsc2UsInZpZXdfcm90ZWlyb3MiOmZhbHNlLCJ2aWV3X2VuY29udHJvIjpmYWxzZSwidmlld19wcm9qZXRvcyI6ZmFsc2V9LCJfYXV0aF91c2VyX2lkIjoiMiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZDNmOTBmNWFiZjU4Y2IwODY0YzU2NGIwOTY2NmM0YmMxZDZhNDU4NyIsInN1YnNjcmlwdGlvbl9pZCI6MSwiY29udGVzdF9pZCI6MX0=','2020-07-26 18:23:20.467600');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-13  1:44:47
