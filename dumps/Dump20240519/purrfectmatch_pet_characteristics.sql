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
-- Table structure for table `pet_characteristics`
--

DROP TABLE IF EXISTS `pet_characteristics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pet_characteristics` (
  `pet_id` int NOT NULL,
  `characteristic` varchar(255) NOT NULL,
  PRIMARY KEY (`pet_id`,`characteristic`),
  CONSTRAINT `fk_PetCharacteristics_Pets` FOREIGN KEY (`pet_id`) REFERENCES `pet` (`id`) ON DELETE CASCADE,
  CONSTRAINT `pet_characteristics_ibfk_1` FOREIGN KEY (`pet_id`) REFERENCES `pet` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pet_characteristics`
--

LOCK TABLES `pet_characteristics` WRITE;
/*!40000 ALTER TABLE `pet_characteristics` DISABLE KEYS */;
INSERT INTO `pet_characteristics` VALUES (1,'Affectionate'),(1,'Lap Cat'),(1,'Shy'),(2,'Independent'),(2,'Playful'),(3,'Lap Cat'),(3,'Social'),(4,'Affectionate'),(4,'Independent'),(4,'Playful'),(5,'Lap Cat'),(5,'Shy'),(6,'Affectionate'),(6,'Playful'),(6,'Shy'),(7,'Independent'),(7,'Lap Cat'),(8,'Affectionate'),(8,'Playful'),(9,'Lap Cat'),(9,'Social'),(10,'Affectionate'),(10,'Independent'),(10,'Playful'),(11,'Lap Cat'),(11,'Shy'),(12,'Affectionate'),(12,'Playful'),(12,'Shy'),(13,'Independent'),(13,'Lap Cat'),(14,'Affectionate'),(14,'Playful'),(15,'Lap Cat'),(15,'Social'),(16,'Affectionate'),(16,'Independent'),(16,'Playful'),(17,'Lap Cat'),(17,'Shy'),(18,'Affectionate'),(18,'Playful'),(18,'Shy'),(19,'Independent'),(19,'Lap Cat'),(20,'Affectionate'),(20,'Playful'),(21,'Lap Cat'),(21,'Shy'),(22,'Affectionate'),(22,'Playful'),(22,'Shy'),(23,'Independent'),(23,'Lap Cat'),(24,'Affectionate'),(24,'Playful'),(25,'Lap Cat'),(25,'Social'),(26,'Affectionate'),(26,'Independent'),(26,'Playful'),(27,'Lap Cat'),(27,'Shy'),(28,'Affectionate'),(28,'Playful'),(28,'Shy'),(29,'Independent'),(29,'Lap Cat'),(30,'Affectionate'),(30,'Playful'),(31,'Lap Cat'),(31,'Social'),(32,'Affectionate'),(32,'Independent'),(32,'Playful'),(33,'Lap Cat'),(33,'Shy'),(34,'Affectionate'),(34,'Playful'),(34,'Shy'),(35,'Independent'),(35,'Lap Cat'),(36,'Affectionate'),(36,'Playful'),(37,'Lap Cat'),(37,'Social'),(38,'Affectionate'),(38,'Independent'),(38,'Playful'),(39,'Lap Cat'),(39,'Shy'),(40,'Affectionate'),(40,'Playful'),(40,'Shy'),(41,'Independent'),(41,'Lap Cat'),(42,'Affectionate'),(42,'Playful'),(43,'Lap Cat'),(43,'Social'),(44,'Affectionate'),(44,'Independent'),(44,'Playful'),(45,'Lap Cat'),(45,'Shy'),(46,'Affectionate'),(46,'Playful'),(46,'Shy'),(47,'Independent'),(47,'Lap Cat'),(48,'Affectionate'),(48,'Playful'),(49,'Lap Cat'),(49,'Social'),(50,'Affectionate'),(50,'Independent'),(50,'Playful'),(51,'Lap Cat'),(51,'Shy'),(52,'Affectionate'),(52,'Playful'),(52,'Shy'),(53,'Independent'),(53,'Lap Cat'),(54,'Affectionate'),(54,'Playful'),(55,'Lap Cat'),(55,'Social'),(56,'Affectionate'),(56,'Independent'),(56,'Playful'),(57,'Lap Cat'),(57,'Shy'),(58,'Affectionate'),(58,'Playful'),(58,'Shy'),(59,'Independent'),(59,'Lap Cat'),(60,'Affectionate'),(60,'Playful'),(61,'Lap Cat'),(61,'Shy'),(62,'Affectionate'),(62,'Playful'),(62,'Shy'),(63,'Independent'),(63,'Lap Cat'),(64,'Affectionate'),(64,'Playful'),(65,'Lap Cat'),(65,'Social'),(66,'Affectionate'),(66,'Independent'),(66,'Playful'),(67,'Lap Cat'),(67,'Shy'),(68,'Affectionate'),(68,'Playful'),(68,'Shy'),(69,'Independent'),(69,'Lap Cat'),(70,'Affectionate'),(70,'Playful'),(71,'Lap Cat'),(71,'Social'),(72,'Affectionate'),(72,'Independent'),(72,'Playful'),(73,'Lap Cat'),(73,'Shy'),(74,'Affectionate'),(74,'Playful'),(74,'Shy'),(75,'Independent'),(75,'Lap Cat'),(76,'Affectionate'),(76,'Playful'),(77,'Lap Cat'),(77,'Social'),(78,'Affectionate'),(78,'Playful'),(79,'Affectionate'),(79,'Independent'),(79,'Playful'),(80,'Playful'),(80,'Shy');
/*!40000 ALTER TABLE `pet_characteristics` ENABLE KEYS */;
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
