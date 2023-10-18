-- List privileges for users user_0d_1 and user_0d_2

SELECT * FROM mysql.user
WHERE user = 'user_0d_1' OR user = 'user_0d_2';

