select
    *
from
    prefectures
where
    name in 
        (select name from kanto_regions);
