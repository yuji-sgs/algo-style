select
    id, 
    name as "都道府県名",
    population / area as "人口密度"
from
    prefectures
order by
    `人口密度` desc
