-- https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-uuid/
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

DROP TABLE IF EXISTS celery_test;
CREATE TABLE celery_test (
    id uuid DEFAULT uuid_generate_v4(),
    test_string VARCHAR(8192) NOT NULL,
    worker CHAR(64) NOT NULL,
    created TIMESTAMP NOT NULL,
    saved TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS grpc_test;
CREATE TABLE grpc_test (
    id uuid DEFAULT uuid_generate_v4(),
    test_string VARCHAR(8192) NOT NULL,
    service CHAR(64) NOT NULL,
    created TIMESTAMP NOT NULL,
    saved TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);
