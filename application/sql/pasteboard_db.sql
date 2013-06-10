CREATE TABLE IF NOT EXISTS pasteboard.pb_users (
    id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    email VARCHAR(254),
    password VARCHAR(32),
    invitekey VARCHAR(32),
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS pasteboard.pb_userdata(
    id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    user_id INTEGER UNSIGNED NOT NULL,
    username VARCHAR(32),
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS pasteboard.pb_pastes(
    id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    group_id INTEGER UNSIGNED NOT NULL ,
    parent_id INTEGER UNSIGNED,
    category_id INTEGER UNSIGNED,
	user_id INTEGER UNSIGNED,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS pasteboard.pb_pastescontent (
    id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    paste_id INTEGER UNSIGNED,
    datum DATETIME,
	title VARCHAR(254),
    content BLOB,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS pasteboard.pb_groupusers (
    group_id INTEGER UNSIGNED NOT NULL,
    user_id INTEGER UNSIGNED NOT NULL,
    PRIMARY KEY(group_id, user_id)
);

CREATE TABLE IF NOT EXISTS pasteboard.pb_groups (
    id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(64),
    parent_id INTEGER UNSIGNED,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS pasteboard.pb_categorys (
    id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(64),
    parent_id INTEGER UNSIGNED,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS pasteboard.pb_token (
    user_id INTEGER UNSIGNED NOT NULL,
    token VARCHAR(254) NOT NULL,
    PRIMARY KEY(user_id),
    KEY token (token)
);


CREATE USER 'pasteboard'@'localhost' IDENTIFIED BY 'pasteboard';
GRANT ALL PRIVILEGES ON pasteboard.* TO 'pasteboard'@'localhost';
