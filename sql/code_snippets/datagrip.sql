-- I use this sql snippets everytime I set up datagrip, I found them really useful

-- sec: Select count(*) from a table
SELECT count(*) FROM table_name;

-- selcu: see duplicates on a column on a given table 
SELECT 1, count(*)
FROM table_name
GROUP BY 1
ORDER BY 2 DESC;

-- cas: Create a temporary table
DROP TABLE IF EXISTS table_name;
CREATE TEMP TABLE table_name AS (

);

-- drs: drop table 
DROP TABLE IF EXISTS table_name;
