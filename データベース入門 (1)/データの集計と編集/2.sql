select
    region as "地方名",
    count(region) as "都道府県数",
    sum(area) as "総面積"
from
    prefectures
group by
    region
order by
    `総面積` desc
