select C.name as Customers from Customers C where 
c.id not in (select customerid from orders)
