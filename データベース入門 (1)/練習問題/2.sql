select
    subject as '科目',
    count(score >= 90 or null) as '秀',
    count(score >= 80 and score <= 89 or null) as '優',
    count(score >= 65 and score <= 79 or null) as '良',
    count(score >= 50 and score <= 64 or null) as '可',
    count(score <= 49 or null) as '不可'
from
    grades
group by
    subject
