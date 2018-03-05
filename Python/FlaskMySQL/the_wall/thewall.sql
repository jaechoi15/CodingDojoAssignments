CREATE DATABASE  IF NOT EXISTS `thewall` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `thewall`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: thewall
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
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `comment` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comments_messages1_idx` (`message_id`),
  KEY `fk_comments_users1_idx` (`user_id`),
  CONSTRAINT `fk_comments_messages1` FOREIGN KEY (`message_id`) REFERENCES `messages` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (1,1,6,'first comment','2018-03-01 23:56:19','2018-03-01 23:56:19'),(18,7,4,'okay','2018-03-01 23:56:39','2018-03-01 23:56:39'),(19,7,4,'s','2018-03-01 23:56:51','2018-03-01 23:56:51'),(20,16,6,'there','2018-03-02 00:02:33','2018-03-02 00:02:33');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_users_idx` (`user_id`),
  CONSTRAINT `fk_messages_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,4,'I am the Green Arrow','2018-02-27 21:40:11','2018-02-27 21:40:11'),(7,6,'To the outside world, I\'m just an ordinary forensic scientist, but secretly I use my speed to fight crime and find others like me, and one day I\'ll find who killed my mother and get justice for my father. I am The Flash. Barry Allen: My name is Barry Allen and I\'m the fastest man alive.','2018-02-27 23:06:25','2018-02-27 23:06:25'),(8,4,'My name is Oliver Queen. For five years, I was stranded on an island with only one goal: survive. Now I will fulfill my father\'s dying wish - to use the list of names he left me and bring down those who are poisoning my city. To do this, I must become someone else. I must become something else','2018-02-27 23:18:50','2018-02-27 23:18:50'),(16,6,'You have failed this city LOL','2018-03-02 00:02:19','2018-03-02 00:02:19');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'test','tester','test@tester.com','$2b$12$mHerxAz2b2JU0O/Q4M9PROtKChbOdDrGQQATTWZRpj454ea9/9XDm','2018-02-26 10:53:04','2018-02-26 10:53:04'),(2,'John','Doe','john@doe.com','$2b$12$YF64dZqnd5SdjTXiLLxyoOdUj45hIOv784K6IseA2T2b6lL96J9fK','2018-02-26 20:31:07','2018-02-26 20:31:07'),(3,'Tony','Stark','iron@man.com','$2b$12$eRLnOu9Y60dc2y7j.bwvV.Br0rIatjMRFBAIrKcHEbPVAKU6p608.','2018-02-26 20:31:42','2018-02-26 20:31:42'),(4,'Oliver','Queen','green@arrow.com','$2b$12$Fr7.dG.59e42UIidEbHI7.cE.G9KhRrTcyKwK.vtmndqUBtpHAovS','2018-02-26 20:32:04','2018-02-26 20:32:04'),(6,'Barry','Allen','theflash@starlabs.com','$2b$12$yeHKRAmo4YoBTv/P0pxiC.LKRcZ23Ya7.5bJVtFTS2TnYf6Mh0mNe','2018-02-27 23:03:26','2018-02-27 23:03:26'),(7,'New','Tester','new@tester.com','$2b$12$k.7YD7HMOD0BITDFvAl2teEyxEAMjgekdOwTLFVadHbvyvRHaBAqC','2018-02-28 11:03:11','2018-02-28 11:03:11');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-02 14:27:09
