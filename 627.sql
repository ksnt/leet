# Write your MySQL query statement below
UPDATE salary
    SET
    sex = CASE sex
		  -- f => m
		  WHEN 'f' THEN 'm'
		  -- m => f
		  WHEN 'm' THEN 'f'
    END;