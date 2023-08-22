FROM postgres:15.4-alpine AS base
COPY .docker/init-tables.sql /docker-entrypoint-initdb.d/
