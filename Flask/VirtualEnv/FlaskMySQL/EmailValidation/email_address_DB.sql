CREATE DATABASE  IF NOT EXISTS `email_address` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `email_address`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: email_address
-- ------------------------------------------------------
-- Server version	5.7.20-log

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
-- Table structure for table `emails`
--

DROP TABLE IF EXISTS `emails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email_address` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emails`
--

LOCK TABLES `emails` WRITE;
/*!40000 ALTER TABLE `emails` DISABLE KEYS */;
INSERT INTO `emails` VALUES (1,'michael@codingdojo.co','2017-12-30 15:46:54','2017-12-30 15:46:54'),(2,'dexter@codingdojo.co','2017-12-30 15:47:17','2017-12-30 15:47:17'),(3,'eylem@codingdojo.co','2017-12-30 15:47:22','2017-12-30 15:47:22'),(4,'test@test.com','2017-12-30 17:36:29','2017-12-30 17:36:29'),(5,'someone@email.com','2017-12-30 17:39:23','2017-12-30 17:39:23'),(6,'test2@test.com','2017-12-30 17:42:05','2017-12-30 17:42:05'),(7,'jae@asdasd.com','2017-12-30 19:08:20','2017-12-30 19:08:20'),(8,'someoneelse@email.com','2017-12-30 19:09:14','2017-12-30 19:09:14'),(9,'samsung@galaxy.com','2017-12-30 19:21:34','2017-12-30 19:21:34'),(10,'tester@test.com','2017-12-30 19:22:26','2017-12-30 19:22:26'),(11,'jae@asdasd.com','2017-12-30 19:24:30','2017-12-30 19:24:30'),(12,'adsasd@asdas.com','2017-12-30 19:50:37','2017-12-30 19:50:37'),(13,'jae@asdasd.com','2017-12-30 19:52:09','2017-12-30 19:52:09'),(14,'jae@asdasd.com','2017-12-30 20:02:56','2017-12-30 20:02:56'),(15,'jae@asdasd.com','2017-12-30 20:03:59','2017-12-30 20:03:59'),(16,'someone@email.com','2017-12-30 20:04:42','2017-12-30 20:04:42'),(17,'someone@email.com','2017-12-30 20:06:05','2017-12-30 20:06:05'),(18,'someone@email.com','2017-12-30 20:06:18','2017-12-30 20:06:18'),(19,'jae@asdasd.com','2017-12-30 20:06:51','2017-12-30 20:06:51');
/*!40000 ALTER TABLE `emails` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-12-30 20:23:55
