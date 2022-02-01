/* 3장 */

SELECT *
FROM EMPLOYEES;

SELECT EMPLOYEE_ID, FIRST_NAME, LAST_NAME
FROM EMPLOYEES
ORDER BY EMPLOYEE_ID DESC;

select job_id
from EMPLOYEES;

select employee_id as 사원번호, first_name as 이름, last_name as 성
from EMPLOYEES;

select employee_id, 
    first_name||' '||last_name, 
    email||'@'||'company.com'
from EMPLOYEES;

select employee_id as 사원번호, 
    salary as 급여, 
    salary + 500 as 추가급여, 
    salary - 100 as 인하급여, 
    (salary * 1.1) / 2 as 조정급여
from EMPLOYEES;

select *
from EMPLOYEES
where employee_id >= 105;

select *
from EMPLOYEES
where salary between 10000 and 20000;

select *
from EMPLOYEES
where salary in (10000, 17000, 24000);

select *
from EMPLOYEES
where job_id like 'AD___';

select *
from EMPLOYEES
where MANAGER_ID is null;

select *
from EMPLOYEES
where salary > 4000
    and job_id = 'IT_PROG';

select *
from EMPLOYEES
where salary > 4000
    and job_id in ('IT_PROG', 'FI_ACCOUNT');

select *
from EMPLOYEES
where employee_id != 105;

select *
from EMPLOYEES
where manager_id is not null;

/* 4장 */

select last_name,
    lower(last_name) lower적용,
    upper(last_name) upper,
    email,
    initcap(email) initcap
from employees;

select job_id, substr(job_id, 1, 2)
from employees;

select job_id, replace(job_id, 'ACCOUNT', 'ACCNT')
from employees;

select first_name, lpad(first_name, 12, '*') lpad적용결과
from employees;

select job_id,
    ltrim(job_id, 'F') ltrim,
    rtrim(job_id, 'T') rtrim
from employees;

select 'start'||trim('   - space -   ')||'end'
from dual;

select salary,
    salary/30,
    round(salary/30, 0),
    round(salary/30, 1),
    round(salary/30, -1)
from employees;

select salary,
    salary/30,
    trunc(salary/30, 0),
    trunc(salary/30, 1),
    trunc(salary/30, -1)
from employees;

select TO_CHAR(sysdate, 'yy/mm/dd/hh24:mi'),
    sysdate+1,
    sysdate-1,
    to_date('20171202')-to_date('20171201'),
    sysdate + 13/24
from dual;

select sysdate,
    hire_date,
    months_between(sysdate, hire_date)
from employees
where department_id = 100;

select hire_date,
    add_months(hire_date, 3),
    add_months(hire_date, -3)
from employees
where employee_id between 100 and 106;

select hire_date,
    next_day(hire_date, '금요일'),
    next_day(hire_date, 6)
from employees
where employee_id between 100 and 106;

select hire_date,
    last_day(hire_date)
from employees
where employee_id between 100 and 106;

select hire_date,
    round(hire_date, 'month'),
    round(hire_date, 'year'),
    trunc(hire_date, 'month'),
    trunc(hire_date, 'year')
from employees
where employee_id between 100 and 106;

select 1 + '2'
from dual;

select sysdate,
    to_char(sysdate, 'cc'), 
    to_char(sysdate, 'yyyy'), 
    to_char(sysdate, 'y,yyy'), 
    to_char(sysdate, 'year'), 
    to_char(sysdate, 'ad'), 
    to_char(sysdate, 'q'), 
    to_char(sysdate, 'mm'), 
    to_char(sysdate, 'month'), 
    to_char(sysdate, 'mon'), 
    to_char(sysdate, 'rm'), 
    to_char(sysdate, 'ww'), 
    to_char(sysdate, 'dd'),
    to_char(sysdate, 'day'),
    to_char(sysdate, 'dy'), 
    to_char(sysdate, 'j')
from dual;

select to_char(sysdate, 'hh:mi:ss PM'),
    to_char(sysdate, 'yyyy/mm/dd hh:mi:ss PM'),
    to_char(sysdate, 'hh-mi-ss PM'),
    to_char(sysdate, ' "날짜:" yyyy/mm/dd "시각:" hh:mi:ss PM')
from dual;

select to_char(salary, '999999999'),
    to_char(salary, '099999999'),
    to_char(salary, '$99999999'),
    to_char(salary, 'L99999999'),
    to_char(salary, '9999999.99'),
    to_char(salary, '999,999,999')
from employees;

select to_number('123')
from dual;

select to_date('20171007', 'yymmdd')
from dual;

select SALARY * nvl(COMMISSION_PCT, 1)
from EMPLOYEES
order by COMMISSION_PCT;

select first_name,
    last_name,
    department_id,
    salary,
    decode(department_id, 60, salary*1.1, salary),
    decode(department_id, 60, '10% 인상', '미인상')
from EMPLOYEES;

select employee_id,
    first_name,
    last_name,
    salary,
    case
        when salary >= 9000 then '상위급여'
        when salary between 6000 and 8999 then '중위급여'
        else '하위급여'
    end as 급여등급
from employees
where job_id = 'IT_PROG'
;

select employee_id,
    salary,
    rank()          over(order by salary desc),
    dense_rank()    over(order by salary desc),
    row_number()    over(order by salary desc)
from employees;

select a.employee_id,
    a.department_id,
    b.department_name,
    salary,
    rank()          over(partition by a.department_id order by salary desc) rank_급여,
    dense_rank()    over(partition by a.department_id order by salary desc) dense_rank_급여,
    row_number()    over(partition by a.department_id order by salary desc) row_number_급여
from employees a, departments b
where a.DEPARTMENT_ID = b.DEPARTMENT_ID
order by b.DEPARTMENT_ID, a.SALARY desc;

select count(salary) salary행수
from EMPLOYEES;

select sum(salary) 합계,
    avg(salary) 평균,
    sum(salary)/count(salary) 계산평균
from EMPLOYEES;

select max(salary), min(salary), max(first_name), min(first_name)
from EMPLOYEES;

select job_id 직무,
    sum(salary) 직무별_총급여,
    avg(salary) 직무별_평균급여
from EMPLOYEES
where EMPLOYEE_ID >= 10
group by job_id
order by 직무별_총급여 desc, 직무별_평균급여;

select job_id job_id_대그룹,
    manager_id manager_id_중그룹,
    sum(salary) 그룹핑_총급여,
    avg(salary) 그룹핑_평균급여
from EMPLOYEES
where employee_id >= 10
group by job_id, manager_id
order by 그룹핑_총급여 desc, 그룹핑_평균급여;

select job_id 직무, sum(salary) 직무별_총급여, avg(salary) 직무별_평균급여
from employees
where employee_id >= 10
group by job_id
having sum(salary) > 30000
order by 직무별_총급여 desc, 직무별_평균급여;

/* 6장 */
select *
from EMPLOYEES a, DEPARTMENTS b
where a.DEPARTMENT_ID = b.DEPARTMENT_ID;

select a.EMPLOYEE_ID, a.DEPARTMENT_ID, b.DEPARTMENT_NAME, c.LOCATION_ID, c.CITY
from EMPLOYEES a, departments b, locations c
where a.DEPARTMENT_ID = b.DEPARTMENT_ID
    and b.LOCATION_ID = c.LOCATION_ID;

select count(*) 조인
from EMPLOYEES a, DEPARTMENTS b
where a.DEPARTMENT_ID = b.DEPARTMENT_ID;

select a.EMPLOYEE_ID, a.FIRST_NAME, a.LAST_NAME, b.DEPARTMENT_ID, b.DEPARTMENT_NAME
from EMPLOYEES a, DEPARTMENTS b
where a.DEPARTMENT_ID = b.DEPARTMENT_ID(+)
order by a.EMPLOYEE_ID;

select a.EMPLOYEE_ID, a.FIRST_NAME, a.LAST_NAME, b.DEPARTMENT_ID, b.DEPARTMENT_NAME
from EMPLOYEES a, DEPARTMENTS b
where a.DEPARTMENT_ID(+) = b.DEPARTMENT_ID
order by a.EMPLOYEE_ID;

select a.EMPLOYEE_ID, a.FIRST_NAME, a.LAST_NAME, a.MANAGER_ID,
    b.FIRST_NAME||' '||b.last_name manager_name
from EMPLOYEES a, EMPLOYEES b
where a.MANAGER_ID = b.EMPLOYEE_ID
order by a.EMPLOYEE_ID;

select DEPARTMENT_ID
from EMPLOYEES
union
select DEPARTMENT_ID
from DEPARTMENTS;

select DEPARTMENT_ID
from EMPLOYEES
union all
select DEPARTMENT_ID
from DEPARTMENTS;

select DEPARTMENT_ID
from EMPLOYEES
intersect
select DEPARTMENT_ID
from DEPARTMENTS;

select DEPARTMENT_ID
from DEPARTMENTS
minus
select DEPARTMENT_ID
from EMPLOYEES;


/* 7장 */

select *
from EMPLOYEES a
where a.SALARY = (
                    select salary
                    from EMPLOYEES
                    where last_name = 'De Haan'
                    );

select *
from EMPLOYEES a
where a.SALARY in (
                    select min(salary)
                    from EMPLOYEES
                    group by department_id
                    )
order by a.SALARY desc;

select *
from EMPLOYEES a
where (a.job_id, a.salary) in (
                                select job_id, min(salary)
                                from EMPLOYEES
                                group by job_id
                                )
order by a.salary desc;

select *
from EMPLOYEES a,
                  ( select department_id
                    from departments
                    where department_name = 'IT' ) b
where a.department_id = b.department_id;

/* 8장 */



