#!/bin/bash
psql << EOF
    drop database if exists jwt;
    create database jwt;
    create user dev with password '12345';
    grant all privileges on database jwt to dev;
EOF

psql postgresql://dev:12345@localhost:5432/jwt -a -f dbscript.sql