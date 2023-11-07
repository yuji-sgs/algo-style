select
    *
from
    users
where
    name like '%RURU'
    and flg_data_public = 1
    and rank is null;
