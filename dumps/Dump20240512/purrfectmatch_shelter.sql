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
-- Table structure for table `shelter`
--

DROP TABLE IF EXISTS `shelter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shelter` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `po_box` varchar(255) DEFAULT NULL,
  `googlemap_link` longtext,
  `email` varchar(255) DEFAULT NULL,
  `phone_number` varchar(255) DEFAULT NULL,
  `description` longtext,
  `website_link` varchar(255) DEFAULT NULL,
  `donation_link` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shelter`
--

LOCK TABLES `shelter` WRITE;
/*!40000 ALTER TABLE `shelter` DISABLE KEYS */;
INSERT INTO `shelter` VALUES (1,'AnimalsLebanon','Hamra, Beirut, Lebanon','PO Box 113-5859','https://www.google.com/maps/embed/v1/place?q=animals+lebanon&key=AIzaSyBFw0Qbyq9zTFTd-tUY6dZWTgaQzuU17R8','contact@animalslebanon.org','+961 01 751 678','At Animals Lebanon, our aim is to enact and enforce comprehensive national animal protection and welfare legislation, increase compliance with international regulations, and empower civil society to improve animal welfare. Currently, we are campaigning for the enactment of national animal protection and welfare laws, providing nationwide assistance for companion animals in need, working to close down substandard zoos, and rescuing and caring for both companion animals and endangered wildlife. Our notable achievements include the successful approval of national animal protection legislation, Lebanons membership in CITES, the establishment of a model shelter, the closure of abusive zoos and rehoming of over 100 animals, and collaborations with sanctuaries worldwide to rehome endangered exotic pets. We also proudly represent Lebanon at conferences of organizations such as the OIE, CITES, and the European Commission, and have been selected by the OIE to contribute to the development of a regional animal welfare strategy.','www.animalslebanon.org','www.animalslebanon.org/donate'),(2,'BETAAnimals',' RGPV+PXR, Baabda','PO Box 115-9932','https://www.google.com/maps/embed/v1/place?q=Beta+animals&key=AIzaSyBFw0Qbyq9zTFTd-tUY6dZWTgaQzuU17R8','contact@betalebanon.org','+961 70 248 765','BETA is one of the most active animal shelters in Lebanon and also the first to initiate and start rescuing dogs, cats and other species of wildlife in its founding country. Rescues often take place in life threatening situations for the animals and are most often at times dangerous or difficult to accomplish, yet BETA strives to make every mechanism of their rescues a success. Our mission is to strive towards ensuring that one day all animals in Lebanon will get the chance to live safely and securely. It’s our goal to educate individuals and take direct action to help animals in Lebanon live the life they deserve, for we all belong to this planet and it is home to all of us.','www.betalebanon.org','www.betalebanon.org/get-involved/donate/');
/*!40000 ALTER TABLE `shelter` ENABLE KEYS */;
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
