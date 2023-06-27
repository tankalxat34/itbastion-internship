-- Language:            SQLite3
-- Migration stage:     1
-- Author:              Alexander Podstrechnyy <tankalxat34@gmail.com>
-- Description:         First migration to create structure for application

DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);