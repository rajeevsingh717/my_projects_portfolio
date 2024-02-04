{{ config(materialized='table') }}

select 
    employee_id as customer_id, 
    first_name||last_name as name,
    email 
from public.employees