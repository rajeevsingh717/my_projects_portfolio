{{ config(materialized='table') }}

with customers as (
    
    select *
from {{ ref('stg_customers') }}

),

orders as (

select *
from {{ ref('stg_orders') }}

),

customer_orders as (

    select c.customer_id,name,email,order_id,order_date, order_status
        from customers c 
             full join orders o on c.customer_id=o.customer_id



)

select * from customer_orders
