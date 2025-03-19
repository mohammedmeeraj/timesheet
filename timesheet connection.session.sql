use timesheet;
delete from user_logs;
select * from user_logs;
alter table user_logs add constraint unique_name_date unique (employee_id, login_date);
delete from user_logs;
desc user_logs;
alter table user_logs add column token varchar(255), add column token_expiry varchar(255);
select username,password from users;

