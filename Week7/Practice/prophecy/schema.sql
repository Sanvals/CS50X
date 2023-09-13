CREATE TABLE new_students (
    id INTEGER,
    students_name TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE houses (
    id INTEGER,
    house TEXT,
    head TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE relations (
    id INTEGER,
    students_name TEXT,
    house TEXT,
    PRIMARY KEY(id)
);