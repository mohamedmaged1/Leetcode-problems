with a as (select rank() over (partition by player_id order by event_date) rankk,player_id,event_date   from Activity)

select  player_id , event_date as first_login  from a
group by player_id