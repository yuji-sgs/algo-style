with min_highest as (
    select
        min(station_id) as min_station_id
    from
        temperature_august
    where highest = (
        select min(highest)
        from temperature_august as tmp_b
        where tmp_b.prefecture = temperature_august.prefecture
    )
    group by prefecture
)
select
    *
from
    temperature_august
where station_id in (
    select
        min_station_id
    from
        min_highest
)
order by highest, station_id
