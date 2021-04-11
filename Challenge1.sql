
CREATE DATABASE famous_scientists;

CREATE TABLE scientists(
id INT(4) NOT NULL AUTO_INCREMENT,
name VARCHAR(255) NOT NULL,
discovery TEXT NOT NULL,
year_of_birth INT(4) NOT NULL,
year_of_death INT(4) default NULL,
PRIMARY KEY(id)
)AUTO_INCREMENT=1;  