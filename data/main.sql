/*
 Navicat Premium Data Transfer

 Source Server         : MoMa
 Source Server Type    : SQLite
 Source Server Version : 3042000
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3042000
 File Encoding         : 65001

 Date: 17/04/2024 10:00:55
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for Artists
-- ----------------------------
DROP TABLE IF EXISTS "Artists";
CREATE TABLE "Artists" (
  "ConstituentID" INTEGER(10) NOT NULL,
  "DisplayName" TEXT(255),
  "ArtistBio" TEXT(100),
  "NationalityID" INTEGER(10),
  "Gender" TEXT(10),
  "BeginDate" integer(10),
  "EndDate" i(10),
  "WikiQID" TEXT(15),
  "ULAN" TEXT(15),
  PRIMARY KEY ("ConstituentID")
);

-- ----------------------------
-- Table structure for ArtworkArtists
-- ----------------------------
DROP TABLE IF EXISTS "ArtworkArtists";
CREATE TABLE "ArtworkArtists" (
  "ConstituentID" INTEGER(10) NOT NULL,
  "ObjectID" INTEGER(10) NOT NULL,
  PRIMARY KEY ("ConstituentID", "ObjectID")
);

-- ----------------------------
-- Table structure for Artworks
-- ----------------------------
DROP TABLE IF EXISTS "Artworks";
CREATE TABLE "Artworks" (
  "objectID" INTEGER(10) NOT NULL,
  "Title" TEXT(200),
  "Dimenssions" TEXT(100),
  "CreditLine" TEXT(1000),
  "AccessionNumber" text(15),
  "DateAcquired" text(10),
  "Catalogued" text(1),
  "URL" TEXT(255),
  "ImageURL" TEXT(255),
  "Circumeferance" real(10,2),
  "Depth" real(10,2),
  "Diameter" real(10,2),
  "Height" real(10,2),
  "Length" REAL(10,2),
  "Weight" REAL(10,2),
  "Width" REAL(10,2),
  "SeatHeight" REAL(10,2),
  "Duration" real(10,2),
  "Medium" integer(5),
  "Classification" integer(5),
  "Department" integer(5),
  "OnView" integer(5),
  PRIMARY KEY ("objectID")
);

-- ----------------------------
-- Table structure for Classifications
-- ----------------------------
DROP TABLE IF EXISTS "Classifications";
CREATE TABLE "Classifications" (
  "ClassificationID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "Classification" TEXT(255)
);

-- ----------------------------
-- Table structure for Departments
-- ----------------------------
DROP TABLE IF EXISTS "Departments";
CREATE TABLE "Departments" (
  "DepartmentID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "Department" TEXT(255)
);

-- ----------------------------
-- Table structure for Nationalities
-- ----------------------------
DROP TABLE IF EXISTS "Nationalities";
CREATE TABLE "Nationalities" (
  "NationalityID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "Nationality" TEXT(20)
);

-- ----------------------------
-- Table structure for OnViews
-- ----------------------------
DROP TABLE IF EXISTS "OnViews";
CREATE TABLE "OnViews" (
  "OnViewID" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "OnView" TEXT(255)
);


PRAGMA foreign_keys = true;
