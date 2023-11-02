-- 内陸県を取得する SELECT 文のサブクエリ作成
with
    inland_prefectures
as (
    -- ここに適切なクエリを記述してください
    select
        *
    from
        prefectures
    where
        name in (
            "栃木県", "群馬県", "埼玉県", "山梨県", 
            "長野県", "岐阜県", "滋賀県", "奈良県"
        )
)
-- 内陸県のデータを面積が大きい順に表示
select
    *
from
    inland_prefectures
order by
    area desc;
