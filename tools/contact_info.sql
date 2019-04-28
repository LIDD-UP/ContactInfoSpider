/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80015
 Source Host           : localhost:3306
 Source Schema         : contact_info

 Target Server Type    : MySQL
 Target Server Version : 80015
 File Encoding         : 65001

 Date: 18/04/2019 10:01:05
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for truth_finder_contact_info
-- ----------------------------
DROP TABLE IF EXISTS `truth_finder_contact_info`;
CREATE TABLE `truth_finder_contact_info`  (
  `contact_info_json` json NULL,
  `address_id` int(11) GENERATED ALWAYS AS (cast(json_extract(`contact_info_json`,_utf8mb4'$.masterContactId') as signed)) VIRTUAL NOT NULL,
  INDEX `address_id`(`address_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
