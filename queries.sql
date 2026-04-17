USE job_analysis;
DESCRIBE salary;
DESCRIBE ai_jobs;

SELECT * FROM salary LIMIT 5;
SELECT * FROM ai_jobs LIMIT 5;

SELECT COUNT(*) FROM salary;
SELECT COUNT(*) FROM ai_jobs;

SELECT DISTINCT job_title FROM salary;

SELECT job_title, ROUND(AVG(salary_in_usd),2) AS avg_salary
FROM salary
GROUP BY job_title
ORDER BY avg_salary DESC;

SELECT experience_level, ROUND(AVG(salary_in_usd),2) AS avg_salary
FROM salary
GROUP BY experience_level;

SELECT company_location, ROUND(AVG(salary_in_usd),2) AS avg_salary
FROM salary
GROUP BY company_location
ORDER BY avg_salary DESC
LIMIT 10;

SELECT remote_ratio, COUNT(*) AS total_jobs
FROM salary
GROUP BY remote_ratio;

SELECT company_location, COUNT(*) AS total_jobs
FROM ai_jobs
GROUP BY company_location
ORDER BY total_jobs DESC;

SELECT company_name, COUNT(*) AS total_jobs
FROM ai_jobs
GROUP BY company_name
ORDER BY total_jobs DESC
LIMIT 10;

SELECT job_title, COUNT(*) AS total_jobs
FROM ai_jobs
GROUP BY job_title
ORDER BY total_jobs DESC;

SELECT job_title, AVG(salary_in_usd) AS avg_salary
FROM salary
GROUP BY job_title
HAVING avg_salary > 100000
ORDER BY avg_salary DESC;

SELECT company_location, 
COUNT(*) AS total_jobs, 
AVG(salary_in_usd) AS avg_salary
FROM salary
GROUP BY company_location
ORDER BY avg_salary DESC;
