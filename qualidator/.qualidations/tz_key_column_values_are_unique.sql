SELECT tz_key, COUNT(*)
FROM ...
GROUP BY tz_key
HAVING COUNT(*)>1;
