-- script that creates a stored procedure
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INTEGER
)
BEGIN
    DECLARE score_a FLOAT;
    SET score_a = (SELECT AVG(score) FROM corrections AS C WHERE C.user_id=user_id);
    UPDATE users SET average_score = score_a WHERE id=user_id;
END
$$
DELIMITER ;