CREATE TABLE IF NOT EXISTS games_pc(
    id INT NOT NULL,
    name TEXT NOT NULL,
    summary TEXT,
    storyline TEXT,
    rating NUMERIC,
    main_hours NUMERIC,
    extra_hours NUMERIC,
    completionist_hours NUMERIC,
    review_score NUMERIC,
    review_count INT,
    people_polled INT,

    PRIMARY KEY (id)
);