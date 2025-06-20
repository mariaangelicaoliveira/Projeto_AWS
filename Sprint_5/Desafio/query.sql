SELECT
    AVG(CAST(chegadas AS FLOAT))
FROM
    s3object;

SELECT
    SUM(CAST(chegadas AS FLOAT))
FROM
    s3object;

SELECT
    UPPER(s.continente),
    s.pais,
    DATE_ADD (month, CAST(s.cod_mes AS INT), `2023T`),
    CASE s.continente
        WHEN 'Europa' THEN 'Euro'
        ELSE 'Dollar'
    END,
    CASE
        WHEN CAST(chegadas AS FLOAT) >= 169 THEN 'Acima da media'
        ELSE 'Abaixo da media'
    END
FROM
    s3object AS s
WHERE
    (
        CAST(s.cod_continente AS INT) >= 4
        AND CAST(s.cod_continente AS INT) <= 6
    )
    OR CAST(s.cod_continente AS INT) = 1
LIMIT
    10;