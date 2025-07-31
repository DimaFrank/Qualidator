SELECT
    CASE WHEN MAX(sales)>= 22500
          AND MAX(sales)<= 25000
           THEN 1 ELSE 0
    END AS result

FROM ...;
