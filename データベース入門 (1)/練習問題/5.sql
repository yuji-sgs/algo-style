with ranking as(
    select
        name as '名前',
        score as 'スコア'
    from
        results
    where
        score = (           
            select max(score)
            from results as res_b
            where res_b.name = results.name
        )
    group by
        name
    order by
        score desc, id
)

select
    row_number() over() '順位',
    *
from
    ranking
