postgresql://uegsmsrkgaomm8:pfc2fb6bc2755d68700ca31d31c66e5f966621007d1bf721338a4544d868755f6@c67okggoj39697.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d7tfu32ti1me77
BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> c99f043ee839

ALTER TABLE logindatabase ALTER COLUMN username TYPE VARCHAR;

INSERT INTO alembic_version (version_num) VALUES ('c99f043ee839') RETURNING alembic_version.version_num;

COMMIT;

