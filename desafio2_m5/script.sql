

CREATE DATABASE desafio2_Francisco_Monroy_666;

CREATE TABLE IF NOT EXISTS INSCRITOS(cantidad INT, fecha DATE, fuente
VARCHAR);
INSERT INTO INSCRITOS(cantidad, fecha, fuente)
VALUES ( 44, '01/01/2021', 'Blog' );
INSERT INTO INSCRITOS(cantidad, fecha, fuente)
VALUES ( 56, '01/01/2021', 'Página' );
INSERT INTO INSCRITOS(cantidad, fecha, fuente)
VALUES ( 39, '01/02/2021', 'Blog' );
INSERT INTO INSCRITOS(cantidad, fecha, fuente)
VALUES ( 81, '01/02/2021', 'Página' );
INSERT INTO INSCRITOS(cantidad, fecha, fuente)
VALUES ( 12, '01/03/2021', 'Blog' );
INSERT INTO INSCRITOS(cantidad, fecha, fuente)
VALUES ( 91, '01/03/2021', 'Página' );
INSERT INTO INSCRITOS(cantidad, fecha, fuente)
VALUES ( 48, '01/04/2021', 'Blog' );
INSERT INTO INSCRITOS(cantidad, fecha, fuente)
VALUES ( 45, '01/04/2021', 'Página' );
INSERT INTO INSCRITOS(cantidad, fecha, fuente)
VALUES ( 55, '01/05/2021', 'Blog' );
INSERT INTO INSCRITOS(cantidad, fecha, fuente)
VALUES ( 33, '01/05/2021', 'Página' );
INSERT INTO INSCRITOS(cantidad, fecha, fuente)
VALUES ( 18, '01/06/2021', 'Blog' );
INSERT INTO INSCRITOS(cantidad, fecha, fuente)
VALUES ( 12, '01/06/2021', 'Página' );
INSERT INTO INSCRITOS(cantidad, fecha, fuente)
VALUES ( 34, '01/07/2021', 'Blog' );
INSERT INTO INSCRITOS(cantidad, fecha, fuente)
VALUES ( 24, '01/07/2021', 'Página' );
INSERT INTO INSCRITOS(cantidad, fecha, fuente)
VALUES ( 83, '01/08/2021', 'Blog' );
INSERT INTO INSCRITOS(cantidad, fecha, fuente)
VALUES ( 99, '01/08/2021', 'Página' );

--1.-
select count(*) from inscritos;
/*
 count
-------
    16
*/

--2.-
select sum(cantidad) from inscritos;
/* sum
-----
 774*/

--3.-
SELECT * FROM INSCRITOS WHERE fecha = (SELECT MIN(fecha) FROM INSCRITOS);
/*
 cantidad |   fecha    | fuente
----------+------------+--------
       44 | 2021-01-01 | Blog
       56 | 2021-01-01 | Página
*/

--4.-
SELECT fecha, SUM(cantidad) as inscritos_x_dia from inscritos group by fecha order by fecha;
/*
   fecha    | inscritos_x_dia
------------+-----------------
 2021-01-01 |             100
 2021-02-01 |             120
 2021-03-01 |             103
 2021-04-01 |              93
 2021-05-01 |              88
 2021-06-01 |              30
 2021-07-01 |              58
 2021-08-01 |             182
*/

--5.-
SELECT fecha, SUM(cantidad) AS total_inscritos FROM INSCRITOS GROUP BY fecha ORDER BY total_inscritos DESC limit 1;

/*
   fecha    | total_inscritos
------------+-----------------
 2021-08-01 |             182
*/
;