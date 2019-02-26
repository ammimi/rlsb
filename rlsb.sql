/*
Navicat MySQL Data Transfer

Source Server         : 192.168.81.128
Source Server Version : 50716
Source Host           : 192.168.81.128:3306
Source Database       : rlsb1

Target Server Type    : MYSQL
Target Server Version : 50716
File Encoding         : 65001

Date: 2019-02-26 18:14:42
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `attendance_attendanceinfo`
-- ----------------------------
DROP TABLE IF EXISTS `attendance_attendanceinfo`;
CREATE TABLE `attendance_attendanceinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  `facedata_id` int(11) NOT NULL,
  `recorded_datetime` datetime(6) DEFAULT NULL,
  `recorded_img_url` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `attendance_attendanc_facedata_id_977a2c83_fk_facedata_` (`facedata_id`),
  CONSTRAINT `attendance_attendanc_facedata_id_977a2c83_fk_facedata_` FOREIGN KEY (`facedata_id`) REFERENCES `facedata_facedata` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of attendance_attendanceinfo
-- ----------------------------

-- ----------------------------
-- Table structure for `attendance_imagetmp`
-- ----------------------------
DROP TABLE IF EXISTS `attendance_imagetmp`;
CREATE TABLE `attendance_imagetmp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of attendance_imagetmp
-- ----------------------------

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
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;

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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('12', 'attendance', 'attendanceinfo');
INSERT INTO `django_content_type` VALUES ('13', 'attendance', 'imagetmp');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('11', 'facedata', 'facedata');
INSERT INTO `django_content_type` VALUES ('5', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('7', 'system', 'menu');
INSERT INTO `django_content_type` VALUES ('8', 'system', 'role');
INSERT INTO `django_content_type` VALUES ('9', 'system', 'structure');
INSERT INTO `django_content_type` VALUES ('10', 'system', 'systemsetup');
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
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;

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
INSERT INTO `django_migrations` VALUES ('24', 'system', '0002_auto_20181115_2124', '2018-12-25 08:46:46.379211');
INSERT INTO `django_migrations` VALUES ('25', 'system', '0003_systemsetup', '2018-12-25 08:46:46.451974');
INSERT INTO `django_migrations` VALUES ('26', 'facedata', '0002_auto_20190225_1042', '2019-02-25 10:42:37.612045');
INSERT INTO `django_migrations` VALUES ('27', 'attendance', '0002_auto_20190225_1042', '2019-02-25 10:47:16.553009');
INSERT INTO `django_migrations` VALUES ('28', 'system', '0004_auto_20190225_1042', '2019-02-25 10:47:16.558686');

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
INSERT INTO `django_session` VALUES ('b1we2doxn1fmnfhoim4frvlci7ksbdbj', 'N2I0Yzg0OTRkZTdmMmI3ZGQxMmRhOTEyYzU3MjA3ZDJjMzcwY2E2OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1ODQ1YzNlY2EyNWYzMGM3N2JhYTUxNzg3NjFiMGY5MmFkNTZjOWQ4In0=', '2019-02-04 09:15:32.638127');
INSERT INTO `django_session` VALUES ('bira4q654fttxkcsuvzo0q8k9it3tub2', 'OGVkMWQ4M2FkZmJlNjY3MzdkM2NiZmY1OTg2MmYwZWYyOGIwMDBjNjp7Il9hdXRoX3VzZXJfaGFzaCI6IjU4NDVjM2VjYTI1ZjMwYzc3YmFhNTE3ODc2MWIwZjkyYWQ1NmM5ZDgiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2019-01-08 02:56:56.141823');
INSERT INTO `django_session` VALUES ('cf6h3014ofi1cgndzdsg23aaa6eoofxo', 'N2I0Yzg0OTRkZTdmMmI3ZGQxMmRhOTEyYzU3MjA3ZDJjMzcwY2E2OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1ODQ1YzNlY2EyNWYzMGM3N2JhYTUxNzg3NjFiMGY5MmFkNTZjOWQ4In0=', '2019-01-11 00:47:20.610485');
INSERT INTO `django_session` VALUES ('e0w6py1xq7k9p66uxvfbxm3hubsqez4m', 'YzBkMjNhYmQ3N2NiYTZkNDg5NGJhNDY2MDM0NWExNGNlOWUzNjA5Zjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTg0NWMzZWNhMjVmMzBjNzdiYWE1MTc4NzYxYjBmOTJhZDU2YzlkOCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2019-01-08 15:03:56.045638');
INSERT INTO `django_session` VALUES ('j0ccxsy7qte437h899o9dkw57ij1cdve', 'N2I0Yzg0OTRkZTdmMmI3ZGQxMmRhOTEyYzU3MjA3ZDJjMzcwY2E2OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1ODQ1YzNlY2EyNWYzMGM3N2JhYTUxNzg3NjFiMGY5MmFkNTZjOWQ4In0=', '2019-02-04 09:23:59.720790');
INSERT INTO `django_session` VALUES ('pgtqcpy92zdn7ghafuq6b29l2vrutifs', 'N2I0Yzg0OTRkZTdmMmI3ZGQxMmRhOTEyYzU3MjA3ZDJjMzcwY2E2OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1ODQ1YzNlY2EyNWYzMGM3N2JhYTUxNzg3NjFiMGY5MmFkNTZjOWQ4In0=', '2019-03-14 10:18:45.944336');
INSERT INTO `django_session` VALUES ('u5i7dyv6kq9ia10942spaa8petx0zups', 'N2I0Yzg0OTRkZTdmMmI3ZGQxMmRhOTEyYzU3MjA3ZDJjMzcwY2E2OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1ODQ1YzNlY2EyNWYzMGM3N2JhYTUxNzg3NjFiMGY5MmFkNTZjOWQ4In0=', '2019-03-15 10:14:36.959488');
INSERT INTO `django_session` VALUES ('u77zili4ya08jbkebn26a0itnm7ramas', 'N2I0Yzg0OTRkZTdmMmI3ZGQxMmRhOTEyYzU3MjA3ZDJjMzcwY2E2OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1ODQ1YzNlY2EyNWYzMGM3N2JhYTUxNzg3NjFiMGY5MmFkNTZjOWQ4In0=', '2019-03-14 09:46:07.798332');
INSERT INTO `django_session` VALUES ('usasph2aw7xompoohbhqgwq86a4vwdlp', 'MTlhNGJjYzQwNjQ1MWE2ODc3OTgzNjhjZWEyYWVjMDdiMzQxZThjZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTg0NWMzZWNhMjVmMzBjNzdiYWE1MTc4NzYxYjBmOTJhZDU2YzlkOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2019-01-09 08:21:51.915633');
INSERT INTO `django_session` VALUES ('uwjobvj1ms7vxmjp00ssx6y7itd5k151', 'MTlhNGJjYzQwNjQ1MWE2ODc3OTgzNjhjZWEyYWVjMDdiMzQxZThjZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTg0NWMzZWNhMjVmMzBjNzdiYWE1MTc4NzYxYjBmOTJhZDU2YzlkOCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2019-01-08 16:15:45.821189');
INSERT INTO `django_session` VALUES ('uxm0zq1407mxjyjyuz81aa0hdsk9kumk', 'NmU3OGFmNTUyYmEzZjU0NWFmMTgwMmJjYWRlNDMzYWU1NTVjNzBkZjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2hhc2giOiI1ODQ1YzNlY2EyNWYzMGM3N2JhYTUxNzg3NjFiMGY5MmFkNTZjOWQ4In0=', '2019-01-08 06:42:30.641188');
INSERT INTO `django_session` VALUES ('ygrm9n5c42t6p80c1lh9kzprr3hps9o5', 'N2I0Yzg0OTRkZTdmMmI3ZGQxMmRhOTEyYzU3MjA3ZDJjMzcwY2E2OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1ODQ1YzNlY2EyNWYzMGM3N2JhYTUxNzg3NjFiMGY5MmFkNTZjOWQ4In0=', '2019-03-03 03:26:15.179511');

-- ----------------------------
-- Table structure for `facedata_facedata`
-- ----------------------------
DROP TABLE IF EXISTS `facedata_facedata`;
CREATE TABLE `facedata_facedata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `face_id` varchar(30) DEFAULT NULL,
  `face_name` varchar(30) NOT NULL,
  `face_cname` varchar(30) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `face_image` varchar(100) DEFAULT NULL,
  `ifsync` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `face_id` (`face_id`),
  KEY `facedata_facedata_owner_id_88d8a264_fk_system_userprofile_id` (`owner_id`),
  CONSTRAINT `facedata_facedata_owner_id_88d8a264_fk_system_userprofile_id` FOREIGN KEY (`owner_id`) REFERENCES `system_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of facedata_facedata
-- ----------------------------

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
  `parent_id` int(11) DEFAULT NULL,
  `number` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `url` (`url`),
  KEY `system_menu_parent_id_c715739f_fk_system_menu_id` (`parent_id`),
  CONSTRAINT `system_menu_parent_id_c715739f_fk_system_menu_id` FOREIGN KEY (`parent_id`) REFERENCES `system_menu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of system_menu
-- ----------------------------
INSERT INTO `system_menu` VALUES ('1', '系统', '', 'SYSTEM', '/system/', null, '1');
INSERT INTO `system_menu` VALUES ('2', '基础设置', 'fa fa-gg', 'SYSTEM-BASIC', '', '1', '1.1');
INSERT INTO `system_menu` VALUES ('3', '组织架构', '', 'SYSTEM-BASIC-STRUCTURE', '/system/basic/structure/', '2', '1.11');
INSERT INTO `system_menu` VALUES ('4', '组织架构：列表', '', 'SYSTEM-BASIC-STRUCTURE-LIST', '/system/basic/structure/list/', '3', '1.111');
INSERT INTO `system_menu` VALUES ('5', '组织架构：创建', '', 'SYSTEM-BASIC-STRUCTURE-CREATE', '/system/basic/structure/create/', '3', '1.112');
INSERT INTO `system_menu` VALUES ('6', '组织架构：删除', '', 'SYSTEM-BASIC-STRUCTURE-DELETE', '/system/basic/structure/delete/', '3', '1.113');
INSERT INTO `system_menu` VALUES ('7', '组织架构：关联用户', '', 'SYSTEM-BASIC-STRUCTURE-ADD_USER', '/system/basic/structure/add_user/', '3', '1.114');
INSERT INTO `system_menu` VALUES ('8', '用户管理', '', 'SYSTEM-BASIC-USER', '/system/basic/user/', '2', '1.12');
INSERT INTO `system_menu` VALUES ('9', '用户管理：列表', '', 'SYSTEM-BASIC-USER-LIST', '/system/basic/user/list/', '8', '1.121');
INSERT INTO `system_menu` VALUES ('10', '用户管理：详情', '', 'SYSTEM-BASIC-USER-DETAIL', '/system/basic/user/detail/', '8', '1.122');
INSERT INTO `system_menu` VALUES ('11', '用户管理：修改', '', 'SYSTEM-BASIC-USER-UPDATE', '/system/basic/user/update/', '8', '1.123');
INSERT INTO `system_menu` VALUES ('12', '用户管理：创建', '', 'SYSTEM-BASIC-USER-CREATE', '/system/basic/user/create/', '8', '1.123');
INSERT INTO `system_menu` VALUES ('13', '用户管理：删除', '', 'SYSTEM-BASIC-USER-DELETE', '/system/basic/user/delete/', '8', '1.124');
INSERT INTO `system_menu` VALUES ('14', '用户管理：启用', '', 'SYSTEM-BASIC-USER-ENABLE', '/system/basic/user/enable/', '8', '1.125');
INSERT INTO `system_menu` VALUES ('15', '用户管理：禁用', '', 'SYSTEM-BASIC-USER-DISABLE', '/system/basic/user/disable/', '8', '1.126');
INSERT INTO `system_menu` VALUES ('16', '用户管理：修改密码', '', 'SYSTEM-BASIC-USER-PASSWORD_CHANGE', '/system/basic/user/password_change/', '8', '1.127');
INSERT INTO `system_menu` VALUES ('17', '权限管理', 'fa fa-user-plus', 'SYSTEM-RBAC', null, '1', '1.2');
INSERT INTO `system_menu` VALUES ('18', '菜单管理', '', 'SYSTEM-RBAC-MENU', '/system/rbac/menu/', '17', '1.21');
INSERT INTO `system_menu` VALUES ('19', '菜单管理：创建', '', 'SYSTEM-RBAC-MENU-CREATE', '/system/rbac/menu/create/', '18', '1.211');
INSERT INTO `system_menu` VALUES ('20', '菜单管理：修改', '', 'SYSTEM-RBAC-MENU-UPDATE', '/system/rbac/menu/update/', '18', '1.213');
INSERT INTO `system_menu` VALUES ('21', '角色管理', '', 'SYSTEM-RBAC-ROLE', '/system/rbac/role/', '17', '1.22');
INSERT INTO `system_menu` VALUES ('22', '角色管理：列表', '', 'SYSTEM-RBAC-ROLE-LIST', '/system/rbac/role/list/', '21', '1.221');
INSERT INTO `system_menu` VALUES ('23', '角色管理：创建', '', 'SYSTEM-RBAC-ROLE-CREATE', '/system/rbac/role/create/', '21', '1.222');
INSERT INTO `system_menu` VALUES ('24', '角色管理：修改', '', 'SYSTEM-RBAC-ROLE-UPDATE', '/system/rbac/role/update/', '21', '1.223');
INSERT INTO `system_menu` VALUES ('25', '角色管理：删除', '', 'SYSTEM-RBAC-ROLE-DELETE', '/system/rbac/role/delete/', '21', '1.224');
INSERT INTO `system_menu` VALUES ('26', '角色管理：关联菜单', '', 'SYSTEM-RBAC-ROLE-ROLE2MENU', '/system/rbac/role/role2menu/', '21', '1.225');
INSERT INTO `system_menu` VALUES ('27', '角色管理：菜单列表', '', 'SYSTEM-RBAC-ROLE-ROLE2MENU_LIST', '/system/rbac/role/role2menu_list/', '21', '1.226');
INSERT INTO `system_menu` VALUES ('28', '角色管理：关联用户', '', 'SYSTEM-RBAC-ROLE-ROLE2USER', '/system/rbac/role/role2user/', '21', '1.227');
INSERT INTO `system_menu` VALUES ('29', '系统工具', 'fa fa-wrench', 'SYSTEM-TOOLS', null, '1', '1.3');
INSERT INTO `system_menu` VALUES ('30', '系统设置', '', 'SYSTEM-TOOLS-SYSTEM_SETUP', '/system/tools/system_setup/', '29', '1.31');
INSERT INTO `system_menu` VALUES ('49', '考勤管理', null, 'OA', '/oa/', null, '2');
INSERT INTO `system_menu` VALUES ('50', '人脸信息', 'fa fa-user', 'OA-FACEDATA', '/oa/facedata/', '49', '2.1');
INSERT INTO `system_menu` VALUES ('51', '人脸信息：列表', null, 'OA-FACEDATA-LIST', '/oa/facedata/list/', '50', '2.11');
INSERT INTO `system_menu` VALUES ('52', '人脸信息：创建', null, 'OA-FACEDATA-CREATE', '/oa/facedata/create/', '50', '2.12');
INSERT INTO `system_menu` VALUES ('53', '人脸信息：修改', null, 'OA-FACEDATA-UPDATE', '/oa/facedata/update/', '50', '2.13');
INSERT INTO `system_menu` VALUES ('54', '人脸信息：删除', null, 'OA-FACEDATA-DELETE', '/oa/facedata/delete/', '50', '2.14');
INSERT INTO `system_menu` VALUES ('55', '人脸信息：详情', null, 'OA-FACEDATA-DETAIL', '/oa/facedata/detail/', '50', '2.15');
INSERT INTO `system_menu` VALUES ('56', '考勤信息', 'fa fa-user', 'OA-ATTENDANCE', '/oa/attendance/', '49', '2.2');
INSERT INTO `system_menu` VALUES ('57', '考勤信息：列表', '', 'OA-ATTENDANCE-LIST', '/oa/attendance/list/', '56', '2.21');
INSERT INTO `system_menu` VALUES ('58', '考勤信息：创建', '', 'OA-ATTENDANCE-CREATE', '/oa/attendance/create/', '56', '2.22');
INSERT INTO `system_menu` VALUES ('59', '考勤信息：修改', '', 'OA-ATTENDANCE-UPDATE', '/oa/attendance/update/', '56', '2.23');
INSERT INTO `system_menu` VALUES ('60', '考勤信息：删除', '', 'OA-ATTENDANCE-DELETE', '/oa/attendance/delete/', '56', '2.24');
INSERT INTO `system_menu` VALUES ('61', '考勤信息：详情', '', 'OA-ATTENDANCE-DETAIL', '/oa/attendance/detail/', '56', '2.25');

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
INSERT INTO `system_role` VALUES ('1', '系统管理员', '系统初始角色组-包含系统所有权限');
INSERT INTO `system_role` VALUES ('2', '公司级管理员', '公司级管理员');
INSERT INTO `system_role` VALUES ('3', '部门管理员', '部门管理员');

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
) ENGINE=InnoDB AUTO_INCREMENT=454 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of system_role_permissions
-- ----------------------------
INSERT INTO `system_role_permissions` VALUES ('411', '1', '1');
INSERT INTO `system_role_permissions` VALUES ('412', '1', '2');
INSERT INTO `system_role_permissions` VALUES ('413', '1', '3');
INSERT INTO `system_role_permissions` VALUES ('414', '1', '4');
INSERT INTO `system_role_permissions` VALUES ('415', '1', '5');
INSERT INTO `system_role_permissions` VALUES ('416', '1', '6');
INSERT INTO `system_role_permissions` VALUES ('417', '1', '7');
INSERT INTO `system_role_permissions` VALUES ('418', '1', '8');
INSERT INTO `system_role_permissions` VALUES ('419', '1', '9');
INSERT INTO `system_role_permissions` VALUES ('420', '1', '10');
INSERT INTO `system_role_permissions` VALUES ('421', '1', '11');
INSERT INTO `system_role_permissions` VALUES ('422', '1', '12');
INSERT INTO `system_role_permissions` VALUES ('423', '1', '13');
INSERT INTO `system_role_permissions` VALUES ('424', '1', '14');
INSERT INTO `system_role_permissions` VALUES ('425', '1', '15');
INSERT INTO `system_role_permissions` VALUES ('426', '1', '16');
INSERT INTO `system_role_permissions` VALUES ('427', '1', '17');
INSERT INTO `system_role_permissions` VALUES ('428', '1', '18');
INSERT INTO `system_role_permissions` VALUES ('429', '1', '19');
INSERT INTO `system_role_permissions` VALUES ('430', '1', '20');
INSERT INTO `system_role_permissions` VALUES ('431', '1', '21');
INSERT INTO `system_role_permissions` VALUES ('432', '1', '22');
INSERT INTO `system_role_permissions` VALUES ('433', '1', '23');
INSERT INTO `system_role_permissions` VALUES ('434', '1', '24');
INSERT INTO `system_role_permissions` VALUES ('435', '1', '25');
INSERT INTO `system_role_permissions` VALUES ('436', '1', '26');
INSERT INTO `system_role_permissions` VALUES ('437', '1', '27');
INSERT INTO `system_role_permissions` VALUES ('438', '1', '28');
INSERT INTO `system_role_permissions` VALUES ('439', '1', '29');
INSERT INTO `system_role_permissions` VALUES ('440', '1', '30');
INSERT INTO `system_role_permissions` VALUES ('441', '1', '49');
INSERT INTO `system_role_permissions` VALUES ('442', '1', '50');
INSERT INTO `system_role_permissions` VALUES ('443', '1', '51');
INSERT INTO `system_role_permissions` VALUES ('444', '1', '52');
INSERT INTO `system_role_permissions` VALUES ('445', '1', '53');
INSERT INTO `system_role_permissions` VALUES ('446', '1', '54');
INSERT INTO `system_role_permissions` VALUES ('447', '1', '55');
INSERT INTO `system_role_permissions` VALUES ('448', '1', '56');
INSERT INTO `system_role_permissions` VALUES ('449', '1', '57');
INSERT INTO `system_role_permissions` VALUES ('450', '1', '58');
INSERT INTO `system_role_permissions` VALUES ('451', '1', '59');
INSERT INTO `system_role_permissions` VALUES ('452', '1', '60');
INSERT INTO `system_role_permissions` VALUES ('453', '1', '61');

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
  `level` int(10) unsigned NOT NULL,
  `lft` int(10) unsigned NOT NULL,
  `rght` int(10) unsigned NOT NULL,
  `tree_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `client_id` (`client_id`),
  KEY `system_structure_parent_id_cdaaaa0f_fk_system_structure_id` (`parent_id`),
  KEY `system_structure_level_595f85f8` (`level`),
  KEY `system_structure_lft_de38db17` (`lft`),
  KEY `system_structure_rght_33972d72` (`rght`),
  KEY `system_structure_tree_id_74919cdd` (`tree_id`),
  CONSTRAINT `system_structure_parent_id_cdaaaa0f_fk_system_structure_id` FOREIGN KEY (`parent_id`) REFERENCES `system_structure` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of system_structure
-- ----------------------------
INSERT INTO `system_structure` VALUES ('1', '公司a', 'unit', null, '公司a', '35', 'gsa', 'gsa123456', '0', '1', '6', '1');
INSERT INTO `system_structure` VALUES ('2', '部门1_a', 'department', '1', null, null, null, null, '1', '2', '5', '1');
INSERT INTO `system_structure` VALUES ('3', '公司b', 'unit', null, '公司b', '36', 'gsb', 'gsb123456', '0', '1', '2', '2');
INSERT INTO `system_structure` VALUES ('4', '部门甲_1_a', 'department', '2', null, null, null, null, '2', '3', '4', '1');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of system_userprofile
-- ----------------------------
INSERT INTO `system_userprofile` VALUES ('1', 'pbkdf2_sha256$120000$6ZojnpP9qM0v$A35O1VZ0PfQoWas/EfkJRzRZwDPvqWim5NPBc/xJB3s=', '2019-02-26 10:27:10.310552', '1', 'admin', '', '', '1', '1', '2018-11-15 21:24:42.002067', '管理员', null, 'male', '13800000000', 'robbie_han@outlook.com', 'image/default.jpg', null, null, null);
INSERT INTO `system_userprofile` VALUES ('2', 'pbkdf2_sha256$120000$xWY3HKEzEh4j$iUAemSHXOIUI+0sCaborxL3Ekfzy6vRCRK1AxO05MUA=', '2018-11-16 19:33:52.674442', '0', 'zhenglu', '', '', '0', '1', '2018-11-16 17:15:20.573879', '郑璐', '1989-10-21', 'male', '18651432008', 'zhenglu@sandbox.com', 'image/default.jpg', null, null, null);

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
