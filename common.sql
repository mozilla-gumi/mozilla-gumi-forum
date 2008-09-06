
CREATE TABLE ua_list (
  id            int         UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  ua            text                 NOT NULL                            ,
  count         int         UNSIGNED NOT NULL                            ,
  os            int         UNSIGNED     NULL                            ,
  browser       int         UNSIGNED     NULL                            
);

CREATE TABLE auth (
  uid           int         UNSIGNED NOT NULL                            ,
  cookie        tinytext             NOT NULL                            ,
  lastdate      DATETIME             NOT NULL                            
);

CREATE TABLE profiles (
  uid           int         UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  uname         tinytext             NOT NULL                            ,
  mailaddr      tinytext             NOT NULL                            ,
  password      tinytext             NOT NULL                            
);


