select
    id,
    name,
    subject,
    score,
    case
        when score >= 90 then '秀'
        when score >= 80 then '優'
        when score >= 65 then '良'
        when score >= 50 then '可'
        else '不可'
    end as '評価'
from
    grades
