CREATE DATABASE  IF NOT EXISTS `fullfriends` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `fullfriends`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: fullfriends
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
-- Table structure for table `full_friends`
--

DROP TABLE IF EXISTS `full_friends`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `full_friends` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `full_friends`
--

LOCK TABLES `full_friends` WRITE;
/*!40000 ALTER TABLE `full_friends` DISABLE KEYS */;
INSERT INTO `full_friends` VALUES (2,'Lola','Bunny','lola@bunny.com','2018-02-21 13:33:02','2018-02-23 11:38:35'),(10,'Bugs','Bunny','bugs@bunny.com','2018-02-23 11:38:48','2018-02-23 11:38:48'),(12,'Road','Runner','rr@rr.com','2018-02-23 14:28:25','2018-02-23 14:28:25'),(14,'Barry','Allen','flash@starlabs.com','2018-03-02 10:50:36','2018-03-02 13:40:54'),(15,'Oliver','Queen','greenarrow@starcity.com','2018-03-02 11:30:02','2018-03-02 11:30:02'),(20,'Bat','Man','batman@cave.com','2018-03-02 13:51:18','2018-03-02 13:51:18'),(21,'Super','Man','superman@sm.com','2018-03-02 13:52:35','2018-03-02 13:52:35'),(24,'Iron','Man','ironman@avengers.com','2018-03-02 13:53:34','2018-03-02 13:57:20');
/*!40000 ALTER TABLE `full_friends` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-02 14:20:28
