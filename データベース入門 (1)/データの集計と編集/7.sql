select
    name as '都道府県名',
    (
        select
            name
        from
            regions
        where
            regions.id = prefectures.region_id
    ) as '地方名'
from
    prefectures
