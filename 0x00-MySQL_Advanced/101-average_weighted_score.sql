DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE total_score FLOAT DEFAULT 0;
    DECLARE total_weight INT DEFAULT 0;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        SET total_score = 0;
        SET total_weight = 0;
        
        SELECT SUM(c.score * p.weight), SUM(p.weight)
        INTO total_score, total_weight
        FROM corrections c
        INNER JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        IF total_weight > 0 THEN
            UPDATE users
            SET average_score = total_score / total_weight
            WHERE id = user_id;
        ELSE
            UPDATE users
            SET average_score = 0
            WHERE id = user_id;
        END IF;
    END LOOP;

    CLOSE cur;
END $$

DELIMITER ;
