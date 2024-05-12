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
-- Table structure for table `pet`
--

DROP TABLE IF EXISTS `pet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pet` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `coat_length` varchar(255) DEFAULT NULL,
  `activity_level` varchar(255) DEFAULT NULL,
  `house_training` varchar(255) DEFAULT NULL,
  `pet_type` varchar(255) DEFAULT NULL,
  `shelter_id` int DEFAULT NULL,
  `health` varchar(255) DEFAULT NULL,
  `good_in_home` tinyint(1) DEFAULT NULL,
  `adoption_fee` int DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `shelter_id` (`shelter_id`),
  CONSTRAINT `pet_ibfk_1` FOREIGN KEY (`shelter_id`) REFERENCES `shelter` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pet`
--

LOCK TABLES `pet` WRITE;
/*!40000 ALTER TABLE `pet` DISABLE KEYS */;
INSERT INTO `pet` VALUES (1,'Aline','Short','High','Yes','Cat',2,'Vaccinated, Spayed',0,50,'Female'),(2,'Basboous','Long','Medium','No','Cat',2,'Spayed',1,50,'Male'),(3,'Blue','Short','Low','Yes','Cat',2,'Vaccinated',1,50,'Female'),(4,'Chopin','Medium','High','Yes','Cat',2,'Vaccinated, Spayed',1,50,'Male'),(5,'Clover','Short','Low','No','Cat',2,'None',1,50,'Female'),(6,'Daisy','Long','Medium','Yes','Cat',2,'Vaccinated',1,50,'Female'),(7,'Honeybee','Short','High','Yes','Cat',2,'None',0,50,'Female'),(8,'Jolly','Medium','Low','No','Cat',2,'Spayed',1,50,'Male'),(9,'Kia','Short','Medium','Yes','Cat',2,'Vaccinated',1,50,'Female'),(10,'Kiki','Long','High','Yes','Cat',2,'Vaccinated, Spayed',1,50,'Female'),(11,'Ninia','Short','Low','Yes','Cat',2,'Vaccinated',0,50,'Female'),(12,'Niro','Medium','High','No','Cat',2,'Spayed',1,50,'Male'),(13,'Rana','Long','Medium','Yes','Cat',2,'Vaccinated',1,50,'Female'),(14,'Scraly','Short','Low','Yes','Cat',2,'Vaccinated, Spayed',1,50,'Female'),(15,'Stevie','Medium','High','No','Cat',2,'None',1,50,'Male'),(16,'Sunny','Short','Medium','Yes','Cat',2,'Vaccinated',0,50,'Female'),(17,'Tail','Long','Low','Yes','Cat',2,'Spayed',1,50,'Male'),(18,'Theo','Short','High','No','Cat',2,'Vaccinated',1,50,'Male'),(19,'Toby','Medium','Medium','Yes','Cat',2,'Vaccinated',1,50,'Male'),(20,'Willow','Long','Low','Yes','Cat',2,'Spayed',1,50,'Female'),(21,'Angus','Short','High','No','Dog',2,'Vaccinated',1,100,'Male'),(22,'Atzo','Medium','Medium','Yes','Dog',2,'Spayed',1,100,'Male'),(23,'Baz','Long','Low','Yes','Dog',2,'Vaccinated, Neutered',1,100,'Male'),(24,'Benito','Short','High','No','Dog',2,'None',1,100,'Male'),(25,'Bozer','Medium','Low','Yes','Dog',2,'Vaccinated',1,100,'Male'),(26,'Buffalo','Long','Medium','Yes','Dog',2,'Spayed',1,100,'Male'),(27,'Chai','Short','High','No','Dog',2,'Vaccinated, Neutered',1,100,'Female'),(28,'Clive','Medium','Low','Yes','Dog',2,'None',1,100,'Male'),(29,'Della','Long','Medium','Yes','Dog',2,'Vaccinated',1,100,'Female'),(30,'Elda','Short','Low','Yes','Dog',2,'Vaccinated',1,100,'Female'),(31,'Fernandel','Medium','High','No','Dog',2,'None',1,100,'Male'),(32,'Lufy','Long','Medium','Yes','Dog',2,'Vaccinated, Neutered',1,100,'Female'),(33,'MacGyver','Short','High','No','Dog',2,'Spayed',1,100,'Male'),(34,'Moushi','Medium','Low','Yes','Dog',2,'Vaccinated',1,100,'Female'),(35,'Natty','Long','Medium','Yes','Dog',2,'None',1,100,'Female'),(36,'Nino','Short','Low','Yes','Dog',2,'Vaccinated',1,100,'Male'),(37,'Pudding','Medium','High','No','Dog',2,'Vaccinated, Neutered',1,100,'Male'),(38,'Rosh','Long','Low','Yes','Dog',2,'None',1,100,'Male'),(39,'Shannon','Short','Medium','Yes','Dog',2,'Vaccinated',1,100,'Female'),(40,'Talia','Medium','High','No','Dog',2,'Spayed',1,100,'Female'),(41,'Aishti','Short','High','Yes','Cat',1,'None',0,50,'Female'),(42,'Anjo','Medium','Medium','Yes','Cat',1,'Vaccinated',1,50,'Male'),(43,'Bart','Short','Low','No','Cat',1,'None',1,50,'Male'),(44,'Bast','Medium','High','No','Cat',1,'Vaccinated',1,50,'Male'),(45,'Bastet','Short','Low','Yes','Cat',1,'Spayed',1,50,'Female'),(46,'Bean','Long','Medium','Yes','Cat',1,'None',0,50,'Male'),(47,'Beau','Short','High','No','Cat',1,'Vaccinated',1,50,'Male'),(48,'Black Beauty','Medium','Low','Yes','Cat',1,'Vaccinated',1,50,'Female'),(49,'Blackie','Short','Medium','Yes','Cat',1,'None',1,50,'Male'),(50,'Bobbi','Long','High','No','Cat',1,'Spayed',1,50,'Female'),(51,'Bolt','Short','Low','Yes','Cat',1,'None',1,50,'Male'),(52,'Bonbon','Medium','Medium','Yes','Cat',1,'Vaccinated',1,50,'Female'),(53,'Bruce','Short','High','No','Cat',1,'Vaccinated',1,50,'Male'),(54,'Bugsy','Medium','Low','Yes','Cat',1,'None',1,50,'Male'),(55,'Butter','Short','Medium','Yes','Cat',1,'Spayed',1,50,'Female'),(56,'Cercie','Long','High','No','Cat',1,'Vaccinated',1,50,'Female'),(57,'Charm','Short','Low','Yes','Cat',1,'None',1,50,'Male'),(58,'Cheese','Medium','Medium','Yes','Cat',1,'Vaccinated',1,50,'Male'),(59,'Chester','Short','High','No','Cat',1,'None',1,50,'Male'),(60,'Chucho','Medium','Low','Yes','Cat',1,'Spayed',1,50,'Male'),(61,'Alma','Short','High','No','Dog',1,'Vaccinated',1,100,'Female'),(62,'Caramella','Medium','Medium','Yes','Dog',1,'Spayed',1,100,'Female'),(63,'Chelsea','Long','Low','Yes','Dog',1,'Vaccinated, Neutered',1,100,'Female'),(64,'Dante','Short','High','No','Dog',1,'None',1,100,'Male'),(65,'Flame','Medium','Low','Yes','Dog',1,'Vaccinated',1,100,'Male'),(66,'Floki','Long','Medium','Yes','Dog',1,'None',1,100,'Male'),(67,'Fox','Short','High','No','Dog',1,'Vaccinated, Neutered',1,100,'Male'),(68,'Hope','Medium','Low','Yes','Dog',1,'None',1,100,'Female'),(69,'Joey','Long','Medium','Yes','Dog',1,'Vaccinated',1,100,'Male'),(70,'Kami','Short','Low','Yes','Dog',1,'Vaccinated',1,100,'Female'),(71,'Lexy','Medium','High','No','Dog',1,'None',1,100,'Female'),(72,'Lucy','Short','Low','Yes','Dog',1,'Vaccinated, Neutered',1,100,'Female'),(73,'Max','Medium','Medium','Yes','Dog',1,'None',1,100,'Male'),(74,'Nahoul','Long','High','No','Dog',1,'Vaccinated',1,100,'Male'),(75,'Nala','Short','Low','Yes','Dog',1,'None',1,100,'Female'),(76,'Noodles','Medium','Medium','Yes','Dog',1,'Vaccinated',1,100,'Male'),(77,'Nour','Short','High','No','Dog',1,'None',1,100,'Female'),(78,'Pele','Medium','Low','Yes','Dog',1,'Vaccinated, Neutered',1,100,'Male'),(79,'Ragnar','Long','Medium','Yes','Dog',1,'None',1,100,'Male'),(80,'Sasha','Short','High','No','Dog',1,'Vaccinated',1,100,'Female');
/*!40000 ALTER TABLE `pet` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-12 17:40:36
