-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: purrfectmatch
-- ------------------------------------------------------
-- Server version	5.7.44-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'1','a@a','scrypt:32768:8:1$bwBYdM10Jfg72VqP$b0668709307709aa03de7d767861fdeaad468d19d4a0a113e19604bc0cea4c1b4db7c22aed14a70916b1814bbbca8f65f2c023ca55509dfa4318a9a92e6f41ab','user'),(2,'1','a@a','scrypt:32768:8:1$NfABl7w0481CLCXV$bccfb3bec10f2b07645ca33db1563d9007fb0a51ce1ad13c3d56085b97d78afd4ba27ec3d2266639477ba41517f2c0656bd1656647deac109656735012a34329','user'),(3,'a','2@2','scrypt:32768:8:1$rqAgwr5CMgSaairh$460508e4e64c1ceca1931de3589308e45c97bea0baf2effc3858b72d8910780ee6dea125809c7271f15518a938d55f26ca69014a36eb43438b4a47ec313d7e7f','user'),(4,'aliawela','ali123awela@gmail.com','scrypt:32768:8:1$VZuJDJCdTYMsAJdH$73e0606677a2253e8f7227921f158a6c8c7e7f19be9c2ba8fa1a9184c6971093dbe97c26c5c48fc9cf8facc94ba21a25702821708e7704b656921a6df316bb0a','shelter'),(5,'alidarsa','ali123darsa@gmail.com','scrypt:32768:8:1$7zbIX66PpgzzL3Yt$f32c5bc0a93b1f8a44201a8c1501a0db0f84304f84507cc23c8f4a6a717a42ad60bbc687468d29860810d2a78306f8488cc6f5dd37444930e8ac93ac55453ec9','user');
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

-- Dump completed on 2024-05-16 16:17:00