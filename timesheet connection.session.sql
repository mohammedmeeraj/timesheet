use timesheet;
delete from user_logs;
select * from user_logs;
alter table user_logs add constraint unique_name_date unique (employee_id, login_date);
delete from user_logs;
desc user_logs;
select * from users;
alter table user_logs add column token varchar(255), add column token_expiry varchar(255);
select username,password from users;
delete from user_logs where id = 121;
alter table user_logs add column regularised enum('Yes','No') default 'No';

CREATE TABLE regularisation(id int primary key auto_increment,
employee_name varchar(200),
date Date not null,
reason varchar(255),
foreign key (employee_name) references users(username) on delete cascade,
unique(employee_name,date),
index (employee_name,date));

drop table regularisation;
SELECT * from regularisation;
delete from regularisation;
alter table user_logs add column state enum('neutral','opened','closed') default 'neutral';