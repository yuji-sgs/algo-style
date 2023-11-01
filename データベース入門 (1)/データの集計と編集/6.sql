select
    name as '顧客名',
    sum(amount) as '合計金額'
from
    ledger
where
    date between '2022-08-08' and '2022-08-14'
group by
    name
having
    `合計金額` >= 5000
