USE Bus_Depots;

SELECT BusDriver.bdno, BusDriver.bdname
FROM BusDriver
WHERE bdsalary < 1800;

SELECT BusDriver.bdno, BusDriver.bdname
FROM BusDriver
WHERE bdname LIKE 'J%';

SELECT * FROM BusDriver
WHERE bdsalary BETWEEN 2000 AND 4000;

SELECT Bus.regno, Bus.model
FROM Bus
WHERE tno = 2 AND dno != 101;

SELECT * FROM Bus
WHERE model LIKE 'Volvo%' OR model LIKE 'Mercedes%'; 

SELECT DISTINCT dno FROM Bus;

SELECT Cleaner.cno, Cleaner.cname,Depot.dname,Depot.daddress
FROM Cleaner
INNER JOIN Depot ON
Cleaner.dno = Depot.dno;


SELECT Training.bdno, BusDriver.bdname, BusType.tdescript
FROM Training
JOIN BusDriver ON 
Training.bdno = BusDriver.bdno
JOIN BusType ON
Training.tno = BusType.tno;

SELECT Cleaner.cno, Cleaner.cname, Depot.dname, Bus.regno, BusType.tno
FROM Bus
JOIN Cleaner ON 
Bus.cno = Cleaner.cno
JOIN BusType ON
Bus.tno = BusType.tno
JOIN Depot ON
Bus.dno = Depot.dno;