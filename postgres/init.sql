-- Create a sample table
CREATE TABLE IF NOT EXISTS mytable (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description TEXT
);

-- Insert a sample record
INSERT INTO mytable (name, description) VALUES ('Sample Name', 'This is a sample record.');

