--This command lists all the current connections to the MySQL server and their status.
show processlist;

--This command shows the maximum connections allowed by the MySQL server.
show variables like 'max_connections';

--This command shows the current number of connections to the MySQL server.
show status like 'Threads_connected';

--This command shows the current number of active connections to the MySQL server.
show status like 'Threads_running';

--This command shows the current number of connections to the MySQL server that are in the process of being established.
show status like 'Threads_connecting';

--This command shows the current number of connections to the MySQL server that are in the process of being closed.
show status like 'Threads_closing';

--This command shows the current number of connections to the MySQL server that are in the process of being killed.
show status like 'Threads_killed';

--If you want a most recent connection to the MySQL server, you can use the following query:
SELECT * FROM information_schema.processlist ORDER BY Id DESC LIMIT 1;

SET GLOBAL wait_timeout = 60;
SET GLOBAL interactive_timeout = 60;

--This command shows the wait timeout
SHOW GLOBAL variables like 'wait_timeout';

--This command sets the max connections
set GLOBAL max_connections = 1000;