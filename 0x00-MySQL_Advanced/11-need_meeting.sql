-- script that creates a view have a score under 80 or more than 1 month
CREATE VIEW need_meeting AS 
SELECT name FROM students 
WHERE 
    score < 80 AND 
    (last_meeting IS NULL 
        OR 
    last_meeting < SUB_DATE(CURDATE(), INTERVAL 1 MONTH));
