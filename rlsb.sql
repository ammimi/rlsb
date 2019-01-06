/*
Navicat MySQL Data Transfer

Source Server         : 192.168.187.129
Source Server Version : 50716
Source Host           : 192.168.187.129:3306
Source Database       : rlsb

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2019-01-06 14:45:40
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `attendance_attendanceinfo`
-- ----------------------------
DROP TABLE IF EXISTS `attendance_attendanceinfo`;
CREATE TABLE `attendance_attendanceinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `attendancetime` datetime(6) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `attendance_attendanc_owner_id_57ad5c86_fk_system_us` (`owner_id`),
  CONSTRAINT `attendance_attendanc_owner_id_57ad5c86_fk_system_us` FOREIGN KEY (`owner_id`) REFERENCES `system_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of attendance_attendanceinfo
-- ----------------------------
INSERT INTO `attendance_attendanceinfo` VALUES ('3', '2018-12-23 12:18:44.551142', '', '2');
INSERT INTO `attendance_attendanceinfo` VALUES ('4', '2018-12-23 12:19:00.293757', '', '2');
INSERT INTO `attendance_attendanceinfo` VALUES ('5', '2018-12-23 12:19:34.875583', '', '2');
INSERT INTO `attendance_attendanceinfo` VALUES ('6', '2018-12-23 15:13:43.134757', '', '2');
INSERT INTO `attendance_attendanceinfo` VALUES ('7', '2018-12-23 15:16:09.860177', '', '2');
INSERT INTO `attendance_attendanceinfo` VALUES ('9', '2018-12-23 15:38:48.299525', 'attendance/2018/12/timg_SQMscCZ.jpg', '2');
INSERT INTO `attendance_attendanceinfo` VALUES ('10', '2018-12-23 15:39:01.239600', 'attendance/2018/12/timg_7pRiOkh.jpg', '2');
INSERT INTO `attendance_attendanceinfo` VALUES ('11', '2018-12-23 15:39:12.839926', 'attendance/2018/12/timg_cIIWrl5.jpg', '2');

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '4', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '4', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '4', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can view content type', '4', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('17', 'Can add session', '5', 'add_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can change session', '5', 'change_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete session', '5', 'delete_session');
INSERT INTO `auth_permission` VALUES ('20', 'Can view session', '5', 'view_session');
INSERT INTO `auth_permission` VALUES ('21', 'Can add 用户信息', '6', 'add_userprofile');
INSERT INTO `auth_permission` VALUES ('22', 'Can change 用户信息', '6', 'change_userprofile');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete 用户信息', '6', 'delete_userprofile');
INSERT INTO `auth_permission` VALUES ('24', 'Can view 用户信息', '6', 'view_userprofile');
INSERT INTO `auth_permission` VALUES ('25', 'Can add 系统设置', '7', 'add_systemsetup');
INSERT INTO `auth_permission` VALUES ('26', 'Can change 系统设置', '7', 'change_systemsetup');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete 系统设置', '7', 'delete_systemsetup');
INSERT INTO `auth_permission` VALUES ('28', 'Can view 系统设置', '7', 'view_systemsetup');
INSERT INTO `auth_permission` VALUES ('29', 'Can add 组织架构', '8', 'add_structure');
INSERT INTO `auth_permission` VALUES ('30', 'Can change 组织架构', '8', 'change_structure');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete 组织架构', '8', 'delete_structure');
INSERT INTO `auth_permission` VALUES ('32', 'Can view 组织架构', '8', 'view_structure');
INSERT INTO `auth_permission` VALUES ('33', 'Can add role', '9', 'add_role');
INSERT INTO `auth_permission` VALUES ('34', 'Can change role', '9', 'change_role');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete role', '9', 'delete_role');
INSERT INTO `auth_permission` VALUES ('36', 'Can view role', '9', 'view_role');
INSERT INTO `auth_permission` VALUES ('37', 'Can add 菜单', '10', 'add_menu');
INSERT INTO `auth_permission` VALUES ('38', 'Can change 菜单', '10', 'change_menu');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete 菜单', '10', 'delete_menu');
INSERT INTO `auth_permission` VALUES ('40', 'Can view 菜单', '10', 'view_menu');
INSERT INTO `auth_permission` VALUES ('41', 'Can add 人脸样本信息', '11', 'add_facedata');
INSERT INTO `auth_permission` VALUES ('42', 'Can change 人脸样本信息', '11', 'change_facedata');
INSERT INTO `auth_permission` VALUES ('43', 'Can delete 人脸样本信息', '11', 'delete_facedata');
INSERT INTO `auth_permission` VALUES ('44', 'Can view 人脸样本信息', '11', 'view_facedata');
INSERT INTO `auth_permission` VALUES ('45', 'Can add 考勤信息', '12', 'add_attendanceinfo');
INSERT INTO `auth_permission` VALUES ('46', 'Can change 考勤信息', '12', 'change_attendanceinfo');
INSERT INTO `auth_permission` VALUES ('47', 'Can delete 考勤信息', '12', 'delete_attendanceinfo');
INSERT INTO `auth_permission` VALUES ('48', 'Can view 考勤信息', '12', 'view_attendanceinfo');

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_system_userprofile_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_system_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `system_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('12', 'attendance', 'attendanceinfo');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('11', 'facedata', 'facedata');
INSERT INTO `django_content_type` VALUES ('5', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('10', 'system', 'menu');
INSERT INTO `django_content_type` VALUES ('9', 'system', 'role');
INSERT INTO `django_content_type` VALUES ('8', 'system', 'structure');
INSERT INTO `django_content_type` VALUES ('7', 'system', 'systemsetup');
INSERT INTO `django_content_type` VALUES ('6', 'system', 'userprofile');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2018-12-22 10:10:36.229376');
INSERT INTO `django_migrations` VALUES ('2', 'contenttypes', '0002_remove_content_type_name', '2018-12-22 10:10:36.513273');
INSERT INTO `django_migrations` VALUES ('3', 'auth', '0001_initial', '2018-12-22 10:10:37.129287');
INSERT INTO `django_migrations` VALUES ('4', 'auth', '0002_alter_permission_name_max_length', '2018-12-22 10:10:37.225262');
INSERT INTO `django_migrations` VALUES ('5', 'auth', '0003_alter_user_email_max_length', '2018-12-22 10:10:37.251911');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0004_alter_user_username_opts', '2018-12-22 10:10:37.284888');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0005_alter_user_last_login_null', '2018-12-22 10:10:37.310185');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0006_require_contenttypes_0002', '2018-12-22 10:10:37.314561');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0007_alter_validators_add_error_messages', '2018-12-22 10:10:37.332331');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0008_alter_user_username_max_length', '2018-12-22 10:10:37.348534');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0009_alter_user_last_name_max_length', '2018-12-22 10:10:37.366079');
INSERT INTO `django_migrations` VALUES ('12', 'system', '0001_initial', '2018-12-22 10:10:38.460309');
INSERT INTO `django_migrations` VALUES ('13', 'admin', '0001_initial', '2018-12-22 10:10:38.593916');
INSERT INTO `django_migrations` VALUES ('14', 'admin', '0002_logentry_remove_auto_add', '2018-12-22 10:10:38.640068');
INSERT INTO `django_migrations` VALUES ('15', 'admin', '0003_logentry_add_action_flag_choices', '2018-12-22 10:10:38.671739');
INSERT INTO `django_migrations` VALUES ('16', 'sessions', '0001_initial', '2018-12-22 10:10:38.722328');
INSERT INTO `django_migrations` VALUES ('17', 'system', '0002_systemsetup', '2018-12-22 10:10:38.747014');
INSERT INTO `django_migrations` VALUES ('18', 'attendance', '0001_initial', '2018-12-22 23:01:28.992075');
INSERT INTO `django_migrations` VALUES ('19', 'facedata', '0001_initial', '2018-12-22 23:01:29.124098');
INSERT INTO `django_migrations` VALUES ('20', 'facedata', '0002_facedata_face_cname', '2018-12-22 23:54:28.433023');
INSERT INTO `django_migrations` VALUES ('21', 'facedata', '0003_auto_20181223_0004', '2018-12-23 00:04:52.894890');
INSERT INTO `django_migrations` VALUES ('22', 'facedata', '0004_auto_20181223_0014', '2018-12-23 00:14:51.125171');
INSERT INTO `django_migrations` VALUES ('23', 'attendance', '0002_auto_20181223_1112', '2018-12-23 11:12:17.072231');
INSERT INTO `django_migrations` VALUES ('24', 'attendance', '0003_auto_20181231_2148', '2018-12-31 21:48:20.103834');
INSERT INTO `django_migrations` VALUES ('25', 'facedata', '0005_auto_20181231_2148', '2018-12-31 21:48:20.273741');
INSERT INTO `django_migrations` VALUES ('26', 'facedata', '0006_facedata_ifsync', '2019-01-01 11:55:05.497768');
INSERT INTO `django_migrations` VALUES ('27', 'facedata', '0007_auto_20190105_2009', '2019-01-05 20:09:54.312231');
INSERT INTO `django_migrations` VALUES ('28', 'system', '0003_auto_20190106_1256', '2019-01-06 12:56:46.624555');
INSERT INTO `django_migrations` VALUES ('29', 'system', '0004_auto_20190106_1311', '2019-01-06 13:11:38.654782');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('473jxo46ebimckgqb20lq4tbm83qpb06', 'YzBkMjNhYmQ3N2NiYTZkNDg5NGJhNDY2MDM0NWExNGNlOWUzNjA5Zjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTg0NWMzZWNhMjVmMzBjNzdiYWE1MTc4NzYxYjBmOTJhZDU2YzlkOCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2019-01-08 15:40:36.621500');
INSERT INTO `django_session` VALUES ('52h6eu2shbgxti4emd41fm2o8bccc9rx', 'OGVkMWQ4M2FkZmJlNjY3MzdkM2NiZmY1OTg2MmYwZWYyOGIwMDBjNjp7Il9hdXRoX3VzZXJfaGFzaCI6IjU4NDVjM2VjYTI1ZjMwYzc3YmFhNTE3ODc2MWIwZjkyYWQ1NmM5ZDgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2019-01-10 13:39:12.122944');
INSERT INTO `django_session` VALUES ('bira4q654fttxkcsuvzo0q8k9it3tub2', 'OGVkMWQ4M2FkZmJlNjY3MzdkM2NiZmY1OTg2MmYwZWYyOGIwMDBjNjp7Il9hdXRoX3VzZXJfaGFzaCI6IjU4NDVjM2VjYTI1ZjMwYzc3YmFhNTE3ODc2MWIwZjkyYWQ1NmM5ZDgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2019-01-08 02:56:56.141823');
INSERT INTO `django_session` VALUES ('e0w6py1xq7k9p66uxvfbxm3hubsqez4m', 'YzBkMjNhYmQ3N2NiYTZkNDg5NGJhNDY2MDM0NWExNGNlOWUzNjA5Zjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTg0NWMzZWNhMjVmMzBjNzdiYWE1MTc4NzYxYjBmOTJhZDU2YzlkOCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2019-01-08 15:03:56.045638');
INSERT INTO `django_session` VALUES ('epc1sjg7k61u3jyq3fccnom4zt0jxnbh', 'N2I0Yzg0OTRkZTdmMmI3ZGQxMmRhOTEyYzU3MjA3ZDJjMzcwY2E2OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1ODQ1YzNlY2EyNWYzMGM3N2JhYTUxNzg3NjFiMGY5MmFkNTZjOWQ4In0=', '2019-01-23 06:40:13.326689');
INSERT INTO `django_session` VALUES ('gi7n2qozdlyfhouureij9f31a0ghukme', 'YzBkMjNhYmQ3N2NiYTZkNDg5NGJhNDY2MDM0NWExNGNlOWUzNjA5Zjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTg0NWMzZWNhMjVmMzBjNzdiYWE1MTc4NzYxYjBmOTJhZDU2YzlkOCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2019-01-17 14:16:11.676091');
INSERT INTO `django_session` VALUES ('k8cvhtuudmcj9z9h8ho4zjfybcqcqj7w', 'MTlhNGJjYzQwNjQ1MWE2ODc3OTgzNjhjZWEyYWVjMDdiMzQxZThjZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTg0NWMzZWNhMjVmMzBjNzdiYWE1MTc4NzYxYjBmOTJhZDU2YzlkOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2019-01-12 13:00:39.999146');
INSERT INTO `django_session` VALUES ('m5qgh5a13pvrh5knr4glv10v15cpi9lm', 'NmU3OGFmNTUyYmEzZjU0NWFmMTgwMmJjYWRlNDMzYWU1NTVjNzBkZjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2hhc2giOiI1ODQ1YzNlY2EyNWYzMGM3N2JhYTUxNzg3NjFiMGY5MmFkNTZjOWQ4In0=', '2019-01-22 08:45:30.770767');
INSERT INTO `django_session` VALUES ('q9pvmqql1puxm8q88785vmozxb3ir0wu', 'OGVkMWQ4M2FkZmJlNjY3MzdkM2NiZmY1OTg2MmYwZWYyOGIwMDBjNjp7Il9hdXRoX3VzZXJfaGFzaCI6IjU4NDVjM2VjYTI1ZjMwYzc3YmFhNTE3ODc2MWIwZjkyYWQ1NmM5ZDgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2019-01-18 04:32:48.221646');
INSERT INTO `django_session` VALUES ('usasph2aw7xompoohbhqgwq86a4vwdlp', 'MTlhNGJjYzQwNjQ1MWE2ODc3OTgzNjhjZWEyYWVjMDdiMzQxZThjZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTg0NWMzZWNhMjVmMzBjNzdiYWE1MTc4NzYxYjBmOTJhZDU2YzlkOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2019-01-09 08:21:51.915633');
INSERT INTO `django_session` VALUES ('uwjobvj1ms7vxmjp00ssx6y7itd5k151', 'MTlhNGJjYzQwNjQ1MWE2ODc3OTgzNjhjZWEyYWVjMDdiMzQxZThjZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTg0NWMzZWNhMjVmMzBjNzdiYWE1MTc4NzYxYjBmOTJhZDU2YzlkOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2019-01-08 16:15:45.821189');
INSERT INTO `django_session` VALUES ('uxm0zq1407mxjyjyuz81aa0hdsk9kumk', 'NmU3OGFmNTUyYmEzZjU0NWFmMTgwMmJjYWRlNDMzYWU1NTVjNzBkZjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2hhc2giOiI1ODQ1YzNlY2EyNWYzMGM3N2JhYTUxNzg3NjFiMGY5MmFkNTZjOWQ4In0=', '2019-01-08 06:42:30.641188');
INSERT INTO `django_session` VALUES ('v1jlcm7n2sdky1efhi4t4rh8prkzeyqi', 'MTlhNGJjYzQwNjQ1MWE2ODc3OTgzNjhjZWEyYWVjMDdiMzQxZThjZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTg0NWMzZWNhMjVmMzBjNzdiYWE1MTc4NzYxYjBmOTJhZDU2YzlkOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2019-01-22 13:46:30.987621');

-- ----------------------------
-- Table structure for `facedata_facedata`
-- ----------------------------
DROP TABLE IF EXISTS `facedata_facedata`;
CREATE TABLE `facedata_facedata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `face_id` varchar(30) DEFAULT NULL,
  `face_name` varchar(30) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `face_cname` varchar(30) NOT NULL,
  `face_image` varchar(100) DEFAULT NULL,
  `ifsync` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `face_id` (`face_id`),
  KEY `facedata_facedata_owner_id_88d8a264_fk_system_userprofile_id` (`owner_id`),
  CONSTRAINT `facedata_facedata_owner_id_88d8a264_fk_system_userprofile_id` FOREIGN KEY (`owner_id`) REFERENCES `system_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of facedata_facedata
-- ----------------------------
INSERT INTO `facedata_facedata` VALUES ('2', '36_80', 'zhenglu', '2', '郑璐', 'facedata/2018/12/timg.jpg', '1');
INSERT INTO `facedata_facedata` VALUES ('9', '36_82', 'ceshi1', '3', '测试1', 'facedata/2019/01/timg1_JdrOQQU.jpg', '1');

-- ----------------------------
-- Table structure for `system_menu`
-- ----------------------------
DROP TABLE IF EXISTS `system_menu`;
CREATE TABLE `system_menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `icon` varchar(50) DEFAULT NULL,
  `code` varchar(50) DEFAULT NULL,
  `url` varchar(128) DEFAULT NULL,
  `number` double DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `url` (`url`),
  KEY `system_menu_parent_id_c715739f_fk_system_menu_id` (`parent_id`),
  CONSTRAINT `system_menu_parent_id_c715739f_fk_system_menu_id` FOREIGN KEY (`parent_id`) REFERENCES `system_menu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of system_menu
-- ----------------------------
INSERT INTO `system_menu` VALUES ('1', '系统', '', 'SYSTEM', '/system/', '1', null);
INSERT INTO `system_menu` VALUES ('2', '基础设置', 'fa fa-gg', 'SYSTEM-BASIC', '', '1.1', '1');
INSERT INTO `system_menu` VALUES ('3', '组织架构', '', 'SYSTEM-BASIC-STRUCTURE', '/system/basic/structure/', '1.11', '2');
INSERT INTO `system_menu` VALUES ('4', '组织架构：列表', '', 'SYSTEM-BASIC-STRUCTURE-LIST', '/system/basic/structure/list/', '1.111', '3');
INSERT INTO `system_menu` VALUES ('5', '组织架构：创建', '', 'SYSTEM-BASIC-STRUCTURE-CREATE', '/system/basic/structure/create/', '1.112', '3');
INSERT INTO `system_menu` VALUES ('6', '组织架构：删除', '', 'SYSTEM-BASIC-STRUCTURE-DELETE', '/system/basic/structure/delete/', '1.113', '3');
INSERT INTO `system_menu` VALUES ('7', '组织架构：关联用户', '', 'SYSTEM-BASIC-STRUCTURE-ADD_USER', '/system/basic/structure/add_user/', '1.114', '3');
INSERT INTO `system_menu` VALUES ('8', '用户管理', '', 'SYSTEM-BASIC-USER', '/system/basic/user/', '1.12', '2');
INSERT INTO `system_menu` VALUES ('9', '用户管理：列表', '', 'SYSTEM-BASIC-USER-LIST', '/system/basic/user/list/', '1.121', '8');
INSERT INTO `system_menu` VALUES ('10', '用户管理：详情', '', 'SYSTEM-BASIC-USER-DETAIL', '/system/basic/user/detail/', '1.122', '8');
INSERT INTO `system_menu` VALUES ('11', '用户管理：修改', '', 'SYSTEM-BASIC-USER-UPDATE', '/system/basic/user/update/', '1.123', '8');
INSERT INTO `system_menu` VALUES ('12', '用户管理：创建', '', 'SYSTEM-BASIC-USER-CREATE', '/system/basic/user/create/', '1.123', '8');
INSERT INTO `system_menu` VALUES ('13', '用户管理：删除', '', 'SYSTEM-BASIC-USER-DELETE', '/system/basic/user/delete/', '1.124', '8');
INSERT INTO `system_menu` VALUES ('14', '用户管理：启用', '', 'SYSTEM-BASIC-USER-ENABLE', '/system/basic/user/enable/', '1.125', '8');
INSERT INTO `system_menu` VALUES ('15', '用户管理：禁用', '', 'SYSTEM-BASIC-USER-DISABLE', '/system/basic/user/disable/', '1.126', '8');
INSERT INTO `system_menu` VALUES ('16', '用户管理：修改密码', '', 'SYSTEM-BASIC-USER-PASSWORD_CHANGE', '/system/basic/user/password_change/', '1.127', '8');
INSERT INTO `system_menu` VALUES ('17', '权限管理', 'fa fa-user-plus', 'SYSTEM-RBAC', null, '1.2', '1');
INSERT INTO `system_menu` VALUES ('18', '菜单管理', '', 'SYSTEM-RBAC-MENU', '/system/rbac/menu/', '1.21', '17');
INSERT INTO `system_menu` VALUES ('19', '菜单管理：创建', '', 'SYSTEM-RBAC-MENU-CREATE', '/system/rbac/menu/create/', '1.211', '18');
INSERT INTO `system_menu` VALUES ('20', '菜单管理：修改', '', 'SYSTEM-RBAC-MENU-UPDATE', '/system/rbac/menu/update/', '1.213', '18');
INSERT INTO `system_menu` VALUES ('21', '角色管理', '', 'SYSTEM-RBAC-ROLE', '/system/rbac/role/', '1.22', '17');
INSERT INTO `system_menu` VALUES ('22', '角色管理：列表', '', 'SYSTEM-RBAC-ROLE-LIST', '/system/rbac/role/list/', '1.221', '21');
INSERT INTO `system_menu` VALUES ('23', '角色管理：创建', '', 'SYSTEM-RBAC-ROLE-CREATE', '/system/rbac/role/create/', '1.222', '21');
INSERT INTO `system_menu` VALUES ('24', '角色管理：修改', '', 'SYSTEM-RBAC-ROLE-UPDATE', '/system/rbac/role/update/', '1.223', '21');
INSERT INTO `system_menu` VALUES ('25', '角色管理：删除', '', 'SYSTEM-RBAC-ROLE-DELETE', '/system/rbac/role/delete/', '1.224', '21');
INSERT INTO `system_menu` VALUES ('26', '角色管理：关联菜单', '', 'SYSTEM-RBAC-ROLE-ROLE2MENU', '/system/rbac/role/role2menu/', '1.225', '21');
INSERT INTO `system_menu` VALUES ('27', '角色管理：菜单列表', '', 'SYSTEM-RBAC-ROLE-ROLE2MENU_LIST', '/system/rbac/role/role2menu_list/', '1.226', '21');
INSERT INTO `system_menu` VALUES ('28', '角色管理：关联用户', '', 'SYSTEM-RBAC-ROLE-ROLE2USER', '/system/rbac/role/role2user/', '1.227', '21');
INSERT INTO `system_menu` VALUES ('29', '系统工具', 'fa fa-wrench', 'SYSTEM-TOOLS', null, '1.3', '1');
INSERT INTO `system_menu` VALUES ('30', '系统设置', '', 'SYSTEM-TOOLS-SYSTEM_SETUP', '/system/tools/system_setup/', '1.31', '29');
INSERT INTO `system_menu` VALUES ('49', '考勤管理', null, 'OA', '/oa/', '2', null);
INSERT INTO `system_menu` VALUES ('50', '人脸信息', 'fa fa-user', 'OA-FACEDATA', '/oa/facedata/', '2.1', '49');
INSERT INTO `system_menu` VALUES ('51', '人脸信息：列表', null, 'OA-FACEDATA-LIST', '/oa/facedata/list/', '2.11', '50');
INSERT INTO `system_menu` VALUES ('52', '人脸信息：创建', null, 'OA-FACEDATA-CREATE', '/oa/facedata/create/', '2.12', '50');
INSERT INTO `system_menu` VALUES ('53', '人脸信息：修改', null, 'OA-FACEDATA-UPDATE', '/oa/facedata/update/', '2.13', '50');
INSERT INTO `system_menu` VALUES ('54', '人脸信息：删除', null, 'OA-FACEDATA-DELETE', '/oa/facedata/delete/', '2.14', '50');
INSERT INTO `system_menu` VALUES ('55', '人脸信息：详情', null, 'OA-FACEDATA-DETAIL', '/oa/facedata/detail/', '2.15', '50');
INSERT INTO `system_menu` VALUES ('56', '考勤信息', 'fa fa-calendar', 'OA-ATTENDANCE', '/oa/attendance/', '2.2', '49');
INSERT INTO `system_menu` VALUES ('57', '考勤信息：列表', '', 'OA-ATTENDANCE-LIST', '/oa/attendance/list/', '2.21', '56');
INSERT INTO `system_menu` VALUES ('58', '考勤信息：创建', '', 'OA-ATTENDANCE-CREATE', '/oa/attendance/create/', '2.22', '56');
INSERT INTO `system_menu` VALUES ('59', '考勤信息：修改', '', 'OA-ATTENDANCE-UPDATE', '/oa/attendance/update/', '2.23', '56');
INSERT INTO `system_menu` VALUES ('60', '考勤信息：删除', '', 'OA-ATTENDANCE-DELETE', '/oa/attendance/delete/', '2.24', '56');
INSERT INTO `system_menu` VALUES ('61', '考勤信息：详情', '', 'OA-ATTENDANCE-DETAIL', '/oa/attendance/detail/', '2.25', '56');
INSERT INTO `system_menu` VALUES ('62', '人脸信息：上传人脸信息', null, 'OA-ATTENDANCE-SENDFACEDATA', '/oa/facedata/sendfacedata/', '2.16', '50');
INSERT INTO `system_menu` VALUES ('63', '人脸信息：删除人脸信息', null, null, '/oa/facedata/deletefacedata/', '2.17', '50');
INSERT INTO `system_menu` VALUES ('64', '人脸信息：更新人脸信息', null, null, '/oa/facedata/updatefacedata/', '2.18', '50');
INSERT INTO `system_menu` VALUES ('65', '人脸信息：人工打卡', null, null, '/oa/facedata/manualclock/', '2.19', '50');
INSERT INTO `system_menu` VALUES ('66', '组织架构:创建客户信息', null, null, '/system/basic/structure/addclient/', '1.115', '3');
INSERT INTO `system_menu` VALUES ('67', '组织架构:删除客户信息', null, null, '/system/basic/structure/deleteclient/', '1.116', '3');
INSERT INTO `system_menu` VALUES ('68', '组织架构:更新客户信息', null, null, '/system/basic/structure/updateclient/', '1.117', '3');

-- ----------------------------
-- Table structure for `system_role`
-- ----------------------------
DROP TABLE IF EXISTS `system_role`;
CREATE TABLE `system_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `desc` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of system_role
-- ----------------------------
INSERT INTO `system_role` VALUES ('1', '系统管理', '系统初始角色组-包含系统所有权限');
INSERT INTO `system_role` VALUES ('2', '用户管理', '具有用户管理和组织架构管理权限');
INSERT INTO `system_role` VALUES ('3', '部门考勤管理员', '管理部门内考勤');
INSERT INTO `system_role` VALUES ('4', '公司考勤管理员', '管理全公司的考勤');

-- ----------------------------
-- Table structure for `system_role_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `system_role_permissions`;
CREATE TABLE `system_role_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NOT NULL,
  `menu_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `system_role_permissions_role_id_menu_id_91fb438a_uniq` (`role_id`,`menu_id`),
  KEY `system_role_permissions_menu_id_f48d14c7_fk_system_menu_id` (`menu_id`),
  CONSTRAINT `system_role_permissions_menu_id_f48d14c7_fk_system_menu_id` FOREIGN KEY (`menu_id`) REFERENCES `system_menu` (`id`),
  CONSTRAINT `system_role_permissions_role_id_a52abc64_fk_system_role_id` FOREIGN KEY (`role_id`) REFERENCES `system_role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=552 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of system_role_permissions
-- ----------------------------
INSERT INTO `system_role_permissions` VALUES ('502', '1', '1');
INSERT INTO `system_role_permissions` VALUES ('503', '1', '2');
INSERT INTO `system_role_permissions` VALUES ('504', '1', '3');
INSERT INTO `system_role_permissions` VALUES ('505', '1', '4');
INSERT INTO `system_role_permissions` VALUES ('506', '1', '5');
INSERT INTO `system_role_permissions` VALUES ('507', '1', '6');
INSERT INTO `system_role_permissions` VALUES ('508', '1', '7');
INSERT INTO `system_role_permissions` VALUES ('512', '1', '8');
INSERT INTO `system_role_permissions` VALUES ('513', '1', '9');
INSERT INTO `system_role_permissions` VALUES ('514', '1', '10');
INSERT INTO `system_role_permissions` VALUES ('516', '1', '11');
INSERT INTO `system_role_permissions` VALUES ('515', '1', '12');
INSERT INTO `system_role_permissions` VALUES ('517', '1', '13');
INSERT INTO `system_role_permissions` VALUES ('518', '1', '14');
INSERT INTO `system_role_permissions` VALUES ('519', '1', '15');
INSERT INTO `system_role_permissions` VALUES ('520', '1', '16');
INSERT INTO `system_role_permissions` VALUES ('521', '1', '17');
INSERT INTO `system_role_permissions` VALUES ('522', '1', '18');
INSERT INTO `system_role_permissions` VALUES ('523', '1', '19');
INSERT INTO `system_role_permissions` VALUES ('524', '1', '20');
INSERT INTO `system_role_permissions` VALUES ('525', '1', '21');
INSERT INTO `system_role_permissions` VALUES ('526', '1', '22');
INSERT INTO `system_role_permissions` VALUES ('527', '1', '23');
INSERT INTO `system_role_permissions` VALUES ('528', '1', '24');
INSERT INTO `system_role_permissions` VALUES ('529', '1', '25');
INSERT INTO `system_role_permissions` VALUES ('530', '1', '26');
INSERT INTO `system_role_permissions` VALUES ('531', '1', '27');
INSERT INTO `system_role_permissions` VALUES ('532', '1', '28');
INSERT INTO `system_role_permissions` VALUES ('533', '1', '29');
INSERT INTO `system_role_permissions` VALUES ('534', '1', '30');
INSERT INTO `system_role_permissions` VALUES ('535', '1', '49');
INSERT INTO `system_role_permissions` VALUES ('536', '1', '50');
INSERT INTO `system_role_permissions` VALUES ('537', '1', '51');
INSERT INTO `system_role_permissions` VALUES ('538', '1', '52');
INSERT INTO `system_role_permissions` VALUES ('539', '1', '53');
INSERT INTO `system_role_permissions` VALUES ('540', '1', '54');
INSERT INTO `system_role_permissions` VALUES ('541', '1', '55');
INSERT INTO `system_role_permissions` VALUES ('546', '1', '56');
INSERT INTO `system_role_permissions` VALUES ('547', '1', '57');
INSERT INTO `system_role_permissions` VALUES ('548', '1', '58');
INSERT INTO `system_role_permissions` VALUES ('549', '1', '59');
INSERT INTO `system_role_permissions` VALUES ('550', '1', '60');
INSERT INTO `system_role_permissions` VALUES ('551', '1', '61');
INSERT INTO `system_role_permissions` VALUES ('542', '1', '62');
INSERT INTO `system_role_permissions` VALUES ('543', '1', '63');
INSERT INTO `system_role_permissions` VALUES ('544', '1', '64');
INSERT INTO `system_role_permissions` VALUES ('545', '1', '65');
INSERT INTO `system_role_permissions` VALUES ('509', '1', '66');
INSERT INTO `system_role_permissions` VALUES ('510', '1', '67');
INSERT INTO `system_role_permissions` VALUES ('511', '1', '68');
INSERT INTO `system_role_permissions` VALUES ('220', '2', '1');
INSERT INTO `system_role_permissions` VALUES ('221', '2', '2');
INSERT INTO `system_role_permissions` VALUES ('222', '2', '3');
INSERT INTO `system_role_permissions` VALUES ('223', '2', '4');
INSERT INTO `system_role_permissions` VALUES ('224', '2', '5');
INSERT INTO `system_role_permissions` VALUES ('225', '2', '6');
INSERT INTO `system_role_permissions` VALUES ('226', '2', '7');
INSERT INTO `system_role_permissions` VALUES ('227', '2', '8');
INSERT INTO `system_role_permissions` VALUES ('228', '2', '9');
INSERT INTO `system_role_permissions` VALUES ('229', '2', '10');
INSERT INTO `system_role_permissions` VALUES ('230', '2', '11');
INSERT INTO `system_role_permissions` VALUES ('231', '2', '12');
INSERT INTO `system_role_permissions` VALUES ('232', '2', '13');
INSERT INTO `system_role_permissions` VALUES ('233', '2', '14');
INSERT INTO `system_role_permissions` VALUES ('234', '2', '15');
INSERT INTO `system_role_permissions` VALUES ('235', '2', '16');

-- ----------------------------
-- Table structure for `system_structure`
-- ----------------------------
DROP TABLE IF EXISTS `system_structure`;
CREATE TABLE `system_structure` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `type` varchar(20) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `client_cname` varchar(30) DEFAULT NULL,
  `client_id` varchar(30) DEFAULT NULL,
  `client_name` varchar(30) DEFAULT NULL,
  `client_secret` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `client_id` (`client_id`),
  KEY `system_structure_parent_id_cdaaaa0f_fk_system_structure_id` (`parent_id`),
  CONSTRAINT `system_structure_parent_id_cdaaaa0f_fk_system_structure_id` FOREIGN KEY (`parent_id`) REFERENCES `system_structure` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of system_structure
-- ----------------------------
INSERT INTO `system_structure` VALUES ('2', '考勤公司2', 'unit', null, '考勤公司2', '36', 'kaoqin2', '1234567890');

-- ----------------------------
-- Table structure for `system_systemsetup`
-- ----------------------------
DROP TABLE IF EXISTS `system_systemsetup`;
CREATE TABLE `system_systemsetup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `loginTitle` varchar(20) DEFAULT NULL,
  `mainTitle` varchar(20) DEFAULT NULL,
  `headTitle` varchar(20) DEFAULT NULL,
  `copyright` varchar(100) DEFAULT NULL,
  `url` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of system_systemsetup
-- ----------------------------
INSERT INTO `system_systemsetup` VALUES ('1', '人脸识别管理系统', '人脸识别', '人脸识别管理系统', 'Test', '');
INSERT INTO `system_systemsetup` VALUES ('6', '人脸考勤信息管理系统', '人脸考勤信息管理系统', '人脸考勤信息管理系统', 'Test', null);

-- ----------------------------
-- Table structure for `system_userprofile`
-- ----------------------------
DROP TABLE IF EXISTS `system_userprofile`;
CREATE TABLE `system_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `name` varchar(20) NOT NULL,
  `birthday` date DEFAULT NULL,
  `gender` varchar(10) NOT NULL,
  `mobile` varchar(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  `superior_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `system_userprofile_department_id_a46d57f9_fk_system_structure_id` (`department_id`),
  KEY `system_userprofile_superior_id_6b0fd92f_fk_system_userprofile_id` (`superior_id`),
  CONSTRAINT `system_userprofile_department_id_a46d57f9_fk_system_structure_id` FOREIGN KEY (`department_id`) REFERENCES `system_structure` (`id`),
  CONSTRAINT `system_userprofile_superior_id_6b0fd92f_fk_system_userprofile_id` FOREIGN KEY (`superior_id`) REFERENCES `system_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of system_userprofile
-- ----------------------------
INSERT INTO `system_userprofile` VALUES ('1', 'pbkdf2_sha256$120000$6ZojnpP9qM0v$A35O1VZ0PfQoWas/EfkJRzRZwDPvqWim5NPBc/xJB3s=', '2019-01-06 10:40:04.888278', '1', 'admin', '', '', '1', '1', '2018-11-15 21:24:42.002067', '管理员', null, 'male', '13800000000', 'robbie_han@outlook.com', 'image/default.jpg', null, null, null);
INSERT INTO `system_userprofile` VALUES ('2', 'pbkdf2_sha256$120000$xWY3HKEzEh4j$iUAemSHXOIUI+0sCaborxL3Ekfzy6vRCRK1AxO05MUA=', '2018-11-16 19:33:52.674442', '0', 'zhenglu', '', '', '0', '1', '2018-11-16 17:15:20.573879', '郑璐', '1989-10-21', 'male', '18651432008', 'zhenglu@sandbox.com', 'image/default.jpg', null, '2', null);
INSERT INTO `system_userprofile` VALUES ('3', 'pbkdf2_sha256$120000$4emzWPQS35BT$5+1PCk/0p6eEZDHY6yp4aVH5o7bOHdqhQNWspuhlWhQ=', null, '0', 'ceshi1', '', '', '0', '1', '2019-01-05 20:36:30.487201', '测试1', null, 'male', '13195988875', '13195988875@163.com', 'image/default.jpg', null, '2', null);
INSERT INTO `system_userprofile` VALUES ('4', 'pbkdf2_sha256$120000$xbIHIyWUrhst$W/kTrF96y0EOMAoGD8InJi+FwIoNDu7Xr3adxBGgswc=', null, '0', 'ceshi2', '', '', '0', '1', '2019-01-05 20:42:13.150093', '测试2', null, 'male', '13195988876', '13195988876@163.com', 'image/default.jpg', null, '2', null);
INSERT INTO `system_userprofile` VALUES ('5', 'pbkdf2_sha256$120000$WyykkdiwNbDl$Lhq7TuM9hvqxlFe6TNysQKN/XUc3ZQf0z3oWeUV84VY=', null, '0', 'ceshi3', '', '', '0', '1', '2019-01-05 20:48:36.622009', '测试3', null, 'male', '13195988877', '13195988877@163.com', 'image/default.jpg', null, '2', null);
INSERT INTO `system_userprofile` VALUES ('6', 'pbkdf2_sha256$120000$O1Op2UrI05Lz$eHnOW1Cqc7q32ywp8dQI2sEXPU4ENfxZzmNbohPtAYQ=', null, '0', 'ceshi4', '', '', '0', '1', '2019-01-05 20:56:51.216363', '测试4', null, 'male', '13195988878', '13195988878@163.com', 'image/default.jpg', null, '2', null);

-- ----------------------------
-- Table structure for `system_userprofile_groups`
-- ----------------------------
DROP TABLE IF EXISTS `system_userprofile_groups`;
CREATE TABLE `system_userprofile_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `system_userprofile_groups_userprofile_id_group_id_23d17c47_uniq` (`userprofile_id`,`group_id`),
  KEY `system_userprofile_groups_group_id_0d309489_fk_auth_group_id` (`group_id`),
  CONSTRAINT `system_userprofile_g_userprofile_id_727b82a9_fk_system_us` FOREIGN KEY (`userprofile_id`) REFERENCES `system_userprofile` (`id`),
  CONSTRAINT `system_userprofile_groups_group_id_0d309489_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of system_userprofile_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `system_userprofile_roles`
-- ----------------------------
DROP TABLE IF EXISTS `system_userprofile_roles`;
CREATE TABLE `system_userprofile_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `system_userprofile_roles_userprofile_id_role_id_459e3bc3_uniq` (`userprofile_id`,`role_id`),
  KEY `system_userprofile_roles_role_id_cc2781b0_fk_system_role_id` (`role_id`),
  CONSTRAINT `system_userprofile_r_userprofile_id_0247f4f3_fk_system_us` FOREIGN KEY (`userprofile_id`) REFERENCES `system_userprofile` (`id`),
  CONSTRAINT `system_userprofile_roles_role_id_cc2781b0_fk_system_role_id` FOREIGN KEY (`role_id`) REFERENCES `system_role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of system_userprofile_roles
-- ----------------------------
INSERT INTO `system_userprofile_roles` VALUES ('1', '1', '1');
INSERT INTO `system_userprofile_roles` VALUES ('2', '1', '2');
INSERT INTO `system_userprofile_roles` VALUES ('3', '2', '2');

-- ----------------------------
-- Table structure for `system_userprofile_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `system_userprofile_user_permissions`;
CREATE TABLE `system_userprofile_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `system_userprofile_user__userprofile_id_permissio_6a5a6534_uniq` (`userprofile_id`,`permission_id`),
  KEY `system_userprofile_u_permission_id_bf146b97_fk_auth_perm` (`permission_id`),
  CONSTRAINT `system_userprofile_u_permission_id_bf146b97_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `system_userprofile_u_userprofile_id_9192044d_fk_system_us` FOREIGN KEY (`userprofile_id`) REFERENCES `system_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of system_userprofile_user_permissions
-- ----------------------------
