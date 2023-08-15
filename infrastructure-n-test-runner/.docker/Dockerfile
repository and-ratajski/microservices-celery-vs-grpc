FROM postgres:15.4-alpine AS base
COPY ./init-tables.sql /docker-entrypoint-initdb.d/
