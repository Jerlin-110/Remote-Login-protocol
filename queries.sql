CREATE TABLE  login  (
  id  int NOT NULL,
  username  varchar(45) NOT NULL,
  password  varchar(45) NOT NULL,
  tcap_login boolean NOT NULL,
 PRIMARY KEY ( id ),
 UNIQUE KEY  id_UNIQUE  ( id )
)



INSERT INTO login VALUES (456, "gihun", "squidgame", 1);
INSERT INTO login VALUES (222, "ddak", "ggonji", 0);
INSERT INTO login VALUES (333, "yang", "woo", 0);
INSERT INTO login VALUES (67, "sae", "byeok", 0);
INSERT INTO login VALUES (001,"ilnam", "owner", 1);



CREATE USER 'ism'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON tcap.* To 'ism'@'localhost';
ALTER USER 'ism'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
flush privileges;






CREATE TABLE algo_map (
    id INT PRIMARY KEY,
    algo TINYINT UNSIGNED NOT NULL CHECK (algo BETWEEN 0 AND 13)
);


DELIMITER //

CREATE TRIGGER before_algo_update
BEFORE UPDATE ONalgo_map
FOR EACH ROW
BEGIN
    IF NEW.algo > 13 THEN
        SET NEW.algo = 0;
    END IF;
END;
//

DELIMITER ;



INSERT INTO algo_map (id, algo) VALUES (1, 8), (456, 7);


UPDATE algo_map SET algo = (algo + 1) % 14 WHERE id = 1;




