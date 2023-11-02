select
    case
        when age <= 14 then '年少人口'
        when age <= 64 then '生産年齢人口'
        else '老年人口'
    end as '年齢3区分',
    sum(total) as '総人口'
from
    population
group by
    `年齢3区分`
