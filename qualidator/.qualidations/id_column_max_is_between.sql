SELECT
    CASE WHEN MAX(ID)>= 0
          AND MAX(ID)<= 1000
           THEN 1 ELSE 0
    END AS result

FROM ...;
