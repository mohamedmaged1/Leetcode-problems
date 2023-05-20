select T.email as Email  from(select email,count(email) As countEmail from person group by email) As T 
where  T.countEmail >1