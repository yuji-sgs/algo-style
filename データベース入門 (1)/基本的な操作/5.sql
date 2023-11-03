with expenses_3months 
    as(
        select
            *
        from
            expenses_april
        union all
            select
                *
            from
                expenses_may
                union all
                    select
                        *
                    from
                        expenses_june
    )

select
    category as 'カテゴリ',
    sum(amount) as '支出額'
from
    expenses_3months
group by
    `カテゴリ`
order by
    `支出額` desc
