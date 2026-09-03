CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    select salary 
    from (
        select salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
        from employee
    )as t 
    where rnk = N
    limit 1
    

  );
END