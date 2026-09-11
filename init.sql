CREATE TABLE IF NOT EXISTS deployments (
    id SERIAL PRIMARY KEY,
    version VARCHAR(20) NOT NULL,
    environment VARCHAR(50) NOT NULL,
    status VARCHAR(20) NOT NULL,
    deployed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO deployments (version, environment, status, deployed_at)
VALUES
('v1.0.0', 'Production', 'SUCCESS', NOW() - INTERVAL '4 days'),
('v1.1.0', 'Production', 'SUCCESS', NOW() - INTERVAL '3 days'),
('v1.2.0', 'Staging', 'SUCCESS', NOW() - INTERVAL '2 days'),
('v1.3.0', 'Production', 'SUCCESS', NOW() - INTERVAL '1 day'),
('v1.4.0', 'Production', 'SUCCESS', NOW());