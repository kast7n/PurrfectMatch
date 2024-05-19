-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: purrfectmatch
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `adoption_application_reply`
--

DROP TABLE IF EXISTS `adoption_application_reply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `adoption_application_reply` (
  `id` int NOT NULL AUTO_INCREMENT,
  `application_id` int DEFAULT NULL,
  `reply_text` longtext,
  `reply_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `pet_id` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `application_id` (`application_id`),
  KEY `fk_adoption_application_reply_pet` (`pet_id`),
  CONSTRAINT `adoption_application_reply_ibfk_1` FOREIGN KEY (`application_id`) REFERENCES `adoption_application` (`id`),
  CONSTRAINT `fk_adoption_application_reply_pet` FOREIGN KEY (`pet_id`) REFERENCES `pet` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adoption_application_reply`
--

LOCK TABLES `adoption_application_reply` WRITE;
/*!40000 ALTER TABLE `adoption_application_reply` DISABLE KEYS */;
INSERT INTO `adoption_application_reply` VALUES (1,1,'Your request have been accepted','2024-05-18 08:02:47',3,8),(2,NULL,'Your request have been accepted','2024-05-18 08:20:09',60,8),(4,NULL,'Your request have been accepted','2024-05-19 08:21:57',70,8),(5,NULL,'Your request have been accepted','2024-05-19 08:21:58',70,8),(6,NULL,'Your request have been accepted','2024-05-19 08:21:58',70,8),(7,NULL,'Your request have been accepted','2024-05-19 08:21:58',70,8),(8,NULL,'Your request have been accepted','2024-05-19 08:21:59',70,8),(9,NULL,'Your request have been accepted','2024-05-19 08:21:59',70,8),(10,NULL,'Your request have been accepted','2024-05-19 08:21:59',70,8),(11,NULL,'Your request have been accepted','2024-05-19 08:22:00',70,8),(12,NULL,'Your request have been accepted','2024-05-19 08:22:00',70,8),(13,NULL,'Your request have been accepted','2024-05-19 08:22:00',70,8),(14,NULL,'Your request have been accepted','2024-05-19 09:44:16',70,8),(15,NULL,'Your request have been accepted','2024-05-19 09:45:08',70,8);
/*!40000 ALTER TABLE `adoption_application_reply` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-19 14:05:19
