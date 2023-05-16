-- A script that computes the score average of all records in the table second_table of the database hbtn_0c_0
-- Execute: cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT AVG(score) AS average FROM second_table;
