DROP TABLE IF EXISTS OURKIDS.COMPLAINTS;
DROP TABLE IF EXISTS OURKIDS.USER;

CREATE TABLE OURKIDS.COMPLAINT(
    ID              BIGINT          NOT NULL UNIQUE AUTO_INCREMENT, 
    NAME            VARCHAR(255)    NOT NULL,
    STATUS          BIT             NOT NULL DEFAULT 1,
    DESCRIPTION     VARCHAR(255),

    CONSTRAINT PK_COMPLAINT PRIMARY KEY (ID)
);

CREATE TABLE OURKIDS.USER(
    ID              BIGINT          NOT NULL UNIQUE AUTO_INCREMENT, 
    USERNAME        VARCHAR(255)    NOT NULL,
    STATUS          BIT             NOT NULL DEFAULT 0,
    PASSWORD        VARCHAR(255),

    CONSTRAINT PK_USER PRIMARY KEY (ID)
);