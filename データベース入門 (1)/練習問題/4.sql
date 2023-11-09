with ranked_results as(
    select
    row_number() over(order by score desc, id) '順位',
    name as '名前',
    score as 'スコア'
    from
        results
    order by
        score desc
)
select
    *
from
    ranked_results
where
    `順位` in (1, 2, 3, 10)
