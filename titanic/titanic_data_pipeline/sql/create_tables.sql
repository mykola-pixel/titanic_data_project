CREATE TABLE IF NOT EXISTS passengers (
    passenger_id INTEGER PRIMARY KEY,
    survived INTEGER,
    pclass INTEGER,
    sex VARCHAR(20),
    age NUMERIC(5, 2),
    sibsp INTEGER,
    parch INTEGER,
    ticket VARCHAR(100),
    fare NUMERIC(10, 2),
    embarked VARCHAR(10),
    deck VARCHAR(20),
    title VARCHAR(50)
);
