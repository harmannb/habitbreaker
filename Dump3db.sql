-- MySQL dump 10.13  Distrib 5.7.12, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: habitbreakerdb
-- ------------------------------------------------------
-- Server version	5.5.42

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
-- Table structure for table `habits`
--

DROP TABLE IF EXISTS `habits`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `habits` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` float DEFAULT NULL,
  `habit_name` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `holder_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_habits_users1_idx` (`holder_id`),
  CONSTRAINT `fk_habits_users1` FOREIGN KEY (`holder_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `habits`
--

LOCK TABLES `habits` WRITE;
/*!40000 ALTER TABLE `habits` DISABLE KEYS */;
INSERT INTO `habits` VALUES (1,2,'biting nails','2016-07-26 16:35:20','2016-07-26 16:35:20',1),(3,1.5,'biting nails','2016-07-26 22:21:37','2016-07-26 22:21:37',2),(4,5.5,'smoking','2016-07-27 10:46:18','2016-07-27 10:46:18',2),(5,1,'smoking','2016-07-27 13:59:08','2016-07-27 13:59:08',6),(6,1.5,'not paying attention','2016-07-27 14:01:53','2016-07-27 14:01:53',6),(7,1,'finger biting','2016-07-27 20:01:25','2016-07-27 20:01:25',7),(10,4,'swearing','2016-07-28 12:24:12','2016-07-28 12:24:12',1),(11,3,'nail biting','2016-07-28 18:45:09','2016-07-28 18:45:09',7),(12,4,'talking loud','2016-07-28 20:27:22','2016-07-28 20:27:22',12),(13,100,'swearing','2016-07-28 21:40:48','2016-07-28 21:40:48',7),(14,1,'going to Starbucks','2016-07-29 08:20:26','2016-07-29 08:20:26',7);
/*!40000 ALTER TABLE `habits` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `helpers`
--

DROP TABLE IF EXISTS `helpers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `helpers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `habit_id` int(11) NOT NULL,
  `helper_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_users_has_helpers_habits1_idx` (`habit_id`),
  KEY `fk_helpers_users1_idx` (`helper_id`),
  CONSTRAINT `fk_users_has_helpers_habits1` FOREIGN KEY (`habit_id`) REFERENCES `habits` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_helpers_users1` FOREIGN KEY (`helper_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `helpers`
--

LOCK TABLES `helpers` WRITE;
/*!40000 ALTER TABLE `helpers` DISABLE KEYS */;
INSERT INTO `helpers` VALUES (1,'2016-07-26 17:41:21','2016-07-26 17:41:21',1,2),(2,'2016-07-26 17:41:45','2016-07-26 17:41:45',1,3),(3,'2016-07-26 17:41:45','2016-07-26 17:41:45',7,1),(4,'2016-07-28 15:43:25','2016-07-28 15:43:25',10,9),(5,'2016-07-28 18:58:39','2016-07-28 18:58:39',10,10),(6,'2016-07-28 20:26:00','2016-07-28 20:26:00',11,12),(7,'2016-07-28 20:37:33','2016-07-28 20:37:33',10,8),(8,'2016-07-28 21:44:18','2016-07-28 21:44:18',13,2),(9,'2016-07-28 21:44:18','2016-07-28 21:44:18',4,1),(10,'2016-07-29 08:31:34','2016-07-29 08:31:34',14,6);
/*!40000 ALTER TABLE `helpers` ENABLE KEYS */;
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
  `phone_number` int(11) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Valentyna','Gorbachenko','gorbachenko.valentyna@gmail.com',1650307120,'$2b$12$7dd9vDhbd0cxyAtfrRZRUecnIBI6/AcrL0lTq8DKk.3GXscoyHbKC','2016-07-25 22:22:58','2016-07-26 22:03:11'),(2,'Dahye','Choi','dahyechoi@gmail.com',NULL,'$2b$12$vEuKWD72WLmb4BotpvchWuY8TJ1PgjxgHEzmobYcpkV1bK4UlWSDa','2016-07-26 08:42:51','2016-07-26 08:42:51'),(3,'John','Smith','jsmith@gmail.com',NULL,'$2b$12$bYR3Xb3K415IfGRQIwVKROG57NRWTMufyAFtPknsF4foz1ZIIytwe','2016-07-26 13:19:45','2016-07-26 16:09:54'),(6,'Andrew','Liu','andcliu@gmail.com',NULL,'$2b$12$tnx4tWH9.fqBR9J7X.ZzQOu/67pocNH2T3voN1sZrIJvEz/eRbLLe','2016-07-27 13:56:35','2016-07-29 08:32:10'),(7,'Dahye','Choi','dahyechoi88@gmail.com',NULL,NULL,'2016-07-27 20:00:44','2016-07-27 20:00:44'),(8,'Kate','Smith','ks@gmail.com',NULL,'$2b$12$tnx4tWH9.fqBR9J7X.ZzQOu/67pocNH2T3voN1sZrIJvEz/eRbLLe','2016-07-27 21:10:52','2016-07-27 21:20:53'),(9,'Andy','Johns','ajohns@gmail.com',NULL,'$2b$12$7S1JiWtMF0b/.VS1MQ31/.eAuVQqExyj2cvalNYMJsZDo2m5rcIJO','2016-07-28 15:43:25','2016-07-28 15:43:25'),(10,'Val','Lala','valentyna@gmail.com',NULL,'$2b$12$OmjqqfGDHDLktZ8gecqp.el3a8GvktzGDFKc0t8zwiapRDIzYs5gq','2016-07-28 18:58:39','2016-07-28 18:58:39'),(11,'Valentyna','Gorbachenko','gorbachenko@gmail.com',NULL,'$2b$12$NRbJE.wbIB9U8cOicnzdY.KyN3fsqdsgzfqc2cllCKDFGBmkdphk6','2016-07-28 20:23:10','2016-07-28 20:23:10'),(12,'Max','Mean','max@gmail.com',NULL,'$2b$12$iL6f5d7XXzocsm5qjilLYu//vCTe/Z2tUL/VNEbeKSHvXc14bKm7q','2016-07-28 20:26:00','2016-07-28 20:26:00');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `violations`
--

DROP TABLE IF EXISTS `violations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `violations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `habit_id` int(11) NOT NULL,
  `helper_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_violations_habits1_idx` (`habit_id`),
  KEY `fk_violations_users1_idx` (`helper_id`),
  CONSTRAINT `fk_violations_habits1` FOREIGN KEY (`habit_id`) REFERENCES `habits` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_violations_users1` FOREIGN KEY (`helper_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `violations`
--

LOCK TABLES `violations` WRITE;
/*!40000 ALTER TABLE `violations` DISABLE KEYS */;
INSERT INTO `violations` VALUES (1,'2016-07-26 17:36:34','2016-07-26 17:36:34',1,3),(2,'2016-07-26 17:36:41','2016-07-26 17:36:41',1,2),(3,'2016-07-28 17:00:01','2016-07-28 17:00:01',7,1),(4,'2016-07-28 17:02:11','2016-07-28 17:02:11',7,1),(5,'2016-07-28 17:11:12','2016-07-28 17:11:12',7,1),(6,'2016-07-28 20:28:08','2016-07-28 20:28:08',11,12),(7,'2016-07-28 20:37:52','2016-07-28 20:37:52',10,8),(8,'2016-07-28 21:44:44','2016-07-28 21:44:44',13,1),(9,'2016-07-29 08:33:54','2016-07-29 08:33:54',14,6);
/*!40000 ALTER TABLE `violations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-07-29  8:47:47
