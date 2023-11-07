with scores as(
    select
        *
    from
        results
    where
        name not in(
            select
                name
            from
                optout
        )
)

select
    row_number() over(order by score desc, id) '順位',
    name as '名前',
    score as 'スコア'
from
    scores
