-- crear conexion al human resources de oracle
ALTER USER hr ACCOUNT UNLOCK;
ALTER USER hr IDENTIFIED BY hr;
-- crear usuario para pruebas
CREATE USER tests IDENTIFIED BY tests;

