
select 
app_id, 
count(userid) 
from usage_data 
where ageGroup = "" and location = ""
group by app_id
order by count(userid)