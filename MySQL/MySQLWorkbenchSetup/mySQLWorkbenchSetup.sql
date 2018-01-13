USE twitter;

SELECT * FROM tweets;

-- INSERT INTO tweets (tweet, user_id, created_at, updated_at) VALUES ("MERRY CHRISTMAS!!!", 4, NOW(), NOW());

UPDATE tweets SET tweet = "NEW TWEET" WHERE id = 15;

DELETE FROM tweets WHERE id = 22;


