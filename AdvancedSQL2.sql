USE Bus_Depots;

SELECT MIN(BusDriver.bdsalary) AS min_salary, 
MAX(BusDriver.bdsalary) AS max_salary
FROM BusDriver;

SELECT Route.rno, Route.rdescript FROM Route
WHERE Route.dno = 101;


SELECT Route.rno, Route.rdescript FROM Route
JOIN Depot ON
Route.dno = Depot.dno
WHERE Depot.dno = 101;

SELECT * FROM Bus
WHERE Bus.dno IS NULL;

SELECT BusDriver.bdname, BusDriver.bdno FROM BusDriver
WHERE BusDriver.dno NOT IN ('101', '102');

SELECT Depot.dname, AVG(BusDriver.bdsalary)
FROM Depot
JOIN BusDriver ON
Depot.dno = BusDriver.dno
GROUP BY Depot.dname;

SELECT Depot.dname, COUNT(BusDriver.dno) AS no_of_drivers
FROM Depot
JOIN BusDriver ON
Depot.dno = BusDriver.dno
GROUP BY Depot.dname HAVING no_of_drivers > 1;

/*
SELECT Cleaner.cname, Cleaner.cno, COUNT(Bus.tno) AS total_no_of_types
FROM Bus
JOIN Cleaner ON
Bus.cno = Cleaner.cno
JOIN Depot ON
Bus.dno = Depot.dno
JOIN BusType ON
Bus.tno = BusType.tno
WHERE BusType.tno = 1 AND BusType.tno = 3
GROUP BY BusType.tno;
*/

SELECT BusDriver.bdname, BusDriver.bdno, 
Route.rno, Route.rdescript
FROM BusDriver
JOIN Route ON
BusDriver.dno = Route.dno
ORDER BY BusDriver.bdno, Route.rdescript;